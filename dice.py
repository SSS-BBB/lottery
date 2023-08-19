import matplotlib.pyplot as plt
import random

number_of_dice_faces = 6

total = 10000
sum_of_score = 0
average_list = []
n_list = []

# calculate expect value
expected_value = (((number_of_dice_faces*(number_of_dice_faces+1)))/2) / number_of_dice_faces
expected_value_list = [expected_value] * total

for i in range(total):
    n = i + 1

    # random dice
    score = random.randint(1, 6)
    sum_of_score += score

    # calculate average
    average = sum_of_score / n
    average_list.append(average)

    n_list.append(n)

# decoration
plt.xlabel("n - times")
plt.ylabel("average")

# graph
plt.plot(n_list, average_list, label="average score")
plt.plot(n_list, expected_value_list, label="expect")

# show
plt.legend()
plt.show()