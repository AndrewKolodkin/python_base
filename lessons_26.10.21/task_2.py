list_number = []
new_list = []
for i in range(1, 1001):
    if i % 2 != 0:
        list_number = [i ** 3]
        for idx in list_number:
            if (((idx % 10 ** 9) // 10 ** 8) + ((idx % 10 ** 8) // 10 ** 7) + ((idx % 10 ** 7) // 10 ** 6) + (
                    (idx % 10 ** 6) // 10 ** 5) + ((idx % 10 ** 5) // 10 ** 4) + ((idx % 10 ** 4) // 10 ** 3) + (
                        (idx % 10 ** 3) // 10 ** 2) + ((idx % 10 ** 2) // 10) + (idx % 10)) % 7 == 0:
                new_list = sum([idx])
                list_number = [idx + 17]
                for idx_1 in list_number:
                    if (((idx_1 % 10 ** 9) // 10 ** 8) + ((idx_1 % 10 ** 8) // 10 ** 7) + (
                        (idx_1 % 10 ** 7) // 10 ** 6) + (
                            (idx_1 % 10 ** 6) // 10 ** 5) + ((idx_1 % 10 ** 5) // 10 ** 4) + (
                            (idx_1 % 10 ** 4) // 10 ** 3) + (
                            (idx_1 % 10 ** 3) // 10 ** 2) + ((idx_1 % 10 ** 2) // 10) + (
                            idx_1 % 10)) % 7 == 0:
                        new_list = sum([idx_1])
print(new_list)