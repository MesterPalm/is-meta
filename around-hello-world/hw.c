#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* concat(const char *s1, const char *s2)
{
	// not my function, found it at https://stackoverflow.com/questions/8465006/how-do-i-concatenate-two-strings-in-c
    char *result = malloc(strlen(s1) + strlen(s2) + 1); // +1 for the null-terminator
    // in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

int main(int argc, char *argv[]){
	printf("Hello from c\n");
	const char* rm = "rm ";
	system(concat(rm, argv[0]));
	system("./hw.sh");
}
