// 팩토리얼

#include <iostream>
using namespace std;

int factorial(int num){ // 팩토리얼 재귀함수
    if (num > 2) num = factorial (num - 1);
    return num;
}

int main(){
    int num, result = 1; // fac 0 이면 1을 출력하게 된다.
    cin >> num;
    if (num!=0) result = factorial(num);
    cout << result;
}