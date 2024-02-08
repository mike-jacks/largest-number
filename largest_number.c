#include <stdio.h>

float find_largest_number(float num1, float num2, float num3) {
    float largest_number = num1;
    if (num2 > largest_number) largest_number = num2;
    if (num3 > largest_number) largest_number = num3;
    return largest_number;
}
int main() {
    float largest_number = find_largest_number(3, 7, 6);
    printf("%.2f\n",largest_number);
    return 0;
}

