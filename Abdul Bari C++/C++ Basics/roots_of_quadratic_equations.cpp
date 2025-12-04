#include   <iostream>
using namespace std;

int main() {
    double a, b, c, r1, r2;
    cout << "Enter coefficients a, b and c of the quadratic equation (ax^2 + bx + c = 0): ";
    cin >> a >> b >> c;
    
    r1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a);
    r2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a);
    cout << "Roots of the quadratic equation are: " << r1 << " and " << r2 << endl;
    return 0;
}