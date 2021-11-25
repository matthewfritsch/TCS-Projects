#include <stdio.h>
#include <string.h>

int add(int a, int b);
int sub(int a, int b);
int mul(int a, int b);
int div(int a, int b);

int main(int argc, char** argv){

    printf("Welcome to my basic, two number calculator.\n");

    int number1;
    char op[2];
    int number2;
    printf("Type in your first number: ");
    scanf("%d", &number1);
    printf("Type in your op: ");
    scanf("%s", op);
    printf("Type in your second number: ");
    scanf("%d", &number2);

    if(strcmp(op, "+") == 0){
        printf("%d\n",add(number1, number2));
    }
    else if(strcmp(op, "-")){
        printf("%d\n",sub(number1, number2));
    }
    else if( strcmp(op, "*")){
        printf("%d\n",mul(number1, number2));
    }
    else if( strcmp(op, "/")){
        printf("%d\n",div(number1, number2));
    }
    else{
        printf("That was not an operator we have!");
    }

    return 0;
}

int add(int a, int b) {
    return a+b;
}

int sub(int a, int b) {
    return a-b;
}

int mul(int a, int b) {
    return a*b;
}

int div(int a, int b) {
    return a/b;
}
