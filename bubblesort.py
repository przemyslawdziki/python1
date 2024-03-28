lista = [9,1,3,5,6,7,8,4,2,0]

def sortowanie(lista):
    _list = list(lista)
    n = len(_list)
    temp = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if(_list[j] > _list[j+1]):
                temp = _list[j + 1]
                _list[j + 1] = _list[j]
                _list[j] = temp
        print(_list)



sortowanie(lista)