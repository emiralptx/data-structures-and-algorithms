#include <iostream>
using namespace std;

int main() {
    int n, sum;
    cout << "Enter a positive integer n: ";
    cin >> n;
    
    sum = n * (n + 1) / 2;
    cout << "The sum of the first " << n << " natural numbers is: " << sum << endl;
    return 0;
}