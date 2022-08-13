def selection_sort(arr: list) -> list:
    # 依次将最小的数交换到序列前面
    length = len(arr)
    for i in range(length-1):
        minIdx = i # 最小数的索引
        for j in range(i, length):
            if arr[j] < arr[minIdx]:
                minIdx = j
        # 若最小值不是 arr[i] 则交换
        if i != minIdx:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr


if __name__ == "__main__":
    from datetime import datetime
    import random


    # nums = [11, 31, 23, 65, 75, 57, 98, 23, 76]
    length = 10000
    nums = [random.randint(0, 1001) for _ in range(length)]

    begin = datetime.now()
    print(selection_sort(nums))
    end = datetime.now()
    delta = end - begin

    print(f"[time cost] select sort: {delta}")
    # [time cost] select sort: 0:00:10.091405