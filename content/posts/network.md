---
title: "Network"
date: 2022-02-20T18:44:18+08:00
images:
series:
  - my note
tags:
  - network
---

## OSI Model

The Open Systems Interconnection model (OSI model) is a conceptual model that characterizes and standardizes the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology. 

| No. | Layer        | Protocol data unit | Description                                                                                      | Case          |
| --- | ------------ | ------------------ | ------------------------------------------------------------------------------------------------ | ------------- |
| 7   | Application  |                    | High-level APIs, including resource sharing, remote file access                                  | HTTP, FTP     |
| 6   | Presentation |                    | Translation of data between a networking service and an application                              | MIME, SSL     |
| 5   | Session      |                    | Managing communication sessions,                                                                 | Sockets       |
| 4   | Transport    | Segment, Datagram  | Reliable transmission of data segments between points on a network                               | TCP, UDP      |
| 3   | Network      | Packet             | Structuring and managing a multi-node network, including addressing, routing and traffic control | IP, ICMP, ARP |
| 2   | Data Link    | Frame              | Reliable transmission of data frames between two nodes connected by a physical layer             | PPP, SLIP     |
| 1   | Physical     | Bit                | Transmission and reception of raw bit streams over a physical medium                             |               |

## Internet protocol suite: TCP/IP

Comparison of TCP/IP and OSI layering
  - Application: Application, Presentation, Session
  - Transport: Transport
  - Network: Network
  - Network Interface: Data Link, Physical 

### TCP

Connect establishment
{{<mermaid>}}
sequenceDiagram
    A-->>B: SYN: SEQ(X)
    B-->>A: SYN-ACK: SEQ(Y) ACK(X+1)
    A-->>B: ACK: ACK(Y+1)
{{</mermaid>}}

Connect termination
{{<mermaid>}}
sequenceDiagram
    A-->>B: FIN: SEQ(X)
    B-->>A: ACK: ACK(X+1)
    B-->>A: FIN: SEQ(Y)
    A-->>B: ACK: ACK(Y+1)
{{</mermaid>}}

see [TCP Segment Structure](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)

### IP

Ipv4: 32 bits, [IPv4 Packet Header](https://en.wikipedia.org/wiki/IPv4#Packet_structure).

**Classless Network**: Like [Classful Network](https://en.wikipedia.org/wiki/Classful_network), we can divide the Internet into subnets. The subnet mask is used to determine the size of the subnet. My IP in local network is `192.168.1.9/24`, which means the subnet can contain 254 hosts.

**NAT and Bridge**: When I use virtual machine, I found there are two network options: `NAT` and `Bridge`. The `NAT` is like a router, it hide the virtual machine to a private network, and the `Bridge` make it expose to host's network.

**loopback**: `127.0.0.1/8` is reserved for loopback. The address will redirect to localhost. In IPv6 loopback is `::1/128`.

**gateway**: A gateway connects networks, while a router typically delivers data within a network. Historically, gateways and routers have been separate devices. However, it's becoming more common for their functions to be combined and simply called a router. 

Ipv6: 128 bits, [IPv6 Packet Header](https://en.wikipedia.org/wiki/IPv6_packet).

## HTTP/HTTPS

**HTTP/1.1**: The first version of the HTTP protocol.
  - Pipelining: The client can send multiple requests to the server in a single TCP connection.
  - Head-of-line blocking: Although the client can send multiple requests to the server in a single TCP connection, the server will only respond to the first request immediately.

**HTTP/2**:  
  - Multiplexing: HTTP/1.1 loads resource one after the other, in contrast, HTTP/2 loads resource in parallel with a single TCP connection. No limit on the number of concurrent requests.
  - Server push
  - Header Compression: HTTP/2 uses a more advanced compression method called HPACK that eliminates redundant information in HTTP header packets. 
  - The HTTP/2 Header can be binary or text, while HTTP/1.1 only support text.
  - Only in HTTPS
  - TCP Head-of-line blocking: All transactions are multiplexed over a single TCP connection, meaning that any packet-level head-of-line blocking of the TCP stream simultaneously blocks all transactions being accessed via that connection. 

**HTTP/3**:
  - HTTP/1.1, HTTP/2 based on TCP, HTTP/3 based on QUIC(on UDP).
  - The TLS is in QUIC.

**HTTPS**:
  - HSTS: HTTP Strict Transport Security. It is a method used by websites to declare that they should only be accessed using a secure connection (HTTPS). To increase the security, the entire `.dev` top domain has been included in the `HSTS preload-list`; as a result, popular web browsers will only connect to a `.dev` webpage using HTTPS.

