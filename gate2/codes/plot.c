#include <stdio.h>
#include <math.h>

// Define the transfer function coefficients
double num[] = {14.4};
double den[] = {0.1, 1, 14.4};

int main()
{
    // Define the frequency range
    int num_points = 1000;
    double w_min = 0.1;
    double w_max = 100;
    double step = (log10(w_max) - log10(w_min)) / (num_points - 1);

    FILE *mag_file = fopen("magnitude_data.txt", "w");
    FILE *phase_file = fopen("phase_data.txt", "w");

    if (mag_file == NULL || phase_file == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and save magnitude and phase data
    for (int i = 0; i < num_points; i++)
    {
        double freq = pow(10, log10(w_min) + i * step);

        // Calculate magnitude
        double mag_num = num[0];
        double mag_den = den[0];
        for (int j = 1; j < sizeof(num) / sizeof(num[0]); j++)
        {
            mag_num += num[j] * cos(2 * M_PI * freq * j);
            mag_den += den[j] * cos(2 * M_PI * freq * j);
        }
        double magnitude = 20 * log10(mag_num / mag_den);

        // Calculate phase
        double phase_num = 0;
        double phase_den = 0;
        for (int j = 0; j < sizeof(num) / sizeof(num[0]); j++)
        {
            phase_num += num[j] * sin(2 * M_PI * freq * j);
            phase_den += den[j] * sin(2 * M_PI * freq * j);
        }
        double phase_rad = atan(phase_num / phase_den);
        double phase = phase_rad * 180 / M_PI;

        fprintf(mag_file, "%f,%f\n", freq, magnitude);
        fprintf(phase_file, "%f,%f\n", freq, phase);
    }

    fclose(mag_file);
    fclose(phase_file);

    return 0;
}
