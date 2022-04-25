---
title: "Variance"
date: 2022-04-25T12:08:35+08:00
toc: false
images:
series:
tags:
    - untagged
---

`covariance` and `contravariance` are terms that refer to the ability to use a more derived type (more specific) or a less derived type (less specific) than originally specified.

```typescript
// covariance
type A {
  a: number | string;
}

let a = { a: 1 }
```

Additionally, functions require extra care.

```typescript
type Fn = (arg: unknown) => unknown

let test: Fn = (s: string) => s // ts(2322)
```

In the above code, the problem is that the interface requires the parameter to be of type unknown, but the implementation only allows the parameter to be of type string.

It can be understood as first declaring an interface and then implementing it, so the implementation should conform to the interface's requirements. So complier gives an error.
