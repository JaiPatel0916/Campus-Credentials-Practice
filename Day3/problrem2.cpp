// #include<iostream>
// using namespace std;
// class Ex
// {
//     public:
//     int a;
//     int b;
//     void acceptData(int x,int y)
//     {
//         a=x;   
//         b=y;
//     }
//     void cal(Ex e1,Ex e2)
//     {
//         a=e1.a+e2.a;
//         b=e1.b+e2.b;
//     }
//     void dsp()
//     {
//      cout << a << "\t" << b;
//     }
// };
// int main()
// {
//     Ex e1,e2,e3;
//     e1.acceptData(5,10);
//     e2.acceptData(2,4);
  
//     e3.cal(e1,e2);
//     e3.dsp();
// }



//Using Constructor
#include <iostream>
#include <string>
using namespace std;
class Ex
{
public:
    int a, b;
    // void acp(int x, int y)
    // {
    //     a = x;
    //     b = y;
    // }
    Ex(int x, int y)
    {
        a = x;
        b = y;
    }
    void cal(Ex e1)
    {
        a = e1.a + a;
        b = e1.b + b;
    }
    void dsp()
    {
        cout << "a = " << a << endl;
        cout << "b = " << b << endl;
    }
};
int main()
{
    // Ex E1, E2, E3;
    // E1.acp(3, 4);
    // E2.acp(10, 20);
    // E3.acp(7, 14);
    Ex e1(3,4), e2(10,20);
    e2.cal(e1);
    e2.dsp();
}