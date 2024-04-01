// FIND IF A GIVEN STRING IS A PALINDROME OR NOT

#include <iostream>

using namespace std;

int main () {
    bool flag = true;

    string str;

    cout << "Enter a string: ";
    cin >> str;

    int i, j = str.length() - 1;

    for (i = 0; i < str.length(); i++) {
        // cout << str[i] << " | " << str[j] << "\n"; 

        if (str[i] != str[j])
            flag = false;

        j--;
    }

    if (flag)
        cout << "Palindrome!\n";
    else
        cout << "Not a palindrome!\n";

    return 0;
}
