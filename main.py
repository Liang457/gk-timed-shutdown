from tkinter import *
from datetime import datetime, timedelta
import tkinter.messagebox
import password
import time
import cmd_run

win = Tk()
win.title("GK-定时关机")


def _to_off():
    cmd_run.to_off(Time_calculation(), do_what.get())


def get_set_time():
    _now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间
    entry_time.delete(0, END)  # 清空输入框
    entry_time.insert(0, _now_time)  # 写入输入框


def Time_calculation():
    _now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取当前时间
    _set_time = entry_time.get()  # 获取输入框时间

    _set_time = datetime.strptime(_set_time, "%Y-%m-%d %H:%M:%S")  # 将STR字符型时间转化为datetime时间
    _now_time = datetime.strptime(_now_time, "%Y-%m-%d %H:%M:%S")  # 同上

    diff = _set_time - _now_time  # 时间差值计算
    _sec = diff.total_seconds()  # 差值时间变量写入（秒）

    if _sec > 0:
        return _sec  # 如果大于 0 则返回秒数
    elif _sec <= 0:
        return False  # 否则返回False


def PW_QR():
    _str = entryPW.get()  # 获取输入框密码
    r = password.if_true_PW(_str)  # 传入密码检测
    # print(r)
    if r:  # 如果输入正确

        b_in_pw.config(state="disabled")  # 确认按钮更改为禁止
        b_in_new_pw.config(state="normal")  # 更改密码按钮为可行
        b_cancel.config(state='normal')  # 取消当前按钮改为可行
        b_confirm.config(state='normal')  # 确认执行按钮改为可行

        lab1.config(text='密码输入正确')  # 更改提示标签
        entryPW.delete(0, END)  # 清空输入框
    elif not r:  # 如果输入错误，则弹出错误信息框
        tkinter.messagebox.showwarning(title="密码错误", message="密码错误,请重新输入")


def PW_GG():
    i = tkinter.messagebox.askyesno(title="确认更改密码", message="确认更改密码吗?\n更改的密码在密码输入框输入")  # 更改前询问
    if i:  # 如果确认
        _str = entryPW.get()  # 获取输入框文本
        r = password.new_password(_str)  # 传入更改密码函数
        # print(r)
        if r:  # 如果更改成功 ，则弹出信息
            tkinter.messagebox.showinfo(title="密码更改成功", message="密码更改成功")
        elif r == 'error:Matching failed':  # 如果更改失败，则弹出错误信息
            tkinter.messagebox.showinfo(title="密码更改", message="密码更改失败\n密码仅包含数字和英文字母")


# 密码输入
lab1 = Label(win, text="请输入密码:", font=12, justify='left')  # 文本提示
lab1.grid(row=0, column=0)

b_in_pw = Button(win, text="确认密码", command=PW_QR, state="normal")  # 确认按钮
b_in_pw.grid(row=0, column=2)

entryPW = Entry(win, show="*", font='微软雅黑')  # 密码输入框
entryPW.grid(row=0, column=1)

# 更改密码
b_in_new_pw = Button(win, text="更改密码", command=PW_GG, state="disabled")
b_in_new_pw.grid(row=0, column=3)

# 时间输入
Label(win, text="设置关机时间", font=12, justify='left').grid(row=1, column=0)

# noinspection SpellCheckingInspection
entry_time = Entry(win, font='微软雅黑')  # 时间输入框
entry_time.grid(row=1, column=1)

Label(win, text='格式：', font=12).grid(row=2, column=0)
Label(win, text="yyyy-mm-dd hh:mm:ss", font=12, justify='left').grid(row=2, column=1)  # 提示

b_get_now_time = Button(win, text='获取时间', command=get_set_time)  # 获取时间的按钮
b_get_now_time.grid(row=1, column=3)

"""
b_calculation_time = Button(win, text='计算时间', command=Time_calculation)  # 计算时间按钮
b_calculation_time.grid(row=1, column=2)
"""

# 选择关机或重启

do_what = IntVar()  # 选择初始值
do_what.set(1)
Radiobutton(win, text='关机', variable=do_what, value=1).grid(row=3, column=2)  # 关机单选框
Radiobutton(win, text='重启', variable=do_what, value=2).grid(row=3, column=3)  # 重启单选框


# 确定与取消

b_confirm = Button(win, text="确定执行", command=_to_off, state="disabled")
b_confirm.grid(row=4, column=2)  # 确定执行按钮

b_cancel = Button(win, text="取消当前", command=cmd_run.to_cancel, state="disabled")
b_cancel.grid(row=4, column=3)  #　取消当前按钮

# PW_QR()
get_set_time()
win.mainloop()
