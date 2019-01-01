from fractions import Fraction
import numpy as np
#print(2*Fraction(1,4)+Fraction(1,4))

"""K = 310

KO = 4
KI = 140
NaO = 150
NaI = 15
ClO = 0
ClI = 0

K = 310

PK = 1
PNa = 0.333333333
PCl = 0




RT = 8.3144598 * K
F = 9.6485*10*10*10*10

#print(RT/F)
up = PK*KO+PNa*NaO+PCl*ClI
down = PK*KI+PNa*NaI+PCl*ClO
print(up)
print(down)
print(up/down)
res = RT/F * (np.log(up/down))
#res = 58 * np.log2(Fraction(PK*KO,PK*KI)+Fraction(PNa*NaO,PNa*NaI))
#res = RT/ F * np.log2(PK*Fraction(KO/KI)+PNa*Fraction(NaO/NaI+PCl*Fraction(ClI/ClO)))
#res = RT/ F * np.log2(PK*Fraction(KO/KI)+PNa*Fraction(NaO/NaI+PCl*Fraction(ClI/ClO)))


print("{} Volt".format(res))

#f(x) = RT/F * ln(PKo/PKi+Nao/Nai+Cli/Clo)"""

def ghk_equation (K = 310, KO = 4, KI = 140, NaO = 150, NaI = 15, ClO = 0, ClI = 0, PK = 1, PNa = 0.333333333, PCl = 0):

    RT = 8.3144598 * K
    F = 9.6485*10*10*10*10
    up = PK*KO+PNa*NaO+PCl*ClI
    down = PK*KI+PNa*NaI+PCl*ClO
    #print(up)
    #print(down)
    #print(up/down)
    res = RT/F * (np.log(up/down))
    return("{} Volt".format(res))


print(ghk_equation())





