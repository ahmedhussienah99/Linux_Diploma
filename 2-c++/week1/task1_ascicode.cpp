#include <iostream>
using namespace std;
int main()
{
    cout<<"ASCII TABLE"<<endl;
    cout << "|" << "char" << "       |" << "ASCII"<<"|"<< endl;
    cout << "--------------------------" << endl;
    for(int i=0;i<=127;i++)
    {
            cout << "|" << i << "       |   " << char(i)<<"|"<< endl;
    }
    return 0;
}