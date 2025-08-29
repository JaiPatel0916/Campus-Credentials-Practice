#include<iostream>
using namespace std;


class Node{
    public:
        int data;
        Node *next;

        Node(int d){
            data = d;
            next = NULL;
        }
};

int main(){
    Node *head;

    head = new Node(5);

    head->next = new Node(10);
    head->next->next = new Node(15);
    head->next->next->next = new Node(20);


    while(head!=NULL){
        cout << head->data << "-->";
        head = head->next;
    }
}