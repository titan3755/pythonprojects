#include <iostream>
#include <string>

// Namespaces

using namespace std;

// Prototypes

int clear();

// Temperature Class Declaration

class Temperature {
public:
	float ctof(float celsius) {
		float result = (celsius * 9 / 5) + 32;
		return result;
	}
	float ftoc(float fahrenheit) {
		float result = (fahrenheit - 32) * 5 / 9;
		return result;
	}
};

// Main Function

int main() {
	float temp;
	string cfrom, cto;
	
	cout << "Enter a temperature for conversion (Numeric values only): ";
	cin >> temp; clear();
	Temperature tempobj;
	cout << 
R"(
Convert from ---         Convert to ---

1. Celsius               1. Celsius
2. Fahrenheit		 2. Fahrenheit

)";
	cout << "Convert From >> ";
	cin >> cfrom; clear();
	cout << "Convert To >> ";
	cin >> cto; clear();

	if (cfrom == "1" and cto == "2") {
		cout << "\n" << tempobj.ctof(temp) << endl;
	}
	else if (cfrom == "2" and cto == "1") {
		cout << "\n" << tempobj.ftoc(temp) << endl;
	}
	else {
		cout << "\n" << "Invalid Inputs!" << endl;
	}

	system("pause");

	return 0;
}

// Functions

int clear() {
	cin.clear();
	cin.ignore(10000, '\n');
	return 0;
}

