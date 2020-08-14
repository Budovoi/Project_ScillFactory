#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
number = np.random.randint(1,101) # загадали число


def game_core_v3(number):
    '''Сначала устанавливаем среднее из интервала, а потом уменьшаем 
       или увеличиваем его на половину оставшегося интервала, в
       зависимости от того, больше оно или меньше искомого числа.  
       Функция принимает загаданное число и возвращает число попыток.
       '''
    pos_ans = [x for x in range(1, 101)]
    count = 0
    low = pos_ans[0] # нижняя граница интервала
    high = len(pos_ans) # верхняя граница интервала
    while low <= high:
        count += 1
        mid = (low+high) / 2
        predict = pos_ans[int(mid)]
        if predict == number:
            return count
        elif predict > number:
            high = mid - 1
        else:
            low = mid + 1
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра
    угадывает число.
    '''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)

