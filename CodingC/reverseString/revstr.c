#include <stdio.h>
#include <string.h>

#define MAX_LEN 1000

int main() {
    char buffer[MAX_LEN];
    int len = 0;
    int c;

    // Read all input into buffer
    while ((c = getchar()) != EOF && len < MAX_LEN - 1) {
        buffer[len++] = c;
    }
    buffer[len] = '\0'; // Null terminate the string

    // Print the buffer in reverse order
    for (int i = len - 1; i >= 0; i--) {
        putchar(buffer[i]);
    }

    return 0;
}
