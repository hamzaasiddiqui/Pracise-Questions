#include <iostream>

using namespace std;

int findSubString(string str, string substr) {
    int index = -1;
    bool found = false;

    int j = 0;

    for (int i = 0; i < str.length(); i++) {
        if (substr[j] == str[i]) {
            index = i;
            found = true;
            cout << i;
        }

        cout << found;

        j++;

        if (found) {
            if (substr[j] != str[i+1] && j < substr.length())
                found = false;
        }
    }

    if (found)
        return index;
    else
        return -1;
}

int main () {
    string str, substr;
    int index;

    cout << "Enter a string: ";
    cin >> str;
    cout << "Enter a substring: ";
    cin >> substr;

    index = findSubString(str, substr);

    if (index > -1)
        cout << "\nSubstring found at index " << index << "!\n";
    else
        cout << "\nSubstring not found!\n";

    return 0;
}