def shift_n_letters(letter, n):
    num=ord(letter)+(n%26)
    if num>122:
        return chr(96+(num%122))
    elif num<97:
        return chr(122-(96-num))
    else:
        return chr(num)


if __name__ == "__main__":
    print (shift_n_letters('s', 1), 't')
    #>>> t
    print (shift_n_letters('s', 2),'u')
    #>>> u
    print (shift_n_letters('s', 10),'c')
    #>>> c
    print (shift_n_letters('s', -10),'i')
    #>>> i
    print (shift_n_letters('a', -1), 'z')
    print (shift_n_letters('k', -12), 'y')
