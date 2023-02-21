import numpy as np
from itertools import permutations

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

symb = ['+','-','*','/']

def possible(num,sym):
    num_perms=permutations(num)
    all_num_perms=list(num_perms)
    symb_perms=permutations(sym,3)
    all_symb_perms=list(symb_perms)
    ans_symb=[]
    ans_num=[]
    for i in all_num_perms:
        for j in all_symb_perms:
            one=(op[j[0]](i[0],i[1]))
            two=(op[j[1]](one,i[2]))
            three=(op[j[2]](two,i[3]))
            if three==10:
                ans_symb.append(j)
                ans_num.append(i)
    if len(ans_symb)!=0:
        return True, ans_symb, ans_num

condition=False
while condition!=True:
    calc = np.random.randint(10, size=4)
    gen=possible(calc,symb)
    if gen is not None:
        condition=True
        print(calc)
        out=False
        while out!=True:
            guess=input('What number/symbols do you guess? [1+2-3*4] ')
            guess_inp=list(guess)
            Zeta=False
            c=0
            for i in gen[1]:
                c+=1
                if i[0] == guess_inp[1] and i[1] == guess_inp[3] and i[2]==guess_inp[5]:
                    for k in gen[2]:
                        if k[0] == int(guess_inp[0]) and k[1] == int(guess_inp[2]) and k[2] == int(guess_inp[4]) and k[3] == int(guess_inp[6]):
                            print()
                            print('Correct!')
                            print()
                            see_ans=input('See all answers? [y/n] ')
                            if see_ans == 'y':
                                print('All correct answers are: ')
                                for i in range(len(gen[1])):
                                    print()
                                    print(gen[1][i])
                                    print(gen[2][i])
                            out=True
                            Zeta=True
                            break
            if Zeta is False:
                print()
                print('Incorrect')
                print()
                retry=input('Try again? [y/n] ')
                if retry == 'n':
                    out=True
                    print()
                    see_ans=input('See all answers? [y/n] ')
                    if see_ans == 'y':
                        print('All correct answers are: ')
                        for i in range(len(gen[1])):
                            print()
                            print(gen[1][i])
                            print(gen[2][i])