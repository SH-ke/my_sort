def shell_sort_3(arr: list) -> list:
    import math

    length = len(arr)
    gap = 1 # 每隔 gap 的元素为一组
    while gap < length/3:
        # 保证初次分组时能够三个元素一组，还有富裕
        gap = gap * 3 + 1 # 最小够用的 gap 值
    while gap > 0:
        for i in range(gap, length):
            current = arr[i]
            j = i - gap
            # 对每个分组进行插入排序；判断是否升序，否则交换
            while j >= 0 and arr[j] > current:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = current
        gap = math.floor(gap/3)
    return arr

def shell_sort_2(arr: list) -> list:
    import math

    length = len(arr)
    gap = math.floor(length/2) # 每隔 gap 的元素为一组
    while gap > 0:
        for i in range(gap, length):
            current = arr[i]
            j = i - gap
            # 对每个分组进行插入排序；判断是否升序，否则交换
            while j >= 0 and arr[j] > current:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = current
        gap = math.floor(gap/2)
    return arr


if __name__ == "__main__":
    import random
    from datetime import datetime


    length, low, up = 100000, 0, 1001 # 生成随机序列，长度为 length 范围为 [low, up)
    nums = [random.randint(low, up) for _ in range(length)]

    begin = datetime.now()
    print(shell_sort_2(nums.copy()))
    end = datetime.now()
    delta_2 = end - begin

    begin = datetime.now()
    print(shell_sort_3(nums.copy()))
    end = datetime.now()
    delta_3 = end - begin

    print(f"[time cost] select sort 2: {delta_2} select sort 3: {delta_3} ")
    # [time cost 1e5] select sort 2: 0:00:05.915345 select sort 3: 0:00:06.464963