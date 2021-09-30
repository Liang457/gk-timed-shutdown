import os
import tkinter.messagebox
import time


def to_off(next_sec, todo):
    global cmd_todo
    if not next_sec:
        tkinter.messagebox.showwarning('错误', '不能使用一个已经过去的时间')
        return 'error:time error'
    elif next_sec > 315360000:
        tkinter.messagebox.showwarning('错误', '时间超过10年(315360000秒)上限')
        return 'error:time out of valid range'

    if todo == 1:
        cmd_todo = '-s'
        todo = '关机'
    if todo == 2:
        cmd_todo = '-r'
        todo = '重启'

    start = time.time()
    tkinter.messagebox.askyesno(title='确认', message=f'确认是在{next_sec}后执行\n(判断时间自动去除)\n执行{todo}')
    end = time.time()

    next_sec = int(next_sec) - int(end - start)
    cmd_all = f'shutdown {cmd_todo} -t {next_sec}'
    # print(cmd_all)
    os.system(cmd_all)


def to_cancel():
    os.system('shutdown -a')
    tkinter.messagebox.showinfo('中止', '中止系统关闭\n如果可能')
