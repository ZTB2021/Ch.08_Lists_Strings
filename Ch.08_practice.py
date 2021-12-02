import random

for hours in range(9, 13):
    for minutes in range(5, 12):
        print(f"Time {hours:2}:{minutes:02}")

for i in range(100):
    x = random.randrange(100000)
    print(f"My number: {float(x):9.2f}")
List_ = [5, 7, 9, 2, 6]

my_list = [5, 8, 2, 4, 0, 9]

my_list[3] = 'Marc'
print(my_list)
print(len(my_list))

uhs_slogan ="My school is the best!"
for ascii in uhs_slogan:
    print(ord(ascii))

print(uhs_slogan[:13]+"Awesome")








