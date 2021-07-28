#include <iostream>
#include <string>
using namespace std;

int main() {
    float input;
    float input2;
    string str2;
    string op;
    cout << "Enter number: ";
    cin >> input;
    cout << "Enter another number: ";
    cin >> input2;
    cout << "Operator: ";
    cin >> op;
    if (op == "+") {
        cout << "Your Result: " << input + input2 << endl;
    }
    else if (op == "-") {
        cout << "Your Result: " << input - input2 << endl;
    }
    else if (op == "*") {
        cout << "Your Result: " << input * input2 << endl;
    }
    else if (op == "/") {
        cout << "Your Result: " << input / input2 << endl;
    }
    else {
        cout << "Invalid Operator! Operator " << '\"' + op + '\"' << " is not a valid mathematical operator!";
    }
    cout << "Enter to exit" << endl;
    cin >> str2;
    return 0;
}
