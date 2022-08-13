def insert_sort_while(arr: list) -> list:
    # 从左到右升序
    for i in range(len(arr)):
        preIdx = i - 1 # current在有序区内的前一个元素的索引
        current = arr[i]
        # 将 current 加入有序区，若左侧元素大于 current 则 current 往左交换一位
        # 实际操作时，空出 current 的位子，比current大的值向右覆盖
        # 最后将 current 的值赋给 preIdx+1 为的元素
        while preIdx >= 0 and arr[preIdx] > current:
            arr[preIdx+1] = arr[preIdx]
            preIdx -= 1
        arr[preIdx+1] = current # 最后依次交换 preIdx -= 1 所以应当是 preIdx+1
    return arr


def insert_sort_for(arr: list) -> list:
    for i in range(len(arr)):
        # arr[i] 加入有序区，依次向左比较
        for j in range(1, i+1)[::-1]:
            # 若左侧大则交换
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else: # arr[i] 已经大于有序区内最大的元素了，不用交换
                break
    return arr


def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr


if __name__ == "__main__":
    import random
    from datetime import datetime


    length = 10000 # 1000以内长度为 length 的序列
    arr = [random.randint(0, 1001) for _ in range(length)]

    begin = datetime.now()
    print(insert_sort_while(arr.copy()))
    end = datetime.now()
    delta_while = end - begin

    begin = datetime.now()
    print(insert_sort_for(arr.copy()))
    end = datetime.now()
    delta_for = end - begin

    print(f"[time cost] insert sort while: {delta_while}, insert sort for {delta_for}")