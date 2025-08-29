#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node *next;

    Node(int d )//constructor
    {
        data = d;
        next = NULL;
    }
};


int main(){
    Node *head;
    head = new Node(5);
    head->next = new Node(10);
    head->next->next = new Node(15);

    cout << head->data << "-->" << head->next->data << "-->" << head->next->next->data;
}