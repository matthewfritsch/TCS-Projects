
#include <iostream>

int main(){
    std::string name;
    int age;
    std::cout << "Please enter your name: ";
    std::cin >> name;
    std::cout << "Please enter your age: ";
    std::cin >> age;

    std::cout << name << " is " << age << " years old "<< std::endl;

    std::string name2 = "Peter Parker";
    int age2 = 17;

    std::cout << name2 << " is " << age2 << " years old "<< std::endl;

    if(age > age2){
        std::cout << name << " is older than " << name2 << std::endl;
    }
    else if(age < age2){
        std::cout << name << " is younger than " << name2 << std::endl;
    }
    else{
        std::cout << name << " is the same age as " << name2 << std::endl;
    }
    return 0;
}