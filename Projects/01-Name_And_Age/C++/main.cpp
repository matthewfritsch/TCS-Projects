
#include <iostream>
using namespace std;
int main(){
    string name;
    int age;
    cout << "Please enter your name: ";
    cin >> name;
    cout << "Please enter your age: ";
    cin >> age;

    cout << name << " is " << age << " years old "<< endl;

    string name2 = "Peter Parker";
    int age2 = 17;

    cout << name2 << " is " << age2 << " years old "<< endl;

    if(age > age2){
        cout << name << " is older than " << name2 << endl;
    }
    else if(age < age2){
        cout << name << " is younger than " << name2 << endl;
    }
    else{
        cout << name << " is the same age as " << name2 << endl;
    }

    return 0;
}