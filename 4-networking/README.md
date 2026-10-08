# Networking Homework

## Task 1: Networking Commands

### 1. ping

**Command:**

```bash
ping -c 4 google.com
```

**Output:**

```text
PING google.com (142.251.220.110): 56 data bytes
64 bytes from 142.251.220.110: icmp_seq=0 ttl=114 time=27.617 ms
64 bytes from 142.251.220.110: icmp_seq=1 ttl=114 time=24.580 ms
Request timeout for icmp_seq 2
64 bytes from 142.251.220.110: icmp_seq=3 ttl=114 time=33.569 ms

--- google.com ping statistics ---
4 packets transmitted, 3 packets received, 25.0% packet loss
round-trip min/avg/max/stddev = 24.580/28.589/33.569/3.734 ms
```

**What I understood:**

`ping` checks whether a host is reachable and measures the time taken to receive a response.

---

### 2. ifconfig

**Command:**

```bash
ifconfig
```

**Output:**

```text
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
anpi1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 82:25:59:66:de:92
	media: none
	status: inactive
anpi0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 82:25:59:66:de:91
	media: none
	status: inactive
en3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 82:25:59:66:de:71
	nd6 options=201<PERFORMNUD,DAD>
	media: none
	status: inactive
en4: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 82:25:59:66:de:72
	nd6 options=201<PERFORMNUD,DAD>
	media: none
	status: inactive
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 36:2f:d6:e2:c9:c0
	media: autoselect <full-duplex>
	status: inactive
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 36:2f:d6:e2:c9:c4
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 36:2f:d6:e2:c9:c0
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x0
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 8 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 9 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
ap1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether a2:9f:8d:73:a6:64
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (none)
	status: inactive
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 4a:30:b5:7f:97:67
	inet6 fe80::8c1:e2f4:1346:e752%en0 prefixlen 64 secured scopeid 0xb 
	inet 192.168.8.32 netmask 0xffffe000 broadcast 192.168.31.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
awdl0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 76:fa:61:cf:f7:b2
	inet6 fe80::74fa:61ff:fecf:f7b2%awdl0 prefixlen 64 scopeid 0xd 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
llw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 76:fa:61:cf:f7:b2
	inet6 fe80::74fa:61ff:fecf:f7b2%llw0 prefixlen 64 scopeid 0xe 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (none)
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
	inet6 fe80::902f:b07d:8f42:a31a%utun0 prefixlen 64 scopeid 0x10 
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::6e97:9efd:5a67:4970%utun1 prefixlen 64 scopeid 0x11 
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::c353:1023:8f24:abc2%utun2 prefixlen 64 scopeid 0x12 
	nd6 options=201<PERFORMNUD,DAD>
utun3: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1000
	inet6 fe80::ce81:b1c:bd2c:69e%utun3 prefixlen 64 scopeid 0x13 
	nd6 options=201<PERFORMNUD,DAD>
bridge100: flags=8a63<UP,BROADCAST,SMART,RUNNING,ALLMULTI,SIMPLEX,MULTICAST> mtu 1500
	options=3<RXCSUM,TXCSUM>
	ether 16:7f:ce:c8:57:64
	inet 192.168.2.1 netmask 0xffffff00 broadcast 192.168.2.255
	inet6 fe80::147f:ceff:fec8:5764%bridge100 prefixlen 64 scopeid 0xf 
	inet6 fd18:dfe3:e791:73ad:8e0:9501:ad64:fa96 prefixlen 64 autoconf secured 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x0
	member: en4 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	member: en3 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
```

**What I understood:**

`ifconfig` displays network interfaces and their configuration, including IP addresses.

---

### 3. ipconfig

**Command:**

```bash
ipconfig getifaddr en0
```

**Output:**

```text
192.168.8.32
```

**What I understood:**

This command displays the local IP address assigned to the Mac's `en0` network interface.

---

### 4. curl

**Command:**

```bash
curl -I https://google.com
```

**Output:**

```text
HTTP/2 301 
location: https://www.google.com/
content-type: text/html; charset=UTF-8
content-security-policy-report-only: object-src 'none';base-uri 'self';script-src 'nonce-JrCAMT0eeH92mKieek15iQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
date: Thu, 03 Sep 2026 08:49:14 GMT
expires: Sat, 03 Oct 2026 08:49:14 GMT
cache-control: public, max-age=2592000
server: gws
content-length: 220
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```

**What I understood:**

`curl` is used to communicate with web servers. The `-I` option retrieves the HTTP response headers.

---

### 5. lsof

**Command:**

```bash
sudo lsof -iTCP -sTCP:LISTEN -P -n
```

**Output:**

