#include <iostream>
using namespace std;
 
// Driver code
int main()
{
    int len;
    cout<<"enter length of your traingle"<<endl;
    cin>>len;

    for(int row=1;row<=len;row++)
    {
        for(int col=1;col<=len;col++)
        {
            if(col<=row)                    //            if(row<=col)  if you draw but oppiste
            {
                cout<<"*";
            }
        }
        cout<<endl;
    }





        return 0;
}