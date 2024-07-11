#include <iostream>
using namespace std;
int is_vowel(char letter);


int main() {

    char c;
    int res;
    cout<<"enter your character"<<endl;
    cin>>c;

        res=is_vowel(c);
        if(res==1)
        {
            cout<<"the character is vowel"<<endl;
        }
        else
        {
        cout<<"the character is not vowel"<<endl;
        }

      return 0;
}



int is_vowel(char letter) {
  
    int result=0;
    if      (letter=='a'){   result=1; return result;     }
    else if (letter=='e'){   result=1; return result;     }
    else if (letter=='i'){   result=1; return result;     }
    else if (letter=='o'){   result=1; return result;     }
    else if (letter=='u'){   result=1; return result;     }
    else if (letter=='A'){   result=1; return result;     }
    else if (letter=='E'){   result=1; return result;     }
    else if (letter=='I'){   result=1; return result;     }
    else if (letter=='O'){   result=1; return result;     }
    else if (letter=='U'){   result=1; return result;     }
    else{ return 0;}

}