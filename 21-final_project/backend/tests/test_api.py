import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base, get_db
from app.main import app


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    test_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    def override_get_db():
        with test_session() as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    engine.dispose()


def test_root_and_swagger_docs(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "TaskBoard API"
    assert response.json()["docs"] == "/docs"
    assert client.get("/docs").status_code == 200


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}


def test_ready_checks_database(client):
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "READY"}


def test_ready_returns_service_unavailable_when_database_fails(client):
    class BrokenSession:
        def execute(self, statement):
            raise SQLAlchemyError("database connection failed")

    def broken_get_db():
        yield BrokenSession()

    app.dependency_overrides[get_db] = broken_get_db
    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {"detail": "Database unavailable"}


def test_task_crud_and_stats(client):
    assert client.get("/api/tasks").json() == []
    created = client.post(
        "/api/tasks",
        json={
            "title": "Deploy application",
            "description": "Ship the capstone",
            "priority": "HIGH",
            "assignee": "Student",
        },
    )
    assert created.status_code == 201
    task = created.json()
    task_id = task["id"]
    assert task["title"] == "Deploy application"
    assert client.get(f"/api/tasks/{task_id}").json() == task

    updated = client.put(
        f"/api/tasks/{task_id}",
        json={"status": "IN_PROGRESS"},
    )
    assert updated.status_code == 200
    assert updated.json()["status"] == "IN_PROGRESS"

    stats = client.get("/api/tasks/stats")
    assert stats.status_code == 200
    assert stats.json() == {"total": 1, "todo": 0, "inProgress": 1, "done": 0}

    assert client.delete(f"/api/tasks/{task_id}").status_code == 204
    assert client.get("/api/tasks").json() == []


def test_task_validation_rejects_invalid_payload(client):
    response = client.post(
        "/api/tasks",
        json={"title": "", "priority": "URGENT"},
    )
    assert response.status_code == 422


def test_task_not_found_responses(client):
    assert client.get("/api/tasks/999").status_code == 404
    assert client.put("/api/tasks/999", json={"status": "DONE"}).status_code == 404
    assert client.delete("/api/tasks/999").status_code == 404


def test_metrics_returns_prometheus_output(client):
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text
