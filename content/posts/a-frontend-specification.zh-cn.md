---
title: "我设想的一个前端开发规范"
date: 2022-02-23T15:34:23+08:00
draft: true
toc: true
images:
series:
  - 我的前端
tags:
  - untagged
---

## 通用

1. 应当配置代码格式化器, 如有必要可加入`git hook`自动格式化代码.

2. 关于`ESlint`, 使用的前提是会用. 样式应该交给`Prettier`这样的格式化器.

## CSS

### 类名

在css的世界里, 选择器或者类名有着各种各样的命名方式, 语义化命名、BEM、原子化的工具类, 在实践中并不能简单地认为哪种最好, 就个人开发的体验, 我总结出一套“最优”的方案. 

1. 善用工具类,  对于flex布局这种使用频率极高的样式, 我喜欢使用工具类, 比如：

```css
.row, .col {
    display: flex;
}
.col {
    flex-direction: column;
}
.grow {
    flex-grow: 1;
}
.noShrink {
    flex-shrink: 0;
}
```

2. 只使用一个语义化的类名, 多了会让人迷惑；BEM不建议使用, 写网站时要完全符合BEM是非常煎熬的事, 写组件库倒是很棒；对于工具类的使用必须克制, 否则便与写行内样式没差了, 个人的感觉是将类名控制在四五个较为合理. 

```html
 <div class="List col">
     <div class="ListItem">1</div>
     <div class="ListItem">2</div>
     <div class="ListItem">3</div>
 </div>

<style>
    .List {
        /* ... */
    }
    .ListItem {
        /* ... */
    }
</style>
```

3. 全局样式与本地样式用大小写进行区分, 一般来说, 将本地类名写在第一位是就可以区分出, 但有时候我们并不需要本地类名, 那么通过首字母大小写来判断是本地还是全局样式就显得更加合理了. 有的人可能不习惯将css驼峰命名, 但实际上这与中划线命名并无本质差别. 

### 行内样式

style属性并不是完全不能使用, 但我认为如果写了行内样式就代表这个样式不会被覆盖了. 行内样式的使用应当是一些非常简单的、不需要也不该复用的样式. 

```html
 <img src="fakeUrl" alt="" style="margin-left: 10px;">
```

## Javascript

### 模块

### 使用ESM

1. 日常使用中我发现很多人仍在使用`require`甚至是将`import`和`require`混用, 这是非常不利于维护的, `import`一般来说只会出现在文件顶部, 而`require`则很容易被滥用以至于分散在文件的各个部分. 这会导致逻辑分散并且使项目丧失重构的能力. 

2. `export` 语句不该随意使用, 我认为大部分情况下单个文件只应该写一个对象, 并`export default`. 在一些特殊情况下, 我们可能会需要命名导出, 比如在入口文件, 在很多库中, 入口文件会提供两种导出, `default`代表不需要tree shake或者默认实例, 命名导出则更好支持tree shake. 但无论那种情况, 都建议立即导出, 这将方便后来的维护者. 

```javascript
// good
export function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        let r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

// bad
function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        let r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

export default uuidv4;
```

3. 单个逻辑不建议超过50行, 单个函数如果超过50行, 或许逻辑过于复杂可以进行拆分. 

4. 单个文件中, `function`和箭头函数最好不要混用. 

### JSDoc

我个人并不喜欢写注释, 但在JS中注释是必不可少的, JS天生就是“anyscript”, 编辑器支持极差, 而JSDoc可以一定程度上改善这个问题. 

![](/img/Screenshot_20220223_163758.png)
![](/img/Screenshot_20220223_163836.png)

详细使用方法见[JSDoc官网](https://jsdoc.app/)

## HTML

1. 属性按照 组件Props、自带属性、`class`、`style`排序, 一目了然. 

2. 嵌套层级不宜过深, 过深可考虑分拆组件

## vue

1. 不要在Vue原型上挂载对象, 这会使该对象失去编辑器支持, 编程将由脑力劳动变为体力工作, 将API请求方法挂载在Vue上简直是噩梦. 

2. 不必要写在SFC中的JS代码请新建JS文件, 在有`ECharts`这类库时, 这些不必要的代码会使SFC变得臃肿难看.
