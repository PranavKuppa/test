#include <assert.h>
#include <stdio.h>
#include <stdint.h>

int32_t square(int32_t value);
int32_t is_even(int32_t value);

int main(void)
{
    assert(square(4) == 16);
    assert(is_even(4) == 1);
    assert(is_even(3) == 0);
    printf("All tests passed\n");
    return 0;
}
