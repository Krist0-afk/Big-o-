# Problema FizzBall
# imprimir 1 .. 100
# si el numero es divisible por 3 -> imprimir Fizz
# si el numero es divisible por 5 -> imprimir Ball
# si el numero es divisible por 3 y 5  -> imprimir FizzBall
# y si no -> imprime el numero

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBall\n")
    elif i % 3 == 0: 
        print ("Fizz\n")
    elif i % 5 == 0:
        print("Ball\n")
    else:    
        print(i, end="\n \n")
    i += 1