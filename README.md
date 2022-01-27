# GK\_定时关机

项目地址：[Github](https://github.com/Liang457/gk-timed-shutdown)|[Gitee](https://gitee.com/liang2457/gk-timed-shutdown)

一个定时关机的小工具

**已知问题：当没有选择做什么时，按下`确认执行`会崩溃**

预览：

![img-预览](https://images.weserv.nl/?url=https://i0.hdslb.com/bfs/album/3c1c44a2dd23c885d4a2c52460ce2fdbc056145c.png)

支持通过日历选择日期：

![img-预览](https://images.weserv.nl/?url=https://i0.hdslb.com/bfs/album/d2dd798f1934f2418b62ba17e7ee4cfcf753c31c.png)

相关原理：

在输入时间后并确认后，生成一个`_.bat`文件，并把命令放进去运行

使用要求：

- `python3`（本人使用 `python3.9.7`）
- pyqt5
需求包

更新：

1.1 - 使用pyqt5重构
删除累赘的密码模块

资助我：[微信](https://images.weserv.nl/?url=https://i0.hdslb.com/bfs/album/47bff47bd7f0343cfdcd117f70ed6a086387f287.png)