import math
a=float(input('podaj a'))
b=float(input('podaj b'))
c=float(input('podaj c'))
while a==0:
      a=float(input('To nie jest funkcja kwadratowa, podaj a różne od zera'))
else:
      delta=b**2-4*a*c
      if delta>0:
          x1=(-b-math.sqrt(delta))/2*a
          x2=(-b+math.sqrt(delta))/2*a
          print(f'Pierwiastki równania kwadratowego to: {x1},{x2}')
      elif delta==0:
          x1=(-b)/2*a
          print(f"Pierwiastek równania kwadratowego to {x1}")
      else:
          print('Funkcja nie posiada pierwiastków kwadratowych')