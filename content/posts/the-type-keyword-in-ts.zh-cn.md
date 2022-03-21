---
title: "TS里的type关键词"
date: 2022-03-21T14:15:33+08:00
toc: false
images:
series:
tags:
  - Javascript
---

在Typescript里, 一个经常被问到的问题是`type`和`interface`的区别。网上常会给出`interface`重复定义会合并这样的回答, 似乎也没什么问题, 但从官方文档中, 我们其实可以看到`type`的意思是`Type Alias`, 类型别名, 从这个名字我们可以更好地理解`type`.

```ts
type Union = string | number;
```
我们说上面的类型是个联合类型, 实际上是因为`string | number`是联合类型, 和`type`没有关系, `type`只是起到一个声明别名的作用, 那么在和`interface`进行比较的时候呢?

```ts
type XType = {
  a: string;
  b: number;
}
interface XInterface {
  a: string;
  b: number;
}
```

实际上, 如果我们给代码用上类型标注, 无论是用`XType`还是`XInterface`都一样的, 甚至直接写`{ a: string; b: number }`也是一样的, 那么这个对比就简单了，可以看出`XType`, `XInterface`的用法都与跟所谓的`Object Type`无异, 前者我们已经知道他只是一个别名, 而后者我们知道他可以拓展, 那么答案就很明显了, 作为一个别名, `type`自然是在定义时就已经确定了, 而`interface`则是声明一个可拓展的`Object Type`, 仅此而已, 你甚至可以给一个`interface`来个别名, 然后通过更改`interface`来更改该别名对应的类型.
