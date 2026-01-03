num_dict = {0: "zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}
phone_num_str = input("Phone number: ")

res = ""
for num in phone_num_str:
    res += (num_dict[int(num)] + " ")
print(res)