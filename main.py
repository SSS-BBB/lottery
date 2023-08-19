import matplotlib.pyplot as plt
import numpy as np
import random

total = 100000
n_list = []
correct_list = []
guess_list = []
money_list = []
n_digits = 3

money = 0
last_num = (10**n_digits) - 1
money_if_correct = 10**(n_digits + 2)
money_if_wrong = 80

expectaion_money = ((1/(10**n_digits)) * money_if_correct) + ((last_num/(10**n_digits)) * (-money_if_wrong))
expectaion_money_list = [expectaion_money] * total

average_list = []

for i in range(total):
    n = i + 1
    n_list.append(n)

    # random correct digtis lottery
    correct = random.randint(0, last_num) # 0 -> 00, 1 -> 01, 2 -> 02
    correct_list.append(correct)

    # guess it
    guess = random.randint(0, last_num)
    guess_list.append(guess)

    # guess correct or not
    if guess == correct:
        money += money_if_correct
    else:
        money -= money_if_wrong

    money_list.append(money)
    average = money / n
    average_list.append(average)

# decoration
plt.xlabel("n - times")
plt.ylabel("money")

# graph
# plt.scatter(n_list, correct_list, label="correct digits")
# plt.scatter(n_list, guess_list, label="guess digits", marker="*")
plt.plot(n_list, average_list, label="average money")
plt.plot(n_list, expectaion_money_list, label=str(round(expectaion_money, 2)))

# show
plt.legend()
plt.show()