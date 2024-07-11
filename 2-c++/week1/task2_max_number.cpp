#include <iostream>
#include <algorithm>
using namespace std;

int maxNumber(int a, int b, int c) ;

int main() {

    int n1;
    int n2;
    int n3;
    int result1;
    int result2;
    //getline(cin, s); 
    cout<<"enter your three number :"<<endl;
    cin>>n1;
    cin>>n2;
    cin>>n3;
    result1=max(n1,max(n2,n3));
    result2=maxNumber(n1,n2,n3);
    cout<< "the max number is : "<<result1<<" another method : " <<result2<<endl;


        return 0;
}


int maxNumber(int a, int b, int c) 
{
    int max = a;
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    return max;
}