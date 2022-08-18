#include<stdio.h>


void shell_sort_2(int arr[], int len)
{
    int i, j, gap = len / 2, current;

    while (gap > 0)
    {
        for (i = gap; i < len; i++)
        {
            current = arr[i];
            j = i - gap;
            // 对于单个分组执行插入排序；判断是否升序，否则调换
            while (j >= 0 && arr[j] > current)
            {
                arr[j+gap] = arr[j];
                j -= gap;
            }
            arr[j+gap] = current;
        }
        gap /= 2;
    }
}

void shell_sort(int arr[], int len) {
    // for 语句性能优于 while 语句？
    // >>1 操作优于 /=2 ？
    int gap, i, j;
    int temp;
    for (gap = len >> 1; gap > 0; gap >>= 1)
        for (i = gap; i < len; i++) {
            temp = arr[i];
            for (j = i - gap; j >= 0 && arr[j] > temp; j -= gap)
                    arr[j + gap] = arr[j];
            arr[j + gap] = temp;
        }
}

void shell_sort_3(int arr[], int len)
{
    int i, j, gap, current;
    while (gap < len/3) gap = gap * 3 + 1;
    while (gap > 0)
    {
        for (i = gap; i < len; i++)
        {
            current = arr[i];
            j = i - gap;
            // 对每个分组进行插入排序；判断是否升序，否则调换
            while (j >= 0 && arr[j] > current)
            {
                arr[j+gap] = arr[j];
                j -= gap;
            }
            arr[j+gap] = current;
        }
        gap /= 3;
    }
}

void main()
{
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int len = (int) sizeof(arr) / sizeof(*arr);

    printf("shell sort 2\n");
    shell_sort_2(arr, len);
    int i;
    for(i = 0; i < len; i++) printf("%d, ", arr[i]);

    // printf("shell sort 3\n");
    // shell_sort_3(arr, len);
    // for(i = 0; i < len; i++) printf("%d, ", arr[i]);
}