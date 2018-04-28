num_of_picks = int(input("How man quick picks do you want?\n\n>>>"))
import random
compile = []
for pick in range(num_of_picks):
    num_list = []
    for i in range(6):
        number = random.randint(1, 45)
        num_list.append(number)
    sorted_list = sorted(num_list)
    compile.append(sorted_list)
for list in compile:
    print('{:2} {:2} {:2} {:2} {:2} {:2}'.format(*list))