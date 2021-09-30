import hashlib
import re


def if_true_PW(PW):
    global savePW
    PW = str(PW)
    shaPW = hashlib.sha3_256(PW.encode("utf-8")).hexdigest()

    try:
        f = open("password.data", 'r')
        savePW = f.read()
        f.close()
    except IOError:
        f = open("password.data", 'w')
        f.write('False')
        f.close()

    if savePW == "False":
        return True

    if shaPW == savePW:
        return True
    else:
        return False


def new_password(PW):
    PW = str(PW)  # 字符型输入
    pattern = re.compile("([0-9]|[a-z]|[A-Z])*")  # 匹配数字 大小写字母

    if not pattern.fullmatch(PW):  # 如果匹配不成功则返回报错
        return "error:Matching failed"

    shaPW = hashlib.sha3_256(PW.encode("utf-8")).hexdigest()  # 密码哈希

    f = open("password.data", 'w')
    f.write(str(shaPW))
    f.close()

    return True


if __name__ == '__main__':
    print(new_password(input()))
