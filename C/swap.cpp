// Swap two without using a third variable

#include <iostream>

using namespace std;

int main () {
    int a, b;

    cout << "\nEnter first no: ";
    cin >> a;

    cout << "\nEnter second no: ";
    cin >> b;

    cout << "\nBEFORE SWAP:\n";
    cout << "a = " << a << ", b = " << b << "\n";

    a = a + b;
    b = a - b;
    a = a - b;

    cout << "\nAFTER SWAP:\n";
    cout << "a = " << a << ", b = " << b << "\n";

    return 0;
}