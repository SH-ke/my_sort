#include<stdio.h>

void swap();

void insert_sort_while(int arr[], int len)
{
    int i;
    for (i = 1; i < len; i++)
    {
        int preIdx = i - 1; // 与current比较的元素
        int current = arr[i];
        while (preIdx >= 0 && arr[preIdx] > current)
        {
            arr[preIdx + 1] = arr[preIdx];
            preIdx --;
        }
        arr[preIdx + 1] = current;        
    }
}

void insert_sort_for(int arr[], int len)
{
    int i, j;
    for (i = 1; i < len; i++)
    {
        for (j = i; j >=0; j--)
        {
            // 判断是否升序，否则交换
            if (arr[j-1] > arr[j]) swap(arr+j-1, arr+j);
            else break; // 若为升序，说明 arr[j] 已经插入到了正确的位置
        }
    }
}

void main()
{
    int arr[] = { 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
    int length = (int) sizeof(arr) / sizeof(*arr);
    printf("insert sort [for loop version]\n");
    // insert_sort_while(arr, length);
    insert_sort_for(arr, length);
    
    int i;
    for (i = 0; i < length; i++)
    {
        printf("%d, ", arr[i]);
    }
}