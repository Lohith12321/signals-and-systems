#include <stdio.h>

int main() {
    int n = 23;
    int a = 0;
    int d = 7;
    int nth_term = 149;

    int sum = (n / 2) * (2 * a + (n - 1) * d);

    if (sum == 1661) {
        printf("Verified\n");
    } else {
        printf("Not Verified\n");
    }

    return 0;
}
