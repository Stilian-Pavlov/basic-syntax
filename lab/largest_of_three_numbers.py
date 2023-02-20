first_num = int(input())
second_num = int(input())
third_num = int(input())

max_num = float('-inf')

if first_num > max_num:
    max_num = first_num
if second_num > max_num:
    max_num = second_num
if third_num > max_num:
    max_num=third_num
print(max_num)
