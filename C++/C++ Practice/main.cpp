#include <iostream>
#include <string>
#include <array>
#include <windows.h>

using namespace std;

int clear_console() {
    cin.clear();
    cin.ignore(1000, '\n');
    return 0;
}

int main() {

    int input_1, input_2;
    cout << "Enter a number : ";
    cin >> input_1;
    clear_console();
    cout << "Enter another number : ";
    cin >> input_2;
    if (input_1 > input_2) {
        cout << input_1 << " is greater than " << input_2 << endl;
    }
    else {
        cout << input_1 << " is smaller than " << input_2 << endl;
    }
    system("Pause");

    cout << "Array Stuff" << endl;

    array<int, 5> array_1 = {1, 2, 3, 4, 5};

    cout << array_1[1] << endl;
    cout << array_1.size();















    return 0;
}