def dict_sort(dict_input):
    return sorted(dict_input.items(), key=lambda item: item[1])


def main():
    f = open("input.txt", "r")
    file_input = f.read()
    input_arr = file_input.replace("\n", " ").split(" ")

    hehe_dict = {}

    for i in input_arr:
        if i not in hehe_dict:
            hehe_dict[i] = 1
        else:
            hehe_dict[i] += 1

    res = dict_sort(hehe_dict)
    most_common = res[-10:]
    least_common = res[:10]

    print(most_common)
    print(least_common)


if __name__ == '__main__':
    main()
