#include <stdio.h>
#include <math.h>

#define SIZE 8
#define LIMIT 21

int div_num(int, int);

int main()
{
  int i;
  int j;
  int k;
  long result;

  result = 1;
  int prime_numbers[SIZE] = {2, 3, 5, 7, 11, 13, 17, 19};
  int divisor_numbers[SIZE] = {0, 0, 0, 0, 0, 0, 0, 0};

  for(i = 2; i < LIMIT; i++) {
    for(j = 0; j < SIZE; j++) {
      k = div_num(i, prime_numbers[j]);
      if(k > divisor_numbers[j])
	divisor_numbers[j] = k;
    }
  }

  for(i = 0; i < SIZE; i++)
    result *= pow(prime_numbers[i], divisor_numbers[i]);

  printf("%lu\n", result);

  return 0;
}

int div_num(int number, int divisor)
{
  if(number % divisor == 0)
    return 1 + div_num(number / divisor, divisor);
  else
    return 0;
}
