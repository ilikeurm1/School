import math

x = int(input('lengte eerste rechthoekzijde:'))
y = int(input('lengte tweede rechthoekzijde:'))
L1 = math.pow(x, 2)
L2 = math.pow(y, 2)
L3 = math.sqrt(L1+L2)

print ("De lengte van de schuine zijde is", round(L3, 2))
