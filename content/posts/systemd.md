---
title: "Systemd"
date: 2022-02-13T11:12:49+08:00
toc: false
images:
series:
  - common skills
tags:
  - untagged
---

In our daily work, we have some repetitive operations, such as simply backing up files or executing scripts, which is very boring for operators.

The damn thing is that these often happen in the company I am intern at. Build and deploy are both manually with tools like `shell` and `sftp`.

In fact, we can easily use `systemd` to solve this repetitive work with `Linux` operation system. Of course, `git flow` is better.

We only need to create a scheduled task, for example, pulling the code every 15min and running it. It's easy to see that there are problems, the service interruption every 15min. We can pull only if the local code is out-date to avoid unnecessary interruption.

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

The `.timer` file will find the `.service` file with the same name, or we can configure it manually.