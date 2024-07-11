//task7_change_binary_to_decmial.cpp

#include <iostream>
#include <bitset>
#include <string>
using namespace std;
void decToBinary(int n)
{
    int binaryNum[32];

    int i = 0;
    while (n > 0) {
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }

    for (int j = i - 1; j >= 0; j--)
    {
        cout << binaryNum[j];
    }
    cout<<endl;

}
int main() {

    string s_binary;
    int decimal_num;
    cout<<"enter your binary number : ";
    cin>>s_binary;
    bitset<8> bits(s_binary);
    cout << "your Decimal number is : "<<bits.to_ulong() << endl;
    cout<<"enter your decimal number :";
    cin>>decimal_num;
    cout<<"your binary number is : ";
    decToBinary(decimal_num);









     return 0;
}