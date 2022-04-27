---
title: "Dataclasses Make Type Definition Easier"
date: 2022-03-14T10:30:29+08:00
toc: false
images:
series:
tags:
  - python
---

I got troubled in the redundant type definition like `dto` and the conversion between various type when I was a backend programmer. For backend developer, it's no need without considering maintainability. But for frontend is's a useful because they need an api documentation. 

Now I work in frontend, the useless lack of type-defining API documentation always annoys me. I know backend programmers sometimes have a lot of work, but it's not a reason. 

In C#, We can't use `AutoMapper` to simplify the type conversion and Java has similar libraries too. As for type definition, Java can use `Lombok` while C# need no such library.

```csharp
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
var config = new MapperConfiguration(cfg =>
    cfg.CreateMap<Employee, EmployeeDTO>()
);
var mapper = new Mapper(config);

var x = new XEntity {
    Name = "John",
    Age = 30
};

var xDto = mapper.Map<XEntity, XDto>(x);
```

I also know a little of Python, which has a better solution for this problem. In Python, we use no third party library and less code to achieve the more clear logic.(Following code written in python3.10)

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

And we can also create a entity obj from several dto objects.

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
