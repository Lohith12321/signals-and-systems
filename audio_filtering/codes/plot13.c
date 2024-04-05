#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <time.h>
#include <math.h>

#define EPS 1e-6
#define Pi 3.14159265

// Function for FFT
complex double *custom_fft(int n, complex double *a) {
    if (n == 1) return a;
    complex double *g = (complex double *)malloc(n/2*sizeof(complex double));
    complex double *h = (complex double *)malloc(n/2*sizeof(complex double));
    for (int i = 0; i < n; i++) {
        if (i%2) h[i/2] = a[i];
        else g[i/2] = a[i];
    }
    g = custom_fft(n/2, g);
    h = custom_fft(n/2, h);
    for (int i = 0; i < n; i++) a[i] = g[i%(n/2)] + cexp(-I*2*Pi*i/n)*h[i%(n/2)];
    free(g); free(h);
    return a;
}

// Function for IFFT
complex double *custom_ifft(int n, complex double *a) {
    if (n == 1) return a;
    complex double *g = (complex double *)malloc(n/2*sizeof(complex double));
    complex double *h = (complex double *)malloc(n/2*sizeof(complex double));
    for (int i = 0; i < n; i++) {
        if (i%2) h[i/2] = a[i];
        else g[i/2] = a[i];
    }
    g = custom_ifft(n/2, g);
    h = custom_ifft(n/2, h);
    for (int i = 0; i < n; i++) {
        a[i] = g[i%(n/2)] + cexp(I*2*Pi*i/n)*h[i%(n/2)];
        a[i] /= n;
    }
    free(g); free(h);
    return a;
}

// Function for Convolution
complex double *custom_convolve(complex double *h, complex double *x, int n) {
    complex double *a = (complex double *)calloc(n, sizeof(complex double));
    for (int i = 0; i < n; i++) for (int j = 0; j <= i; j++) a[i] += h[j]*x[i - j];
    return a;
}

int main() {
    FILE *f_time_fft = fopen("fft.txt", "w");
    FILE *f_time_conv = fopen("conv.txt", "w");

    for (int j = 0; j <= 15; j++) {
        srand(time(0));
        int n = 1 << j;
        complex double *x = (complex double *)malloc(sizeof(complex double) * n);
        complex double *h = (complex double *)malloc(sizeof(complex double) * n);

        for (int i = 0; i < n; i++) {
            x[i] = (double)drand48();
            h[i] = (double)drand48();
        }

        // Measure time for FFT
        clock_t fft_begin = clock();
        custom_fft(n, x);
        clock_t fft_end = clock();

        // Measure time for IFFT
        clock_t ifft_begin = clock();
        custom_ifft(n, x);
        clock_t ifft_end = clock();

        // Measure time for convolution
        clock_t conv_begin = clock();
        custom_convolve(h, x, n);
        clock_t conv_end = clock();

        // Calculate total time for FFT and IFFT
        double time_fft = (double)(fft_end - fft_begin) / CLOCKS_PER_SEC;
        double time_ifft = (double)(ifft_end - ifft_begin) / CLOCKS_PER_SEC;
        double total_time_fft = time_fft + time_ifft;

        // Write total time for FFT and IFFT to file
        fprintf(f_time_fft, "%lf\n", total_time_fft);

        // Write time for convolution to file
        double time_conv = (double)(conv_end - conv_begin) / CLOCKS_PER_SEC;
        fprintf(f_time_conv, "%lf\n", time_conv);

        free(x);
        free(h);
    }

    fclose(f_time_fft);
    fclose(f_time_conv);

    return 0;
}
