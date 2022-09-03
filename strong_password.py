from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
isFinish = 'Д'

while isFinish == 'Д':
    
    print("Будете ли вы генерировать код с цифрами?")
    ans = input("Да = Д, Нет = н")
    if ans == 'Д':
        chars += digits
        
    print("Будете ли вы генерировать код со строчными буквами?")
    ans = input("Да = Д, Нет = Н")
    if ans == 'Д':
        chars += lowercase_letters
    
    print("Будете ли вы генерировать код с прописными буквами?")
    ans = input("Да = Д, Нет = Н")
    if ans == 'Д':
        chars += uppercase_letters
        
    print("Будете ли вы генерировать код со специальными символами?")
    ans = input("Да = Д, Нет = Н")
    if ans == 'Д':
        chars += punctuation
        
    print('Исключать ли неоднозначные символы il1Lo0?')
    ans = input("Да = Д, Нет = Н")
    if ans == 'Д':
        arr = [i for i in chars if i not in "il1Lo0"]
    
    print(arr)