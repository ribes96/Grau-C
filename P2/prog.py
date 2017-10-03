#!/usr/bin/python3

class Polynomial:
    'Represents a polynomial in the Galois Field GF(256)'

    prime = bytes(b'\x01\x1A') # x^8 + x^4 + x^3 + x + 1
    # prime = bytes([0x01, 0x1A]])

    def __bytes_to_string(self, b):
        l = [128, 64, 32, 16, 8, 4, 2, 1]
        retVal = ''
        for by in range(0, len(b)):
            num = int.from_bytes(b[by:by+1], byteorder='big')
            for i in l:
                if num >= i:
                    retVal += '1'
                    num -= i
                else:
                    retVal += '0'
        return retVal
    def __string_to_byte(self, st):
        # TODO permitir polinomios de más de grado 7
        #By the moment only a byte
        l = [128, 64, 32, 16, 8, 4, 2, 1]
        num = 0
        for i in range(8):
            if st[i] == '1':
                num += l[i]
        single_byte = num.to_bytes(1, byteorder='big', signed=False)
        return single_byte
    def __string_to_bytes(self, st):
        # Lo mismo que el de arriba pero con strings arbitrariamente largos
        comp = len(st) // 8
        res = len(st) % 8
        retVal = bytes(0)
        if res > 0:
            mis = ('0' * (8 - res)) + (st[0:res])
            retVal = self.__string_to_byte(mis)
        while res < len(st):
            z = self.__string_to_byte(st[res:res+8])
            retVal = retVal + self.__string_to_byte(st[res:res+8])
            res += 8
        return retVal

    def __int_to_bytes(self, i):
        if i < 0:
            raise ValueError("Es un número negativo")
        if i < 256:
            return bytes([i])
        tmp = i % 256
        b = self.__int_to_bytes(i >> 8)
        b = b + bytes([tmp])
        return b

    def __init__(self, value=bytes(b'\x00')):
        if type(value) == bytes:
            self.value = value
        elif type(value) == str:
            self.value = self.__string_to_bytes(value)
        elif type(value) == int:
            # if value < 0 or 255 < value:
                # raise ValueError("Ese polinomio tiene grado incorrecto")
            self.value = self.__int_to_bytes(value)
    def __repr__(self):
        return self.__bytes_to_string(self.value)

    def __add__(self, other):
        num1 = int.from_bytes(self.value, byteorder='big')
        num2 = int.from_bytes(other.value, byteorder='big')
        # retVal = Polynomial(bytes([num1 ^ num2]))
        retVal = Polynomial(num1 ^ num2)
        # TODO esto no funciona bien
        print("El primero es", num1, "y el segundo es",num2)
        return retVal

    def __bit(self, by, bi):
        o = int.from_bytes(by, byteorder='big')
        masc = 1 << bi
        r = o & masc
        if r: return 1
        return 0

    # return degree of the polynomial
    # 00000000 is considered degree = -1
    def deg(self):
        act = 7
        while act >= 0:
            b = self.__bit(self.value, act)
            if b:
                return act
            act -= 1
        return act

    def __truediv__(self, other):
        # return "Esto es una división"
        ract = self
        dsor = Polynomial(0)
        while ract.degree() >= other.degree():
            dif = ract.degree() -  other.degree()
        return Polynomial('11111111')

    @staticmethod
    def fromDegree(a):
        if a < -1 or 7 < a:
            raise ValueError("Ese grado es incorrecto")
        if a == -1:
            return Polynomial(0)
        num = 1 << a
        return Polynomial(num)


# def GF_product_p(byte a)

print("Crypto-program starts!!")
a = Polynomial('00010000')
b = Polynomial('00001000')
