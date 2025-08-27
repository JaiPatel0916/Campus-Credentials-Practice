#include<iostream>
using namespace std;
class Ex
{
    public:
    int a;
    int b;
    void acceptData(int x,int y)
    {
        a=x;   
        b=y;
    }
    void cal(Ex e1,Ex e2)
    {
        a=e1.a+e2.a;
        b=e1.b+e2.b;
    }
    void dsp()
    {
     cout << a << "\t" << b;
    }
};
int main()
{
    Ex e1,e2,e3;
    e1.acceptData(5,10);
    e2.acceptData(2,4);
  
    e3.cal(e1,e2);
    e3.dsp();
}