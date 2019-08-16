#include <stdio.h>
#define BUFFER 100

int main(int argc, char**argv){
    char name[BUFFER];
    printf("Enter your name here: \n");
    scanf("%s",  name);
    int age = 0;
    printf("Enter your age here: \n");
    scanf("%d", &age);
    printf("%s is %d years old\n", name, age);

    char name2[BUFFER] = "Peter Parker";
    int age2 = 16;
    printf("%s is %d years old\n", name2, age2);

    if(age > age2){
        printf("%s is older than %s", name, name2);
    }
    else if(age < age2){
        printf("%s is younger than %s", name, name2);
    }
    else{
        printf("%s is the same age as %s", name, name2);
    }

    printf("\n");
    return 0;
}