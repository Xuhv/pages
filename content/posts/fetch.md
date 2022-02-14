---
title: "Fetch API"
date: 2022-02-14T16:48:30+08:00
toc: false
images:
series:
tags:
  - untagged
---

At this point, I think `fetch` is finally worthy of being considered.

`fetch` is a better alternative of `XMLHttpRequest`, but it's always compared with the powerful library `axios` so that it seem like a little weak. And it has some limitations, for example, the lack of native support for aborting a request, if a request will change the server state, then it's not safe to ignore the request, which make it impossible to cover all areas of use of `XHR`.

But in 2022, this problem should not be a problem anymore. We have `AbortController`, and this new API has good browser compatibility[^1].

In the compatibility table of `AbortController`, we can see `node15` is included, so the problem is, `node` doesn't have native `fetch` API, what's the use for it? So I found in the latest `17.5.0` version of `node` has experimental support for `fetch`[^2], which means that `fetch` will have a same ability as `axios`, supporting both browser and server(Emm, `deno` was ignored).

[^1]: https://developer.mozilla.org/en-US/docs/Web/API/AbortController/AbortController#browser_compatibility
[^2]: https://nodejs.org/en/blog/release/v17.5.0/
