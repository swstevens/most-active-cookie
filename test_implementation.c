
#include <stdio.h>
#include <string.h>
#include <time.h>

const int SIZE = 1024;

//helper to increment value lists
void increment_instance(char*to_increment, char**cookies,int* instances){
    for (int i=0; i<SIZE;i++){
        if(strcmp(cookies[i],to_increment) == 0){
            instances[i]++;
        }
    }
    return;
}

void find_most_active(char filename[], int dateflag, char date[]){
    char line[1024];


}

int main(int argc, char* argv[]){
    //Processing Flags
    int i = 2;
    int dateflag = 0;
    char *date;
    while (i<argc){
        if(argv[i][0]!= '-'){
            i++;
            continue;
        } if (strstr(argv[i],"d")){
            dateflag=1;
            date = argv[i+1];
        }
        i++;
    }
    // run child function (parsed all flags and set )
    if (i==argc && dateflag){
        find_most_active(argv[1],dateflag,date);
    }
    return 0;

}