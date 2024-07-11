#include <iostream>
using namespace std;

int sum_Digits(int num) ;


int main() {


    int result;
    int input;

    cout<<"enter your integer : ";
    cin>> input;
    result=sum_Digits(input);
    cout<<"the sum of digits is : "<<result<<endl;


        return 0;
}



int sum_Digits(int num) {
    int sum = 0;
    while (num != 0) {
        sum =sum +(num % 10);
        num /= 10;
    }
    return sum;
}