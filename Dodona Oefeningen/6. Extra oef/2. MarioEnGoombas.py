"""
+ <-----BP(y)---------A--------B--------------AG(x=0)

De invoer bestaat uit 5 regels:
de afstand van de bloempot tot aan de afgrond -> y (geheel getal)
de afstand van Goomba A vanaf de afgrond gemeten (geheel getal)
de richting waarin Goomba A loopt: dit is de letter L voor links en R voor rechts
de afstand van Goomba B vanaf de afgrond gemeten (geheel getal)
de richting waarin Goomba B loopt: ook L of R
"""
## CONSTANTS
v = 1 # meter / minute

## inputs
y = int(input("Afstand y tussen bloempot en afgrond (m): "))
A = int(input("Afstand A tussen Goomba A en afgrond (m): ")) # initial position of Goomba A
B = int(input("Afstand B tussen Goomba B en afgrond (m): ")) # idem for B

## initial speed vectors
VA = v if input("Start Goomba A naar Links of Rechts (L/R) ?") == "L" else -v
VB = v if input("Start Goomba B naar Links of Rechts (L/R) ?") == "L" else -v

T = 0 # expired minutes

## Let the goomba's run as long as they are not in the AG
while (A >= X or B= > x):
  A=A+VA
  B=B+VB
  # check for collision with BP
  if A = y: 
    VA=-VA
  if B = y:
    VB=-VB
  if A = B:
    VB = -VB
    VA = -VA
  T = T + 1
  if (T = 10 * y):
    # Something is wrong here
    break
 
print(f"Het duurt {T} minuten tot beide Goomba's weg zijn")
  
  
