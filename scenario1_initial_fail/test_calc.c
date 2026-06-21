#include <assert.h>
#include <stdio.h>

int add(int a, int b);

int main(void) {
    assert(add(2, 3) == 5); /* FAILS due to bug in calc.c */
    printf("All tests passed\n");
    return 0;
}
