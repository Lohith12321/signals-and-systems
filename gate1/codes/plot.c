#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("plot.txt", "w");

    if (fp == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double t;
    for (t = 0; t <= 7; t += 0.01) {
        double y = (t >= 0) ? (6 - 6 * exp(-10 * t) - 60 * t * exp(-10 * t)) : 0;
        fprintf(fp, "%lf %lf\n", t, y);
    }

    fclose(fp);
    return 0;
}