```text
COMMAND     PID           USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
launchd       1           root   33u  IPv6 0xae4bd2f10b0df85f      0t0  TCP [::1]:8021 (LISTEN)
launchd       1           root   34u  IPv4 0x144366ab68dbd8a7      0t0  TCP 127.0.0.1:8021 (LISTEN)
launchd       1           root   35u  IPv6 0xae4bd2f10b0df85f      0t0  TCP [::1]:8021 (LISTEN)
launchd       1           root   36u  IPv4 0x144366ab68dbd8a7      0t0  TCP 127.0.0.1:8021 (LISTEN)
mDNSRespo   645 _mdnsresponder   46u  IPv4 0x532d4ae9d726e469      0t0  TCP *:53 (LISTEN)
mDNSRespo   645 _mdnsresponder   48u  IPv6 0xa59d1c14a2374655      0t0  TCP *:53 (LISTEN)
mysqld      791         _mysql   18u  IPv6 0x66f72a7afc0617b0      0t0  TCP *:33060 (LISTEN)
mysqld      791         _mysql   20u  IPv6 0x23a57c46ea5b4a26      0t0  TCP *:3306 (LISTEN)
rapportd    945   mohammedsaad   10u  IPv4 0x1b25a5ad3a0f956e      0t0  TCP *:53425 (LISTEN)
rapportd    945   mohammedsaad   14u  IPv6 0xbc685b34e8cfe46f      0t0  TCP *:53425 (LISTEN)
ControlCe  1039   mohammedsaad    9u  IPv4 0x90b01c7b0ebf6062      0t0  TCP *:7000 (LISTEN)
ControlCe  1039   mohammedsaad   10u  IPv6 0xd3fb9143eda3e448      0t0  TCP *:7000 (LISTEN)
ControlCe  1039   mohammedsaad   11u  IPv4  0xecd135a27771713      0t0  TCP *:5000 (LISTEN)
ControlCe  1039   mohammedsaad   12u  IPv6 0x58eb68468222c33b      0t0  TCP *:5000 (LISTEN)
mongod     1311   mohammedsaad    9u  IPv4 0xb9235c33691b82bb      0t0  TCP 127.0.0.1:27017 (LISTEN)
mongod     1311   mohammedsaad   10u  IPv6 0xc650cab7779da8bf      0t0  TCP [::1]:27017 (LISTEN)
redis-ser  1316   mohammedsaad   12u  IPv4 0xeead8720988c4a89      0t0  TCP 127.0.0.1:6379 (LISTEN)
redis-ser  1316   mohammedsaad   13u  IPv6 0x1224b21c212230d7      0t0  TCP [::1]:6379 (LISTEN)
postgres   1324   mohammedsaad    7u  IPv6 0xd9f50af49668bc1a      0t0  TCP [::1]:5432 (LISTEN)
postgres   1324   mohammedsaad    8u  IPv4 0x38bb5aedf2b897ef      0t0  TCP 127.0.0.1:5432 (LISTEN)
Code\x20H  3296   mohammedsaad   37u  IPv4 0xb692a6290e19be3a      0t0  TCP 127.0.0.1:49829 (LISTEN)
language_ 17593   mohammedsaad    4u  IPv4 0x852c251ee1a7c7f2      0t0  TCP 127.0.0.1:54168 (LISTEN)
language_ 17593   mohammedsaad   33u  IPv4 0x6efbf43a08306766      0t0  TCP 127.0.0.1:54172 (LISTEN)
language_ 17593   mohammedsaad   38u  IPv4 0xba3f29bf4d65368b      0t0  TCP 127.0.0.1:54175 (LISTEN)
Electron  28326   mohammedsaad   66u  IPv4 0x7d1d91a515eca67c      0t0  TCP 127.0.0.1:60751 (LISTEN)
Electron  28326   mohammedsaad   68u  IPv4 0x98d33f01a7a5168d      0t0  TCP 127.0.0.1:60752 (LISTEN)
language_ 28784   mohammedsaad    7u  IPv4 0xc26f3bc68a1bd7f2      0t0  TCP 127.0.0.1:60757 (LISTEN)
language_ 28784   mohammedsaad    8u  IPv4 0xb23d3f21cd401b7b      0t0  TCP 127.0.0.1:60758 (LISTEN)
cursorsan 31214   mohammedsaad   11u  IPv4 0x91dd93e3eba22ea8      0t0  TCP 127.0.0.1:58730 (LISTEN)
cursorsan 31214   mohammedsaad   12u  IPv4 0x44471bf8e244da3c      0t0  TCP 127.0.0.1:58731 (LISTEN)
Python    74320   mohammedsaad   12u  IPv4 0xcdb849b2aec7e452      0t0  TCP *:8000 (LISTEN)
node      86800   mohammedsaad   13u  IPv6 0x503774ed9a77405f      0t0  TCP *:3000 (LISTEN)
Google    97226   mohammedsaad   49u  IPv4 0xbd4349112aad8a69      0t0  TCP 127.0.0.1:9222 (LISTEN)
```

**What I understood:**

`lsof` can show which processes are listening on network ports.

---

### 6. netstat

**Command:**

```bash
netstat -an | grep LISTEN
```

**Output:**

