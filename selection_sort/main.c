#include<stdio.h>

void swap();

void selection_sort(int arr[], int len)
{
    int i, j;
    for (i = 0; i < len - 1; i++)
    {
        int minIdx = i;
        // 使用 for loop 找到[i, len-1]中最小元素的索引
        for (j = i; j < len; j++)
            if (arr[j] < arr[minIdx]) swap(arr+j, arr+minIdx);
    }
}

void main()
{
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int length = (int) sizeof(arr) / sizeof(*arr);
    printf("selection sort\n");
    selection_sort_for(arr, length);
    
    int i;
    for (i = 0; i < length; i++)
    {
        printf("%d, ", arr[i]);
    }
}