---
title: "Asynchronous in JS"
date: 2022-02-12T16:21:25+08:00
toc: false
images:
series:
    - my front-end
tags:
    - Javascript
---

In general, there is no need to ensure the order of asynchronous request results, but in some case it is necessary to do so.

I met a stupid back-end api. The api gives me a list of image file's id used to request the real URI. It means if the list's length is N, I had to request for N times. So it's necessary to keep the order same every page loading to show same result. Unfortunately, I had just finished my back-end internship and started my first front-end one so that I can't find a solution immediately.

The initial code like this

```javascript
const imgIdList = ["fake1", "fake2"];
const imgUriList = [];

imgIdList.forEach(async (it) => {
    return await fetch(`http://fake-api/${it}`)
        .then((res) => res.json())
        .then((res) => imgUriList.push(res));
});
```

However, the latest `imgIdList` has different order from `imgIdList`. After searching `forEach`'s implement[^1], I found that there is no asynchronous logic in the implement. It did not `await`.

In fact, experienced front-end developer should know `Promise.all`[^2]and `Promise.allSettled`[^3], which can solve this problem well.

But if you  have to do it in a traversal way? Then I discovered a new world:`for ... await of`[^4].

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
[^4]: see[for...await of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of), I say "discovered a new world" because it introduced concepts like `Symbol.asyncIterator`, `Iteration protocols`, etc.
