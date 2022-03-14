---
title: "dataclasses 让类型定义更加简单"
date: 2022-03-14T10:30:29+08:00
toc: false
images:
series:
tags:
  - python
---

我还是个后端时候, 经常觉得dto, vo, entity这些类型定义太过繁琐, 还需要转来转去. 对于后端, 在不考虑可维护性的情况下, 这些东西实在没啥用, 事实上小公司也确实不考虑可维护性(考虑得了吗). 但对于前端, 这东西就很有用了, 没类型定义Swagger上全他妈空着我要这玩意有何用?

现在做前端了嘛, 狗后端给的Swagger看得我只想骂人. 你后端忙就能随意强奸前端的体验吗?

也没啥好抱怨的, 我也做过后端, 那么就来探索下怎么简化这东西让后端能少写点代码吧, 用C#写的话, 用`AutoMapper`可以稍稍简化下, Java也有类似库, 但说实话这种效果不咋地, 语言本身的设计限制了这类操作.

```c#
// type definition
public class XDto {
    public string Name { get; set; }
    public int Age { get; set; }
}
public class XEntity {
    public string Name { get; set; }
    public int Age { get; set; }
    // ...
}

// use
var config = new MapperConfiguration(cfg => // Auto Mapper
    cfg.CreateMap<Employee, EmployeeDTO>()
);
var mapper = new Mapper(config);

var x = new XEntity {
    Name = "John",
    Age = 30
};

var xDto = mapper.Map<XEntity, XDto>(x);
```

用Python的话就好很多了(这个代码要python3.9以上才跑得通), 第三方库都不需要引, 同样的功能只用了更少的代码, 并且逻辑在一处, 更好的面向对象有没有啊?

```python
from dataclasses import dataclass, asdict

@dataclass
class XDto:
    x: str
    y: str

@dataclass
class XEntity(XDto):

    def to_dto(self):
        return XDto(**asdict(self))

x = XEntity('x', 'y')
xDto = x.to_dto()
```

而且, 我们还很容易就能实现一些额外的东西, 比如从多个DTO合并成一个Entity

```python
@dataclass
class XDto2:
    x: str
    z: str

@dataclass
class XEntity(XDto, XDto2):

    @classmethod
    def from_dto(cls, dto: XDto, dto2: XDto2):
        return cls(**(asdict(dto) | asdict(dto2)))

dto1 = XDto('x1', 'y1')
dto2 = XDto2('x2', 'z1')
entity = XEntity.from_dto(dto1, dto2)
```
