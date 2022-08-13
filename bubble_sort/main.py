def bubble_sort(array: list) -> list:
    length = len(array)
    for i in range(1, length):
        for j in range(length-i):
            # 判断 是否升序，否则调换
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def bubble_sort_flag(array: list) -> list:
    length = len(array)
    flag: bool = False
    for i in range(1, length):
        for j in range(length-i):
            # 判断 是否升序，否则调换
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        # 判断标志位是否为false，
        # 如果为false，说明后面的元素已经有序，就直接return
        if not flag:
            break

    return array


if __name__ == "__main__":
    from datetime import datetime
    import random


    # nums = [11, 31, 23, 65, 75, 57, 98, 23, 76]
    length = 40
    nums = [random.randint(0, 1001) for _ in range(length)]

    begin = datetime.now()
    print(bubble_sort(nums.copy()))
    end = datetime.now()
    delta_no_flag = end - begin

    begin = datetime.now()
    print(bubble_sort_flag(nums.copy()))
    end = datetime.now()
    delta_flag = end - begin

    print(f"[time cost] bubble sort: {delta_no_flag}, bubble sort with flag: {delta_flag}")
    # 序列长度小的情况flag更优
    # [time cost] bubble sort: 0:00:00.000999, bubble sort with flag: 0:00:00.000997
    # 序列长度巨大的情况不适用flag更节省时间
    # [time cost] bubble sort: 0:00:00.795229, bubble sort with flag: 0:00:00.954324
    # 当序列长度为1e4时 改进效果明显