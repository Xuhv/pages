---
title: "网络"
date: 2022-02-20T18:44:18+08:00
images:
series:
  - 我的笔记
tags:
  - 网络
---

## OSI 模型

OSI模型是一个概念化的模型，它描述了和标准化了网络通信系统的通信功能，而不考虑其内部结构和技术。

| No. | 层     | 单位     | 描述                                                                                               | 例子            |
|-----|-------|--------|--------------------------------------------------------------------------------------------------|---------------|
| 7   | 应用层   |        | High-level APIs, including resource sharing, remote file access                                  | HTTP, FTP     |
| 6   | 表现层   |        | Translation of data between a networking service and an application                              | MIME, SSL     |
| 5   | 会话层   |        | Managing communication sessions,                                                                 | Sockets       |
| 4   | 传输层   | 段, 数据报 | Reliable transmission of data segments between points on a network                               | TCP, UDP      |
| 3   | 网络层   | 包      | Structuring and managing a multi-node network, including addressing, routing and traffic control | IP, ICMP, ARP |
| 2   | 数据链路层 | 帧      | Reliable transmission of data frames between two nodes connected by a physical layer             | PPP, SLIP     |
| 1   | 物理层   | 位      | Transmission and reception of raw bit streams over a physical medium                             |               |

## IP协议簇: TCP/IP

Comparison of TCP/IP and OSI layering
  - Application: Application, Presentation, Session
  - Transport: Transport
  - Network: Network
  - Network Interface: Data Link, Physical 

### TCP

连接建立：三次握手
{{<mermaid>}}
sequenceDiagram
    A-->>B: SYN: SEQ(X)
    B-->>A: SYN-ACK: SEQ(Y) ACK(X+1)
    A-->>B: ACK: ACK(Y+1)
{{</mermaid>}}

连接终止：四次挥手
{{<mermaid>}}
sequenceDiagram
    A-->>B: FIN: SEQ(X)
    B-->>A: ACK: ACK(X+1)
    B-->>A: FIN: SEQ(Y)
    A-->>B: ACK: ACK(Y+1)
{{</mermaid>}}

see [TCP Segment Structure](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)

### IP

Ipv4: 32 bits, Ipv6: 128 bits

上课的时候学过一个一个什么ABCDE类地址，但后面根本就没听过这说法了，后来才发现 [见他妈的鬼，这玩意原来早就不用了是吧](https://en.wikipedia.org/wiki/Classful_network)，现在用的一般都是子网掩码那一套，即`无分类编址`，我的IP是`192.168.1.9/24`，那我这个子网的网络号就是24个1，这个网就能装253个主机。

而在装虚拟机的时候我们一般会看见两个不同的选项：`NAT`和桥接，NAT就是虚拟机通过宿主机上网，桥接就是俩机子平级。

开发的时候经常会用到`localhost`或者`127.0.0.1`，这是因为后者（`127.0.0.1/8`）是`回环网络`，在IPv6下，回环是`::1/128`

我家里面装宽带送的那个路由器后台写的是中国电信网关，其实是因为很多时候网关和路由器的作用已经被揉在一起了（那为什么不叫网关路由器呢？）


### HTTP/HTTPS

**HTTP/1.1**：这货顶着1.1的名字却是第一个版本，服了。
  - 在1.0的基础上增加了`Pipelining`，但用处不大，队头阻塞还是有。

**HTTP/2**： 
  - 必须得HTTPS
  - 多路复用，这波有效解决了HTTP1.1时的（请求）队头阻塞问题，但TCP数据包这个级别的队头阻塞该咋地还是咋地。
  - 采用了更高效的header压缩方法，并且header也支持了二进制格式，一些文章就说一句“HTTP2支持二进制格式”，属实害人。

**HTTP/3**：
  - 基于UDP（QUIC，谷歌真的稳），QUIC支持TLS，改善了HTTP2中TCP和TLS叠加造成的额外开销
  
**HTTPS**：
  - HSTS：强制使用HTTPS，我这个`.dev`的顶级域名整个被加入了 preload-list，就只能通过HTTPS访问。

