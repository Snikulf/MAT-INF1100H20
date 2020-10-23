from numpy import exp
from math import frexp

# Regner ut ett ledd i Taylor-polynomet
def taylorterm(x, lna, i):
    if i == 0:
        return lna
    else:
        a = exp(lna)
        return -(1/i)*(1 - x/a)**i

# Regner ut hele Taylor-polynomet
def taylor(x, lna, n):
    sum = 0.0
    for i in range(n + 1):
        sum += taylorterm(x, lna, i)
    return sum

# Oppgave 1: Regn ut restleddet til Taylor-polynomet
def errorterm(x, lna, n):
    a = exp(lna)
    # TODO: hva blir restleddet?
    return 0

# Deres helt egne logaritme-funksjon, som bruker bl.a. Taylor-polynomet
def taylorlog(x, lna, n):
    mantissa, exponent = frexp(x) # henter ut grunntall og eksponent for tallet x fra minnet i datamaskinen
    log2 = 0.6931471805599453 # ln(2) med maskin-nøyaktighet (16 siffer)
    # TODO: Regn ut ln(x) når vi vet at x = mantissa*2^exponent
    # OBS: Ikke bruk funksjonen log(...) her, bruk taylor(..., lna, n) hvis du trenger en logaritme
    return 0
