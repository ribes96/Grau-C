#!/usr/bin/python3

def grade(a):
    # Returns the grade of a polynomial
    if type(a) != int:
        raise Exception("Parameters with bad type")
    if a < 0:
        raise Exception("Polynomials are only represented with unsigned ints")
    if a == 0: return -1
    g = 0
    while True:
        if a < 2**g:
            return g - 1
        g = g + 1
        
def mod(a, d = 283):
    #283 is the binary representation of x^8 + x^4 + x^3 + x + 1
    #283: 100011011
    if type(a) != int:
        raise Exception("Parameters with bad type")
    if a < 0:
        raise Exception("Polynomials are only represented with unsigned ints")
    n = grade(d)
    g = grade(a)
    while g >= n:
        dif = g - n
        p = d * 2**dif
        a ^= p
        g = grade(a)
    return a

def GF_product_p(a, b):
    if type(a) != int or type(b) != int:
        raise Exception("Parameters with bad type")
    if a < 0 or 255 < a or b < 0 or 255 < b:
        raise Exception("Product only allowed in Galois Field")
    
    #print("Los parámetros son")
    #print(a,":   ",bin(a)[2:])
    #print(b,":   ",bin(b)[2:])
    res = []
    l = [128,64,32,16,8,4,2,1]
    for i in l:
        if b >= i:
            res.append(a * i)
            b -= i
            #print("Multiplicamos por",i)
    #print("La lista con la que nos hemos quedado es:")
    #print(res)
    p = 0
    for i in res:
        p ^= i
    #print("Y la respuesta final es")
    #print(p,":   ",bin(p)[2:])
    return mod(p)

def GF_tables(g = 3):
    ini = g
    exp_table = []
    log_table = {}
    
    exp_table.append(1)
    #log_table[g] = 1
    for i in range(1,256):
            exp_table.append(ini)
            log_table[ini] = i
            ini = GF_product_p(ini,g)
    return exp_table,log_table

def GF_product_t(a,b):
    if type(a) != int or type(b) != int:
        raise Exception("Parameters with bad type")
    if a < 0 or 255 < a or b < 0 or 255 < b:
        raise Exception("Product only allowed in Galois Field")
    if a == 0 or b == 0: return 0
    #e,l = GF_tables()
    ai = log_table[a]
    bi = log_table[b]
    return exp_tabl[e(ai + bi)%255]

def GF_generador(g = 3):
    if g == 1: return [1]
    l = []
    ini = g
    while ini != 1:
        ini = GF_product_p(ini,g)
        l.append(ini)
    return l
    
print("Esto está funcionando")
exp_table, log_table = GF_tables()
for i in range(30):
    for j in range(30):
        print(GF_product_t(i,j))
