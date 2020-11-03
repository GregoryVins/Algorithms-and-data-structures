# https://drive.google.com/file/d/1X16iK2XOA7w1tp-jD3Nrf2-nw_RST6wG/view?usp=sharing

"""
Сформировать из введенного числа обратное по порядку входящих
в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""
user_answer = int(input("Введите натуральное число: "))
i = 10
answer = ""
while user_answer:
    answer += f"{user_answer % i}"
    user_answer //= i

print(answer)
