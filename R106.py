from math import e
from math import cos, sin, log, pi

def CORDIC(x,N=100):  #calcul de cos,sin,tan
    # x entre 0 et pi/2 mini
    from math import e
    from math import cos, sin, log, pi
    A, B = 1.0, 0.0 # a c'est cos b c'est sin de l'angle0
    tableau_cos = [A]
    tableau_sin = [B]
    reste = x
    for i in range(N):
        angle = pi / 2**(i+1)  # ca fait pi/4 puis /8 ect
        if reste >= angle: # on sépare les morceau je crois
            reste -= angle
            C, s = cos(angle), sin (angle)
            A,B = A*C - B*s, B*C + A*s # additione tout
    return A, B    # (cos de x, sin  de x)

print("le CORDIC vaut",CORDIC(90))
# explication : on prend deux angle qu'on choisi la c'est 1.0 et  0.0 
# puis on veut que ça s'additione  ou soustrait pour calcuer le cos et sin respectivement
# on prend la liste d'angle qui diminue de moitié a chaque fois 
# on check si pi/4 rentre dans 1.0 par exemple


def Newton_Raphson(a,k,xdeb = 1.0, N = 100):
    x = xdeb
    for pif in range(N): # on fait àa un nb donné de fois
        x = ((k+1)*x - a*x**(k+1)) / k    # x devient la prochaine valeur
        return 1/x # on inverse apparament 
    
print("Le cos est normalement de ",Newton_Raphson(2,2,1.0,100))
print("et le sin vaut",Newton_Raphson(27,3))


