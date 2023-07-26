// 팩토리얼

#include <iostream>
using namespace std;

int main(){
    int a = 0;;
    int b = 1;
    while (-1 < a <= 12) cin >> a;
    while (a--){
        b = b * a;
    }
    cout << b;
}