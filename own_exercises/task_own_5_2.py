# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

address = input('Введите IP-сеть в формате IP/Mask: ')

ip = address.split("/")[0]
mask = address.split("/")[1]

octet_a = int(ip.split(".")[0])
octet_b = int(ip.split(".")[1])
octet_c = int(ip.split(".")[2])
octet_d = int(ip.split(".")[3])

ip_x = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
# ip_b = "\n{:08b}  {:08b}  {:08b}  {:08b}"

# mask_bin = "1" * int(mask) + "0" * (32 - int(mask))

# mask_template = '''
# Mask:

# '''

print(ip_x.format(octet_a, octet_b, octet_c, octet_d),
      "\nMask:\n",
        mask)
      # ip_b.format(int(octet_a), int(octet_b), int(octet_c), int(octet_d))) 
