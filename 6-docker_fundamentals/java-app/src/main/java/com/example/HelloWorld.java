package com.example;

import static spark.Spark.get;
import static spark.Spark.port;

public class HelloWorld {
    public static void main(String[] args) {
        port(8080);
        get("/", (req, res) -> "<h1>Hello World from Java!</h1>");
    }
}
