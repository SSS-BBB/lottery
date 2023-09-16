# Lottery Simulator Project
this is a lottery simulator project. Imagine you buy a lottery, and in order to win you need to guess nth digit number if you're correct you get 10^(n+2) baht, if not you lose 80 baht.

# Expected Value
Expected Value is the value that will predict the long term average out come of random variable.

we will use the concept of lottery, and dice to help us understand more about expected value

https://en.wikipedia.org/wiki/Expected_value

# Code
```python
for i in range(total):
    n = i + 1
    n_list.append(n)

    # random correct n digtis lottery
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
```

we will random a number from 0 to 10^n - 1 two times. If they match then we will get the money if not we will lose.

After that we will calculate the average of the money, and add it to the list, so we can plot those to the graph later.

# Graph
![alt text](https://github.com/SSS-BBB/lottery/blob/main/3digits_lottery.png)

<center>This is a 3 digits random graph.</center>

As you can see from the graph the result of the average money from the loop tend to come close to the expected value.

# A person who writes this code
Suphawit Buaphan
(นายศุภวิชญ์ บัวพันธ์)
