from operator import length_hint
from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
isFinish = 'Д'
arr = list()

while True:
    
    print("Будете ли вы генерировать код с цифрами?")
    ans = input("Да = Д, Нет = н: ")
    if ans == 'Д':
        chars += digits
        
    print("Будете ли вы генерировать код со строчными буквами?")
    ans = input("Да = Д, Нет = Н: ")
    if ans == 'Д':
        chars += lowercase_letters
    
    print("Будете ли вы генерировать код с прописными буквами?")
    ans = input("Да = Д, Нет = Н: ")
    if ans == 'Д':
        chars += uppercase_letters
        
    print("Будете ли вы генерировать код со специальными символами?")
    ans = input("Да = Д, Нет = Н: ")
    if ans == 'Д':
        chars += punctuation
        
    print('Исключать ли неоднозначные символы il1Lo0?')
    ans = input("Да = Д, Нет = Н: ")
    if ans == 'Д':
        arr = [i for i in chars if i not in "il1Lo0"]
    break

def generate_password(length, arr):
    passwords = ''
    for i in range(length):
        passwords += choice(arr)
    return passwords

length_password = int(input('Введите длину пароля: '))
amount_password = int(input('Введите количество паролей: '))

for i in range(amount_password):
    print(generate_password(length_password, arr))

    