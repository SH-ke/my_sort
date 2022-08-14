#include<stdio.h>

void swap(int* x, int* y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(int arr[], int length)
{
    int i, j, temp;

    // 排序必须有2个以上的元素，因此i = 1开始
    for(i = 1; i < length - 1; i++)
    {
        for(j = 0; j < length-i; j++)
        {
            // 判断是否为升序，否则交换
            if (arr[j] > arr[j+1]) swap(arr+j, arr+j+1);
        }
    }
}

void bubble_sort_flag(int arr[], int length)
{
    int i, j, flag = 0;

    for (i = 1; i < length; i++)
    {
        for (j = 0; j < length-i; j++)
        {
            // 判断是否为升序，否则交换
            if (arr[j] > arr[j+1])
            {
                swap(arr+j, arr+j+1);
                flag = 1;
            }
        }
        // 若没有发生交换，说明排序已经完成，直接跳出循环
        if (!flag) break;
    }
}

int random_arr(int low, int up, int length)
{
    // 生成范围在[low, up]之间的，长度为 length 的随机数
    int* arr;

    return arr;
}

void main()
{
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int length = (int) sizeof(arr) / sizeof(*arr);
    // bubble_sort(arr, length);
    bubble_sort_flag(arr, length);
    // 添加计时函数，计算各种排序方法的优劣

    int i;
    for (i = 0; i < length; i++)
    {
        printf("%d, ", arr[i]);
    }
}