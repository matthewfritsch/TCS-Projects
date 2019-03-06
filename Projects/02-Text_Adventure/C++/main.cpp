
#include <iostream>
using namespace std;
int main(){
    cout << "You wake up in a forest, with no other signs of human life in sight. You don't remember arriving here, and do not recognize where you are." << endl;
    cout << "You're right on top of a trail, which leads three different ways that you must choose from:" << endl;
    cout << "1. Enter the nearby cave" << endl;
    cout << "2. Follow the dirt trail over a hill" << endl;
    cout << "3. Walk deeper into the forest." << endl;
    string choice;
    cout << "Type choice here (1,2,3): ";
    cin >> choice;

    while(!(choice == "1" || choice == "2" || choice == "3")){
        cout << "That is not a choice, please try 1, 2, or 3: ";
        cin >> choice;
    }

    if (choice == "1"){
        cout << "You enter the cave, to find a bear is comfortably laying down, its head on its hands." << endl;
        cout << "Instinctually, you choose to:" << endl;
        cout << "1. Attack the bear" << endl;
        cout << "2. Sneak past the bear" << endl;
        cout << "3. Try to befriend the bear" << endl;
        cout << "Please type the number for your choice: " << endl;
        cin >> choice;

        while(!(choice == "1" || choice == "2" || choice == "3")){
            cout << "That is not a choice, please try 1, 2, or 3: ";
            cin >> choice;
        }

        if (choice == "1"){
            cout << "What were you thinking? You can't fight a bear! You were eaten!" << endl;
        }
        else if(choice == "2"){
            cout << "The bear is definitely not asleep, it sees you tiptoeing around, gets up, and attacks! You were eaten!" << endl;

        }
        else if(choice == "3"){
            cout << "The bear, eerily enough, seems quite docile. He starts walking out of the cave with you, and directs you all the way back home!" << endl;

        }
    }
    else if(choice == "2"){
        cout << "You follow the dirt trail, which leads you over top a small yet, steep hill. Behind the hill is a horse, which appears to be waiting for you." << endl;
        cout << "Instinctually, you choose to:" << endl;
        cout << "1. Feed the horse" << endl;
        cout << "2. Ride the horse" << endl;
        cout << "3. Leave the hill" << endl;
        cout << "Please type the number for your choice: " << endl;
        cin >> choice;
        while(!(choice == "1" || choice == "2" || choice == "3")){
            cout << "That is not a choice, please try 1, 2, or 3: ";
            cin >> choice;
        }

        if (choice == "1"){
            cout << "The horse was not waiting to be fed, so it gets spooked and kicks you! You're knocked out!" << endl;

        }
        else if(choice == "2"){
            cout << "The horse was waiting for you to hop on, and as you did, it ran you straight to your home!" << endl;

        }
        else if(choice == "3"){
            cout << "You leave the hill and, along the way, lose track of where you are. You get so lost that you never seem to make it out of the forest." << endl;

        }
    }
    else if(choice == "3"){
        cout << "You walk deeper into the forest, and see some people who are all around a bonfire, staring right into it." << endl;
        cout << "Instinctually, you choose to:" << endl;
        cout << "1. Attack the people" << endl;
        cout << "2. Talk to the people" << endl;
        cout << "3. Run away from the people" << endl;
        cout << "Please type the number for your choice: " << endl;
        cin >> choice;
        while(!(choice == "1" || choice == "2" || choice == "3")){
            cout << "That is not a choice, please try 1, 2, or 3: ";
            cin >> choice;
        }
        if (choice == "1"){
            cout << "There are so many people here, and they all attack you right back at the same time. You fall unconscious!" << endl;

        }
        else if(choice == "2"){
            cout << "As a person sees you approaching, they all begin screaming and chasing you. They were too fast, and you fall unconscious!" << endl;

        }
        else if(choice == "3"){
            cout << "You understood that these people were kind of scary, and when you begin running away you start to recognize where you are! You make it out of the forest back to your home!" << endl;
  
        }
    }

    return 0;
}