# GK_定时关机

[gitee](https://gitee.com/liang2457/gk-timed-shutdown)|[github](https://github.com/Liang457/gk-timed-shutdown)

#### 介绍
一个输入目标时间进行定时关机的小工具

#### 步骤

0.输入密码

1.输入目标时间 （格式：yyyy-mm-dd hh:mm:SS）

2.选择关机或重启

3.确认

#### 关于密码
其实准确来说没有防御性

密码就只是保存在目录下的文件中的 SHA3_256 摘要
再和输入的密码的 SHA3_256 摘要比对

只能说 “防君子不防小人”

在首次使用中要 连续确认两次密码

#### 系统要求
|      | python源文件   | .exe打包文件           |
|------|-------------|--------------------|
| 系统兼容 | 仅Windows    | Windows8及以上64位操作系统 |
| 备注   | 至少是 python3 | -                  |

#### 未来更新
- 使用pyqt5重置界面
- 增加设置界面