#include <stdio.h>
#include <stdlib.h>

#define COL_LIMIT 20    // Maximum column width

int main(void) {
    int c;
    int col = 0;                // current column counter
    int last_blank = -1;        // position of last blank
    char buffer[COL_LIMIT + 1]; // temp buffer for current segment
    int buf_index = 0;

    while ((c = getchar()) != EOF) {
        buffer[buf_index++] = c;
        col++;

        if (c == ' ' || c == '\t') {
            last_blank = buf_index - 1;  // remember last blank
        }

        // If we reached the limit
        if (col >= COL_LIMIT) {
            if (last_blank >= 0) {
                // Print up to the last blank
                for (int i = 0; i < last_blank; i++) {
                    putchar(buffer[i]);
                }
                putchar('\n');

                // Shift remainder of buffer to start
                int shift = 0;
                for (int i = last_blank + 1; i < buf_index; i++) {
                    buffer[shift++] = buffer[i];
                }
                buf_index = shift;
            } else {
                // No blank found, just break at limit
                for (int i = 0; i < buf_index; i++) {
                    putchar(buffer[i]);
                }
                putchar('\n');
                buf_index = 0;
            }

            col = buf_index;   // new column count
            last_blank = -1;   // reset blank tracker
        }

        // Handle newlines normally (reset everything)
        if (c == '\n') {
            for (int i = 0; i < buf_index; i++) {
                putchar(buffer[i]);
            }
            buf_index = 0;
            col = 0;
            last_blank = -1;
        }
    }

    // Flush any remaining characters
    for (int i = 0; i < buf_index; i++) {
        putchar(buffer[i]);
    }

    return 0;
}
