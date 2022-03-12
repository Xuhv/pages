---
title: "迷惑的TS"
date: 2022-03-12T21:38:06+08:00
toc: false
images:
series:
tags:
  - Javascript
---

TS在给JS加上了类型的同时也增加了不少额外的内容, 于是一个有趣的现象出现了, TS程序员用更复杂的语法写着跟JS一样的内容. 正因为这种原因, 我经常看到有人从JS转到TS时`any`一把梭, 活生生写成了`AnyScript`. 那么就盘点下那些复杂得一批又令人令人迷惑的TS语法.

## any & unknown

这俩玩意算是最让人迷惑的东西之一了, 初学者横看竖看都看不出有啥不同. 先来解释下这俩玩意儿是啥用法, `unknown`是任何类型的父类型, 而`any`既是所有类型的子类型, 也是所有类型的父类型.

或许你会觉得`any`这个既是子类型又是父类型很离谱, 但`any`本来就是让不那么熟练的玩家能够在类型系统中找到个逃生窗口, 其设计自然就不能以常理度之. 那么这父子关系不同又有什么关系呢?

```ts
function testAny(a: any): string {
    return a;
}

function testUnknown(a: unknown): string {
    return a;
}
```

在你的IDE中粘贴如上代码, 你就会看到. 子类 -> 父类的过程是类型安全的, 而反过来嘛就不行了.

## union & intersection

这大概是TS中最常用的东西了, 紧接上文, 这俩在"父类子类"这个概念上又该怎么区分呢?

```ts
type A = 'A' | 'a'

let a: A = 'A'

type BTest = 'B' & 'b'

let b: BTest = 'B' // Type 'string' is not assignable to type 'never'.ts(2322)
```

我相信你的编辑器会给出一样的报错的, 原因在于`Union`是"父类型", 而`Intersection`是"子类型". 还是那句话, 从子类到父类不是类型安全的.

当然, 这只是一个简单的例子, 在一些复杂的情况下我们可能会遇到需要将`Union`转化成`Intersection`的需求.

```ts
type A = { a: string }
type B = { b: string }

type AB = A & B // but sometime we can't get the type of `A` and `B` directly
```
在某些情况下, 我们无法直接得到需要合并的两个类型但我们可以得到他们的联合, 那么从联合转换成交叉类型就好了. 下面这个例子有经验的朋友应当能看出来能应用在什么场景.

```ts
const example = {
    module1: {
        get: { getA: () => "A" },
        action: { actionA: () => {} },
    },
    module2: {
        get: { getB: () => "B" },
        action: { actionB: () => {} },
    },
};

type UnionToIntersection<U> = (
    U extends unknown ? (k: U) => void : never
) extends (k: infer I) => void
    ? I
    : never;

type Get = UnionToIntersection<typeof example[keyof typeof example]["get"]>;

type Action = UnionToIntersection<
    typeof example[keyof typeof example]["action"]
>;
```

## infer

上面转换联合的代码中已经用到了范型和推断, 需要注意的是`infer`是需要配合`extend`使用的, 休想在一般的代码中使用这个.

出了上述的例子, 还有一个`Tuple`转`Union`也可以用`infer`实现.

```ts
type MyTuple = [ string, number, boolean ]

type TupleToUnion<T> = T extends Array<infer E> ? E : never

type MyUnion = TupleToUnion<MyTuple>
```

## function overload

这东西有些为了写而写了, JS可以接受任意长度的参数, 其实并不需要这个功能, 写了三函数签名, 其实上面两个根本都没用上, 只是在调用时提供类型支持, 倒是方便写文档? 

```ts
function len(merged: string): number;
function len(s1: string, s2: string): number;
function len(mergedOrS1: string, s2?: string): number {
    if (s2 === undefined) {
        return mergedOrS1.length;
    }
    return mergedOrS1.length + s2.length;
}
```

 其实, 用`overload`的方式来写函数的话, 从参数推断返回类型倒也可行了, 不过我为啥要给一个函数几种不同的返回值呢?

 ```ts
function Test(s: string): string;
function Test(n: number): number;
function Test(sOrN: string | number): number | string {
    if (typeof sOrN === "string") {
        return sOrN;
    }
    else {
        return sOrN + 1;
    }
}
 ```