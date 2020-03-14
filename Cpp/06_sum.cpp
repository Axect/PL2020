#include <iostream>

using namespace std;

int main() {
    long s = 0;

    for (long i=0; i<10000000; i++) {
        s += i;
    }

    cout << s << endl;
}
