# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# Пример:
# ноутбук
#     12

# В случае с английским алфавитом очки распределяются так:
# {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'} – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков; 
# J, X – 8 очков;
# Q, Z – 10 очков.
# Русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# def price_en(str):
    # count = 0
    # if str[i] == 'd' 'g':
    #     print(str[i])
    #     count += 2
    # # elif =

wrd = str(input('Введите слово: ' ))
# print(len(wrd))
count = 0
wrd.lower()
if wrd.isalpha() == 0:
    print('ERROR! Введите только буквы')

count = (wrd.count('a') + wrd.count('e') + wrd.count('i') + wrd.count('o') + wrd.count('u') + wrd.count('l') + wrd.count('n') +
    wrd.count('s') + wrd.count('t') + wrd.count('r') + 
    wrd.count('d')*2 + wrd.count('g')*2 + 
    (wrd.count('b') + wrd.count('c') +  wrd.count('m') +  wrd.count('p'))*3 + 
    (wrd.count('f') + wrd.count('h') +  wrd.count('v') + wrd.count('w') + wrd.count('y'))*4 + wrd.count('k')*5 + 
    wrd.count('j')*8 + wrd.count('q')*8 +  wrd.count('q')*10 +  wrd.count('z')*10 +
    wrd.count('а') + wrd.count('в') + wrd.count('е') + wrd.count('и') + wrd.count('н') + wrd.count('о') + 
    wrd.count('р') +  wrd.count('с') + wrd.count('т') + 
    (wrd.count('д') +  wrd.count('к') + wrd.count('л') + wrd.count('м') + wrd.count('п') + wrd.count('у'))*2 +
    (wrd.count('б') +  wrd.count('г') + wrd.count('ё') + wrd.count('ь') + wrd.count('я'))*3 +
    wrd.count('й')*4 + wrd.count('ы')*4 + 
    (wrd.count('ж') +  wrd.count('з') + wrd.count('х') + wrd.count('ц') + wrd.count('ч'))*5 +
    (wrd.count('ш') + wrd.count('э') +  wrd.count('ю'))*8 + 
    (wrd.count('ф') + wrd.count('щ') +  wrd.count('ъ'))*10)
    
# for i in range (len(wrd)):
    # print(wrd[i])
    # if wrd[i] == 'd' or 'g':
    #     print(wrd[i])
    #     count += 2
#     # elif =

print(count)
