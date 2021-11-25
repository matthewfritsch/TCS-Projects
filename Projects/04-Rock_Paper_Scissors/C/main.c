#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// takes in an int as the Upper Bound, Exclusive of that value.
int get_random(int ube){
    return rand()%ube;
}

int main(int argc, char**argv){

    srand(time(NULL));
    
    printf("Welcome to Rock, Paper, Scissors! Your opponent is the computer!\n");
    char user[10];
    printf("Choose 'rock', 'paper', or 'scissors': ");
    scanf("%s", user);
    int number = get_random(3)+1;
    char computer[10];
    if(number == 1){
        strcpy(computer, "rock");
    }
    else if(number == 2){
        strcpy(computer, "paper");
    }
    else{
        strcpy(computer, "scissors");
    }

    if(strcmp(user,computer) == 0){
        printf("It was a tie!\n");
    }
    else if(strcmp(user, "rock") == 0){
        if(strcmp(computer, "paper") == 0){
            printf("You lost, CPU chose paper!\n");
        }
        else if(strcmp(computer, "scissors") == 0){
            printf("You won, CPU chose scissors!\n");
        }
    }
    else if(strcmp(user, "paper") == 0){
        if(strcmp(computer, "scissors") == 0){
            printf("You lost, CPU chose scissors!\n");
        }
    }
    else if(strcmp(computer, "rock") == 0){
        printf("You won, CPU chose rock!\n");
    }
    else if(strcmp(user, "scissors") == 0){
        if(strcmp(computer, "rock") == 0){
            printf("You lost, CPU chose rock!\n");
        }
        else if(strcmp(computer, "paper") == 0){
            printf("You won, CPU chose paper!\n");
        }
    }
    else{
        printf("That was not an option!\n");
    }

    return 0;
}