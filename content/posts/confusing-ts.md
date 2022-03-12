---
title: "Confusing Typescript"
date: 2022-03-12T21:38:06+08:00
toc: false
images:
series:
tags:
  - Javascript
---

TS add some extra features to JS, so a curious thing happened. TS programmer use more complicated syntax to write the same content as JS. Because of this reason, I often see people who migrated from JS to TS write `any` everywhere. So let's take a look at some of the complicated TS syntax.

## any & unknown

The relationship between them is one of the most confusing things, and beginners can't see any difference when they look anyway. The `unknown` is the supertype of all type, and the `any` type is both the supertype and subtype of all types. You may think it's absurd that `any` is both the supertype and subtype, but it's originally designed to allow to escape the type system. 

The following code show how they differ.

```ts
function testAny(a: any): string {
    return a;
}

function testUnknown(a: unknown): string {
    return a; // Type 'unknown' is not assignable to type 'string'.ts(2322)
}
```

Going from subtype to supertype is not type safe .

## union & intersection

How should these two be distinguished in terms of the concept of supertype and subtype?

```ts
type A = 'A' | 'a'

let a: A = 'A'

type BTest = 'B' & 'b'

let b: BTest = 'B' // Type 'string' is not assignable to type 'never'.ts(2322)
```

I believe your editor will give the same error because `Union` is a "supertype", and `Intersection` is a "subtype". Again, going from subtype to supertype is not type safe .

And in some complex cases, we may need to convert `Intersection` to `Union`.

```ts
type A = { a: string }
type B = { b: string }

type AB = A & B // but sometime we can't get the type of `A` and `B` directly
```

Experienced front-end developer would know the usage scenarios shown in this example.

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

Generic type and `infer` have been used in the above code. It should be noted that `infer` needs to be used with `extend`, and it is impossible to use this in other code.

```ts
type MyTuple = [ string, number, boolean ]

type TupleToUnion<T> = T extends Array<infer E> ? E : never

type MyUnion = TupleToUnion<MyTuple>
```

## function overload

I don't think there is an important reason to use this feature. In the next code block, I write three function signatures, but only the third one is used while defining and only the front two are used while calling. Use union type and option parameters to achieve the same result is ok.

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

In fact, if you write a function with `overload`, it is feasible to infer the return type from the parameters, but why should I give a function several different return types?

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