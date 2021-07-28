#include <iostream>
#include <string>
#include <windows.h>
using namespace std;

int clear_console() {
    cin.clear();
    cin.ignore(10000, '\n');
    return 0;
}
float calculate(char operator_cal, float num1, float num2) {
    float result;
    if (operator_cal == '1') {
        result = num1 + num2;
    }
    else if (operator_cal == '2') {
        result = num1 - num2;
    }
    else if (operator_cal == '3') {
        result = num1 * num2;
    }
    else if (operator_cal == '4') {
        result = num1 / num2;
    }
    else {
        result = 1.2;
    }
    return result;
}

int main() {
    system("Color 02");
    int num1, num2, num3;
    float cal_1, cal_2;
    char operator_cal_main;
    cout << "Simple Calculator -----------" << endl;
    cout << "\n\nEnter a number: ";
    cin >> cal_1;
    clear_console();
    cout << "\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide" << endl;
    cout << "\nSelect: ";
    cin >> operator_cal_main;
    clear_console();
    cout << "Enter another number: ";
    cin >> cal_2;
    if (calculate(operator_cal_main, cal_1, cal_2) == 1.2) {
        cout << "Invalid Inputs!" << endl;
    }
    else {
        cout << "Your result: " << calculate(operator_cal_main, cal_1, cal_2) << endl;
    }
    system("pause");
    return 0;
}