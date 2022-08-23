#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.#


cube_rt = int(1000 ** 0.334)
print(cube_rt)

for i in range(10+1):
    print(i**3)


def cubic_printer(num):

    # Get the square root of a number like so:
    cube_rt = int(num ** 0.334)

    print(f'cubic root of num: {cube_rt}')

    for i in range(cube_rt+1):
        print(i ** 3)

    cubic_printer(1000)

# check = 32 ** 2
# print(check)

# Get first prime numbers up to 100
Number = 1

while (Number <= 100):
    count = 0
    i = 2

    while (i <= Number//2):
        if (Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" % Number)
    Number = Number + 1


# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


answer = int(input('what is your age?'))

if answer < 18 :
    print("kids")
elif answer >= 18 and answer <=65:
    print("adults")
else:
    print("seniors")

