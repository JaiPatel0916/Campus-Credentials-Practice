#include <iostream>
#include <string>
using namespace std;
class Student {
private:
    int roll, m1, m2, m3, total;
    float per;
public:
    Student(int r, int m1, int m2, int m3) {
        roll = r;
        m1 = m1;
        m2 = m2;
        m3 = m3;
        total = m1 + m2 + m3;
    }
    void cal() {
        per = total/3*100;
    }
    void dsp() {
        if(per>35){
            cout<<"Pass"<<endl;
        }
        else{
            cout<<"Fail"<<endl;
        }
    }
};
int main(){
    Student s1(1,70,60,90), s2(2,20,36,35);
    s1.cal();
    s2.cal();
    s1.dsp();
    s2.dsp();
    return 0;
}