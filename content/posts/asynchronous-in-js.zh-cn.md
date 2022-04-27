---
title: "JS中的异步"
date: 2022-02-12T16:21:25+08:00
toc: false
images:
series:
    - 我的前端
tags:
    - Javascript
---

一般来说并不用太在意异步请求结果的顺序, 但个别情况下保证异步请求结果的顺序是有必要的.

我曾遇到一个奇怪的后端 API, 后端先返回一个图片 id 列表, 然后前端用这个列表去请求到所有图片的的真实 URI 并将图片显示出来, 如果不保证请求结果的有序性, 那么每次刷新显示的结果就可能不一致. 撇开这个脑残的后端设计, 当时我刚结束了后端的实习, 开始做前端, 这问题把我难住了, 下班回家我花了一个多小时琢磨了这个问题才明白.

一开始的代码大概像这样

```javascript
const imgIdList = ["fake1", "fake2"];
const imgUriList = [];

imgIdList.forEach(async (it) => {
    return await fetch(`http://fake-api/${it}`)
        .then((res) => res.json())
        .then((res) => imgUriList.push(res));
});
```

然而`imgIdList`的顺序却与`imgIdList`不一致, 问题出在哪呢? 搜索`forEach`的实现[^1], 就会发现实现中不包含异步相关逻辑, 也就是说在执行异步函数时并没有`await`, 那么这里的`async/await`算是白写了.

其实经验丰富的前端应该是知道`Promise.all`[^2]这个 API 的, 而在"ES2020"中还有 Promise.allSettled[^3], 这俩可以很好的解决这个问题.

但如果非要用遍历的方式来做呢? 于是我发现了新世界:`for ... await of`[^4], 用这个方式可以写出符合我一开始逻辑的代码

```javascript
const imgIdList = ["fake1", "fake2"];
const imgUriList = [];

for await (const it of imgIdList.map(
   // the synchronous function can be replaced by a simple promise
    async (it) => {
        return await fetch(`http://fake-api/${it}`)
            .then((res) => res.json())
    }
) {
    list.push(it)
}

console.log(list)
```

[^1]: https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.foreach
[^2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
[^3]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/allSettled
[^4]: 见 [for...await of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of), 但我说发现了新世界却不是因为这个语法本身, 而是它牵扯出的`Symbol.asyncIterator`, `Iteration protocols`等概念
