#include <iostream>
#include <time.h>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

string makeDashes(string w);
string getWord();
char input(char[]);
bool notAlpha(char);
bool usedIn(char[], char);
bool hasDashes(string);
bool goodGuess(char, string, string &);

int main(){
    srand(time(NULL));
    string word = getWord();
    string dashes = makeDashes(word);
    int chances = 6;
    int curLocUsed = 0;
    char used[] = "";
    while(chances > 0 && hasDashes(dashes)){
        cout << dashes << endl;
        printf("You have %d guesses left\n", chances);
        char guess = input(used);
        used[curLocUsed++] = guess;
        if(!goodGuess(guess, word, dashes)){
            chances--;
        }
    }

    if(hasDashes(dashes))
        cout << "You lose." << endl;
    else
        cout << "You win." << endl;
    
    free(used);
    return 0;
}

bool goodGuess(char c, string w, string &d){
    bool toRet = false;
    for(int x = 0; x < w.size(); x++){
        if(w[x] == c){
            d = d.substr(0,x*2) + c + d.substr(x*2+1);
            toRet = true;
        }
    }
    return toRet;
}

bool hasDashes(string s){
    for(char c : s){
        if(c == '_'){
            return true;
        }
    }
    return false;
}

string makeDashes(string w){
    string dashes = "";
    for(char c : w){
        dashes+="_ ";
    }
    return dashes;
}
string getWord(){
    ifstream i("myWords.txt");
    int rando = rand()%379900;
    string s;
    while(rando > 0){
        rando--;
        i>>s;
    }
    return s;
}
char input(char used[]){
    cout << "Enter a letter: ";
    string s;
    cin >> s;
    while(notAlpha(s[0]) || usedIn(used, s[0])){
        cout << "You need to type in a working letter, try again: ";
        cin >> s;
    }
    return s[0];
}

bool notAlpha(char c){
    return !(c>=97 && c <= 122);
}

bool usedIn(char used[], char check){
    for(int x = 0; x < sizeof(used)/sizeof(char); x++){
        if(used[x] == check){
            return true;
        }
    }
    return false;
}