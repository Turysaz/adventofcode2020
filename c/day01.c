#include <stdio.h>

int main() {
    /* input */
    unsigned int buf, count = 0, arr[256];
    /* solutions */
    unsigned int p1, p2;
    /* iterations */
    unsigned int i, j, k;

    while (scanf("%i", &buf) != EOF) {
        arr[count++] = buf;
    }

    for (i = 0; i < count; i++) {
        for (j = 0; j < count; j++) {
            if (arr[i] + arr[j] == 2020) {
                p1 = arr[i] * arr[j];
            }

            for (k = 0; k < count; k++) {
                if (arr[i] + arr[j] + arr[k] == 2020) {
                    p2 = arr[i] * arr[j] * arr[k];
                }
            }
        }
    }

    printf("Part 1: %u\nPart 2: %u\n", p1, p2);

    return 0;
}
