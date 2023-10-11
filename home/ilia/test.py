def s(f):
    def inner():
        print(2)
        a = f()
        print(a+22)
        return a
    return inner

@s
def A11():
    #print(dict)
    #print(args)
    return 1
A11()

