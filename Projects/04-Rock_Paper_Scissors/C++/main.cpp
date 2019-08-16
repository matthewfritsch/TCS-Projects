#include <iostream>
#include <time.h>
#include <ctime>

using namespace std;
int main(){
    srand(time(NULL));
    cout << "Welcome to Rock, Paper, Scissors! Your opponent is the computer!"<< endl;
    string user;
    cout << "Choose 'rock', 'paper', or 'scissors': ";
    cin >> user;
    int number = (rand()%3) + 1;
    string computer;
    if(number == 1){
        computer = "rock";
    }
    else if(number == 2){
        computer = "paper";
    }
    else{
        computer = "scissors";
    }

    if(user == computer){
        cout << "It was a tie!"<< endl;
    }
    else if(user == "rock"){
        if(computer == "paper"){
            cout << "You lost, CPU chose paper!"<< endl;
        }
        else if(computer == "scissors"){
            cout << "You won, CPU chose scissors!"<< endl;
        }
    }
    else if(user == "paper"){
        if(computer == "scissors"){
            cout << "You lost, CPU chose scissors!"<< endl;
        }
    }
    else if(computer == "rock"){
        cout << "You won, CPU chose rock!"<< endl;
    }
    else if(user == "scissors"){
        if(computer == "rock"){
            cout << "You lost, CPU chose rock!"<< endl;
        }
        else if(computer == "paper"){
            cout << "You won, CPU chose paper!"<< endl;
        }
    }
    else{
        cout << "That was not an option!"<< endl;
    }


    return 0;
}
