---
title: "Systemd"
date: 2022-02-13T11:12:49+08:00
toc: false
images:
series:
  - 通用技巧
tags:
  - untagged
---

在日常工作中我们会经常进行一些重复的操作, 如简单的备份文件或执行脚本, 这对操作者来说是非常无趣的事情. 

不幸的是在我此时实习的单位经常就会出这些事, 前端打包, 后端打包, 上传服务器都是人工通过`shell`和`sftp`进行操作的.

其实如果用`Linux`系统, 我们可以很轻易地用`systemd`解决这个重复性的工作. 当然, 用`git flow`其实更好.

我们只需要在服务器上建立一个定时任务, 比如每十五分钟拉取一次代码并构建跑起来. 当然, 这样做会有问题, 比如每五分钟服务中断一次, 但也不是没有解决的方法. 比如只有在本地代码滞后的情况下才拉取, 这样就可以避免不必要的服务中断.

```shell
# /path/to/script/auto-build.sh
cd project_dir
git clone http://fakehost/fake.git
npm run build
cp ./dist/* target_dir
```

```ini
# /etc/systemd/system/auto-build.service
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash /path/to/script/auto-build.sh
```

```ini
# /etc/systemd/system/auto-build.timer
[Unit]
Description=update every 15min

[Timer]
OnCalendar=*:0/15

[Install]
WantedBy=timers.target
```

`.timer` 会去找同名的`.service`文件, 如果不同名, 就得自己去手动配置了.