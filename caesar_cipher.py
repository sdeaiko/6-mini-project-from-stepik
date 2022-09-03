symbols = ' !.,?"()-:'

en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lower = 'abcdefghijklmnopqrstuvwxyz'
ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def encryption(s, language, n):
    
    lan_upper = ''
    lan_lower = ''
    
    if language == 'А':
        lan_upper = en_upper
        lan_lower = en_lower
    elif language == 'Р':
        lan_upper = ru_upper
        lan_lower = ru_lower
        
    s_ans = ''
    
    for i in range(len(s)):
        for j in range(len(lan_lower)):
            if s[i] == lan_lower[j]:
                s_ans += lan_lower[((j+n) % len(lan_lower))]
            elif s[i] == lan_upper[j]:
                s_ans += lan_upper[((j+n) % len(lan_upper))]
        if s[i] in symbols:
            s_ans += s[i]
    return s_ans
            
def decryption(s, language, n):
    
    lan_upper = ''
    lan_lower = ''
    
    if language == 'А':
        lan_upper = en_upper
        lan_lower = en_lower
    elif language == 'Р':
        lan_upper = ru_upper
        lan_lower = ru_lower
        
    s_ans = ''
    
    for i in range(len(s)):
        for j in range(len(lan_lower)):
            if s[i] == lan_lower[j]:
                s_ans += lan_lower[((j-n) % len(lan_lower))]
            elif s[i] == lan_upper[j]:
                s_ans += lan_upper[((j-n) % len(lan_upper))]
        if s[i] in symbols:
            s_ans += s[i]
    return s_ans


isFinish = 'y'


while isFinish == 'y':
        direction = input("Ш - Шифрование, Д - Дешифрование: ")
        cipher_lan = input("Р - Русский, А - Английский: ")
        n = int(input('Шаг сдвига: '))
        s = input('Введите ваш текст: ')
    
        if direction == 'Ш':
            print('Output: ', encryption(s, cipher_lan, n))
        elif direction == 'Д':
            print('Output: ', decryption(s, cipher_lan, n))
    
        isFinish = input("Хотите ли вы продолжить?(y = yes): ")

    
