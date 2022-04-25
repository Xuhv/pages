---
title: "逆变和协变"
date: 2022-04-25T12:08:40+08:00
toc: false
images:
series:
tags:
  - untagged
---

`逆变` 与`协变` covariance**,这俩概念分别是指能使用比原有指定类型派生程度更低和派生程度更高的类型。

```typescript
// covariance
type A {
  a: number | string;
}

let a = { a: 1 }
```

但需要注意的地方是函数的参数

```typescript
type Fn = (arg: unknown) => unknown;

let test: Fn = (s: string) => s; // ts(2322)
```

在上面的代码中, 问题就出在我对逆变协变的理解上, 我以为是这个操作是协变, 把派生程度更高的 string 给派生程度更低的 unknown 嘛, 这还能有错? 然后编译器教会了我做人要谦虚。

事实上,这个代码可以理解为先声明了一个接口然后实现了他, 那么我们的实现应当符合接口的要求, 在接口中, 要求 arg 可以是任意类型, 但在实现中参数只能是 string 类型, 好家伙, 我用一个派生程度更低的函数去实现了一个派生程度更高的函数, 本以为的协变成了逆变, 这不报错就有鬼了。
