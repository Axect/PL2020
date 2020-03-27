#include <iostream>

using namespace std;

int add(int a, int b);
double add(double a, double b);
double add(double a, int b);

int main() {
    cout << add(1, 2) << endl;
    cout << add(1.0, 2.0) << endl;
    cout << add(1.0, 2) << endl;
}

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a - b;
}

double add(double a, int b) {
    return a * double(b);
}
