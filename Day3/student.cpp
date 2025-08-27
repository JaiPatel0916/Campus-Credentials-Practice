#include<iostream>
using namespace std;
class Student
{
 public:
     int roll;
     string name;
     void acceptData(int roll , string name){
         this->roll = roll;
         this->name = name;
         showData();
     }
     void showData(){
         cout << roll;
         cout << name;
     }
};


int main(){
    Student s1, s2;

    s1.acceptData(5, "Jai");
}