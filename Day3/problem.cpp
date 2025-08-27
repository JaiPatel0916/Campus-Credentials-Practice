#include<iostream>
using namespace std;

class Ex{
public:
    int a, b;
    void acp(int x, int y)
    {
        a = x;
        b = y;
    };

    void cal(Ex e1){
        a = e1.a + a;
        b = e1.b + b;
    };

    void dsp(){
        cout << a << "\t" << b;
    }
};

int main(){
    Ex e1, e2;
    e1.acp(3, 4);
    e2.acp(10, 20);
    e2.cal(e1);
    e2.dsp();
}