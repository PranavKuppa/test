#include <assert.h>
#include <stdio.h>

int add(int a, int b);
int subtract(int a, int b);

int main(void) {
    assert(add(2, 3) == 5);
    assert(subtract(5, 2) == 3);
    printf("All tests passed\n");
    return 0;
}
