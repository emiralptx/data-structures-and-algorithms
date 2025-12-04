#include <iostream>
using namespace std;

int main() {
    double u, v, a;  // initial velocity, final velocity, acceleration
    cout << "Enter initial velocity (u), final velocity (v), and acceleration (a): ";
    cin >> u >> v >> a;
    if (a == 0) {
        cout << "Acceleration cannot be zero." << endl;
        return 1;
    }
    double s = (v * v - u * u) / (2 * a);  // calculate distance
    cout << "The distance traveled is: " << s << endl;
    return 0;
}