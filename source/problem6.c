#include <stdio.h>

int main()
{
  int i;
  long sum_square;
  long square_sum;

  sum_square = 0;
  square_sum = 0;

  for(i = 1; i < 101; i++) {
    sum_square += i * i;
    square_sum += i;
  }

  square_sum *= square_sum;

  printf("%lu\n", square_sum - sum_square);

  return 0;
}
