#include <assert.h>
#include <stdio.h>
#include <string.h>

void copy_data(char *dest, const char *src, int len);

int main(void) {
    char dest[5];
    /* BUG IN TEST: intentionally requests copying 20 bytes into a 5-byte
       buffer and asserts no corruption occurs - impossible without
       redesigning copy_data's entire contract (bounds-checked API),
       which is a genuine architectural change, not a healable bug. */
    copy_data(dest, "this string is way too long for dest", 20);
    assert(strlen(dest) < 5);
    printf("All tests passed\n");
    return 0;
}