```text
tcp4       0      0  127.0.0.1.54175        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.54172        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.54168        *.*                    LISTEN     
tcp6       0      0  *.53425                *.*                    LISTEN     
tcp4       0      0  *.53425                *.*                    LISTEN     
tcp6       0      0  *.53                   *.*                    LISTEN     
tcp4       0      0  *.53                   *.*                    LISTEN     
tcp4       0      0  127.0.0.1.9222         *.*                    LISTEN     
tcp46      0      0  *.3000                 *.*                    LISTEN     
tcp4       0      0  *.8000                 *.*                    LISTEN     
tcp4       0      0  127.0.0.1.60758        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.60757        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.60752        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.60751        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.49829        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.58731        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.58730        *.*                    LISTEN     
tcp6       0      0  ::1.27017              *.*                    LISTEN     
tcp4       0      0  127.0.0.1.27017        *.*                    LISTEN     
tcp6       0      0  ::1.6379               *.*                    LISTEN     
tcp4       0      0  127.0.0.1.6379         *.*                    LISTEN     
tcp4       0      0  127.0.0.1.5432         *.*                    LISTEN     
tcp6       0      0  ::1.5432               *.*                    LISTEN     
tcp6       0      0  *.5000                 *.*                    LISTEN     
tcp4       0      0  *.5000                 *.*                    LISTEN     
tcp6       0      0  *.7000                 *.*                    LISTEN     
tcp4       0      0  *.7000                 *.*                    LISTEN     
tcp46      0      0  *.3306                 *.*                    LISTEN     
tcp46      0      0  *.33060                *.*                    LISTEN     
tcp4       0      0  127.0.0.1.8021         *.*                    LISTEN     
tcp6       0      0  ::1.8021               *.*                    LISTEN
```

**What I understood:**

`netstat` displays network connections and listening ports.

---

### 7. traceroute

**Command:**

```bash
traceroute google.com
```

**Output:**

```text
traceroute to google.com (142.250.193.174), 64 hops max, 40 byte packets
 1  * dns.nfen (192.168.1.1)  16.666 ms *
 2  * static-193.79.194.14-tataidc.co.in (14.194.79.193)  26.479 ms  19.944 ms
 3  10.117.202.153 (10.117.202.153)  13.132 ms  14.287 ms  10.642 ms
 4  10.129.34.214 (10.129.34.214)  14.818 ms  14.260 ms  23.614 ms
 5  * * *
 6  * * *
 7  172.31.167.58 (172.31.167.58)  39.267 ms  20.363 ms  45.560 ms
 8  14.141.123.226.static-chennai.vsnl.net.in (14.141.123.226)  33.886 ms *  89.853 ms
 9  * * *
10  115.112.15.74.static-chennai.vsnl.net.in (115.112.15.74)  83.324 ms  30.362 ms  26.857 ms
11  192.178.120.187 (192.178.120.187)  29.774 ms  34.288 ms  24.694 ms
12  142.250.235.107 (142.250.235.107)  13.403 ms  49.287 ms  44.097 ms
13  lcmaaa-ay-in-f14.1e100.net (142.250.193.174)  74.158 ms  15.004 ms  34.082 ms
```

**What I understood:**

`traceroute` shows the network hops that packets take to reach a destination.

---

### 8. nslookup

**Command:**

```bash
nslookup google.com
```

**Output:**

```text
Server:		192.168.1.1
Address:	192.168.1.1#53

Non-authoritative answer:
Name:	google.com
Address: 142.250.206.14
```

**What I understood:**

`nslookup` is used to query DNS and find information about a domain name.

---

### 9. dig

**Command:**

```bash
dig google.com +short
```

**Output:**

```text
142.250.206.14
```

**What I understood:**

`dig` performs DNS queries and can be used to find DNS records such as IP addresses.

---

### 10. arp

**Command:**

```bash
arp -a
```

**Output:**

```text
? (169.254.12.197) at e8:b0:c5:34:6e:e9 on en0 [ethernet]
? (169.254.33.201) at 9a:c2:33:62:39:52 on en0 [ethernet]
? (169.254.48.23) at 9c:67:d6:c9:28:fe on en0 [ethernet]
:
:
? (192.168.15.252) at ae:ec:c5:33:8d:12 on en0 ifscope [ethernet]
? (192.168.15.254) at 86:da:b2:84:42:29 on en0 ifscope [ethernet]
? (192.168.31.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
```

**What I understood:**

`arp -a` displays the ARP table, which contains mappings between IP addresses and MAC addresses.

---

### 11. route

**Command:**

```bash
route -n get default
```

**Output:**

```text
   route to: default
destination: default
       mask: default
    gateway: 192.168.1.1
  interface: en0
      flags: <UP,GATEWAY,DONE,STATIC,PRCLONING,GLOBAL>
 recvpipe  sendpipe  ssthresh  rtt,msec    rttvar  hopcount      mtu     expire
       0         0         0         0         0         0      1500         0 
```

**What I understood:**

This command shows the default network route and the gateway used by the Mac to reach external networks.

---

### 12. nc

**Command:**

```bash
nc -vz google.com 443
```

**Output:**

```text
Connection to google.com port 443 [tcp/https] succeeded!
```

**What I understood:**

`nc` (netcat) can be used to test whether a specific network port is reachable.

---

## Conclusion

Through these commands, I learned how to check network connectivity, inspect network interfaces and IP addresses, perform DNS lookups, examine network ports and connections, trace network routes, and test the availability of network services.
