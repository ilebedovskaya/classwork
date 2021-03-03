# Задание 1 .Пользователь вводит путь к папке и искомое слово. Программа ищет слово в папке и её подпапках. После
# работы программы формируется отчет с информацией
# о том, где было слово найдено, количество совпадений.
# Добавьте возможность замены или удаления искомого
# слова из файлов.

f = open("task1", mode="r")
lst = f.read()
lst = lst.split("\n")
f.close()


def search_word():
    search_word = input("Введите слово для поиска в файле: ")
    counter = 0
    for i, word in enumerate(lst):
        print(word)
        if word == search_word:
            counter += 1
    if int(str(counter)[:1]) == 2 or int(str(counter)[:1]) == 3 or int(str(counter)[:1]) == 4:
        print("Слово", search_word, "было найдено", counter, "раза")
    elif counter == 0:
        print("Такого слова в файле нет!")
    else:
        print("Слово", search_word, "было найдено", counter, "раз")


def replace_word():
    search_word = input("Введите слово, которое хотите заменить: ")
    replace_word = input("Введите слово, на которое хотите заменить: ")
    counter = 0
    for i, word in enumerate(lst):
        if word == search_word:
            lst[i] = replace_word
            counter += 1
    if counter == 0:
        print("Такого слова нет в файле!")
    else:
        print(lst)


def delete_word():
    delete_word = input("Введите слово, которое хотите удалить: ")
    counter = 0
    print(lst)
    for i, word in enumerate(lst):
        if word == delete_word:
            lst.pop(i)
            counter += 1
    if counter == 0:
        print("Такого слова нет в файле!")
    else:
        print(lst)


search_word()
replace_word()
delete_word()


# Задание 2
# Определить, сколько символов букв содержит файл.
# Скопировать из файла F1 в файл F2 все символы кроме символов-«цифр».
# Определить, сколько раз заданный разделитель встречается в файле.
# Скопировать из файла F1 в файл F2 все символы, заменив символ-«цифру» на символ %.

f = open("F1", mode="r")
lst_t2 = f.read()
f.close()


def count_symbols():
    counter = 0
    for i in enumerate(lst_t2):
        if i[1] != " ":
            counter += 1
    print("Всего", counter, "символов")


def not_copy_digits():
    new_list = []
    for i in enumerate(lst_t2):
        if i[1] != " ":
            if i[1].isdigit():
                pass
            else:
                new_list.append(i[1])
                f = open("F2", mode="w")
                for i in range(len(new_list)):
                    f.write(str(new_list[i]) + "")
                f.close()


def count_sep():
    counter = 0
    for i in enumerate(lst_t2):
        if i[1] == " ":
            counter += 1
    print("Сепаратор встречается", counter, "раз")


def replace_digits():
    new_list = list(lst_t2)
    for i in range(len(new_list)):
        if new_list[i].isdigit():
            new_list[i] = "%"
    f = open("F2", mode="w")
    for i in range(len(new_list)):
        f.write(str(new_list[i]) + "")
    f.close()


count_symbols()
not_copy_digits()
count_sep()
replace_digits()



