#include <iostream>
using namespace std;

int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
double divide(int a, int b);

int main(){

    cout << "Welcome to my basic, two number calculator." << endl;

    int number1;
    string op;
    int number2;
    cout << "Type in your first number: ";
    cin >> number1;
    cout << "Type in your op: ";
    cin >> op;
    cout << "Type in your second number: ";
    cin >> number2;

    if(op == "+"){
        cout << add(number1, number2) << endl;
    }
    else if(op == "-"){
        cout << subtract(number1, number2) << endl;
    }
    else if( op == "*"){
        cout << multiply(number1, number2) << endl;
    }
    else if( op == "/"){
        cout << divide(number1, number2) << endl;
    }
    else{
        cout << "That was not an operator we have!" << endl;
    }
    return 0;
}

int add(int a, int b){
    return a+b;
}
int subtract(int a, int b){
    return a-b;
}
int multiply(int a, int b){
    return a*b;
}
double divide(int a, int b){
    return (double)a/(double)b;
}