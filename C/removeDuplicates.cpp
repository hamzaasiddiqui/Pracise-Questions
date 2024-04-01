#include <iostream>

void removeDuplicates(int arr[], int &size) {
    if (size == 0 || size == 1) {
        return;
    }

    int newSize = 1;
    for (int i = 1; i < size; i++) {
        if (arr[i] != arr[newSize - 1]) {
            arr[newSize++] = arr[i];
        }
    }

    size = newSize;
}

int main() {
    int arr[] = {1, 2, 2, 3, 4, 4, 4, 5, 6, 6};
    int size = sizeof(arr) / sizeof(arr[0]);

    removeDuplicates(arr, size);

    for (int i = 0; i < size; i++) {
        std::cout << arr[i] << " ";
    }

    return 0;
}