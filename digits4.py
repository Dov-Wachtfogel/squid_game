import random


class digits4:
    def __init__(self):
        self.num = str(random.randint(1000, 9999))
        self.someone_win = False

    def check_num(self, num: int | str):
        num = list(str(num))
        T_num = list(self.num)
        A_num = 0
        B_num = 0
        try:
            for i in range(4)[::-1]:
                if num[i] == T_num[i]:
                    A_num += 1
                    num.pop(i)
                    T_num.pop(i)
        except:
            pass
        try:
            for i in range(len(num)):
                for x in range(len(T_num)):
                    if num[i] == T_num[x]:
                        B_num += 1
                        num.pop(i)
                        T_num.pop(x)
        except:
            pass
        if A_num == 4:
            self.someone_win = True
        return f'{A_num}A{B_num}B'
