---
title: "Fetch API"
date: 2022-02-14T16:48:46+08:00
toc: false
images:
series:
tags:
  - untagged
---

在这个时间点, 我认为`fetch`终于值得重视起来了.

`fetch`是`XMLHttpRequest`的一个更好的替代品, 但在过去的时间里它却往往被用来与`axios`这一功能强大的库来进行比较, 这让它看起来并没有什么优势. 而`fetch`本身的的一些局限性也使它无法彻底替代`XHR`, 比如说, 请求的中断, 如果一个请求会改变服务器状态, 那么直接忽略该请求是不安全的.

但在2022年, 这个问题不应当再是个问题. 我们有`AbortController`, 并且这个新的API已经有相当好的兼容性[^1].

在`AbortController`的兼容性表格中我们可以看见`node15`也包含在内, 那么问题来了, 众所周知`node`没有原生的`fetch` API, 要这个东西干什么? 于是我发现在最新的`17.5.0`版本中, `node`已经实验性支持了`fetch`[^2].

这意味着`fetch`即将获得与`axios`相同的能力, 在服务端也能使用(如果我们不忽视掉`deno`, 那么这点早就实现了). 可以预见地, `fetch`生态将会接替`axios`的生态位.

[^1]: [MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/AbortController#browser_compatibility) , 需要注意的是, 截至今日, 在中文版MDN中, 该API仍被标记为实验性. 这也导致很多中文的技术文章谈到`AbortController`就会说实验性支持, 其实大多数情况下已经可以放心使用了.
[^2]: https://nodejs.org/en/blog/release/v17.5.0/
