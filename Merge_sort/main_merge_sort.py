from random import randint
from tkinter import *


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


def random_variant(event):
    global ent_len, ent_do, ent_ot
    # Lable
    lable_len = Label(fra, text="Укажите размерность генерируемого масива чисел:", fg="#000", bg="#fff")
    lable_len.place(x=10, y=70)
    lable_ot = Label(fra, text="Укажите минимальное число масива:", fg="#000", bg="#fff")
    lable_ot.place(x=10, y=98)
    lable_do = Label(fra, text="Укажите максимальное число масива:", fg="#000", bg="#fff")
    lable_do.place(x=10, y=125)

    # Entry
    ent_len = Entry()
    ent_len.place(x=310, y=70)
    ent_ot = Entry()
    ent_ot.place(x=235, y=98)
    ent_do = Entry()
    ent_do.place(x=235, y=125)

    # Button
    but_merge_sort = Button(fra, height=1, text='Сортировать', font='Arial 10', fg="#fff", bg="#000",
                            borderwidth=0)
    but_merge_sort.place(x=10, y=152)
    but_merge_sort.bind('<Button-1>', sbor_random)


def me_variant(event):
    global ent_len
    # Lable
    lable_len = Label(fra, text="Укажите числа масива через пробел:", fg="#000", bg="#fff")
    lable_len.place(x=10, y=70)

    # Entry
    ent_len = Entry()
    ent_len.place(x=228, y=70, height=20, width=300)

    # Button
    but_merge_sort = Button(fra, height=1, text='Сортировать', font='Arial 10', fg="#fff", bg="#000",
                            borderwidth=0)
    but_merge_sort.place(x=10, y=97)
    but_merge_sort.bind('<Button-1>', sbor_me)


def sbor_me(event):
    A = ent_len.get().split()
    h = 0
    for i in A:
        A[h] = int(i)
        h += 1
    list_merge_sort_r = merge_sort(A)

    # Lable
    lable_list_merge_sort_r = Label(fra, text=A, fg="#000", bg="#fff")
    lable_list_merge_sort_r.place(x=10, y=127)
    lable_len = Label(fra, text=list_merge_sort_r, fg="#000", bg="#fff")
    lable_len.place(x=10, y=153)

    print(A)
    print(list_merge_sort_r)


def sbor_random(event):


    lenn = int(ent_len.get())
    ot = int(ent_ot.get())
    do = int(ent_do.get())
    A = [randint(ot, do) for i in range(lenn)]
    list_merge_sort_r = merge_sort(A)

    # Lable
    lable_list_merge_sort_r = Label(fra, text=A, fg="#000", bg="#fff")
    lable_list_merge_sort_r.place(x=10, y=182)
    lable_list_merge_sort_r = Label(fra, text=list_merge_sort_r, fg="#000", bg="#fff")
    lable_list_merge_sort_r.place(x=10, y=208)

    print(A)
    print(list_merge_sort_r)



# Tk
root = Tk()
root.title('Merge Sort')

# Интерфейс
fra = Frame(root, width=550, height=300, bg='#fff')
fra.pack()

# Label
info = Label(fra, text="Задать свой масив?", fg="#000", bg="#fff")
info.place(x=10, y=10)

# Button
but_yes = Button(fra, height=1, text='Да', font='Arial 10', fg="#fff", bg="#000", borderwidth=0)
but_yes.place(x=10, y=40)
but_yes.bind('<Button-1>', me_variant)

but_no = Button(fra, height=1, text='Нет', font='Arial 10', fg="#fff", bg="#000", borderwidth=0)
but_no.place(x=40, y=40)
but_no.bind('<Button-1>', random_variant)

root.mainloop()
