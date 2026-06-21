#include <stdio.h>

int global_counter;  /* MISRA violation: non-const global, no static qualifier */

float read_sensor(void) {
    int x;  /* MISRA violation: uninitialized variable used below */
    return x * 1.5;  /* also implicit int-to-float, mixed types */
}

void process(int flag) {
    if (flag = 1) {  /* MISRA violation: assignment in conditional, should be == */
        printf("flag set\n");
    }
}
