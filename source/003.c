#include <stdio.h>
#include <math.h>

int is_prime(long int);

int main(){
  unsigned long long number = 600851475143;
  unsigned long long i;

  for(i = sqrt(number); !(is_prime(i) && number % i == 0); i--);

  printf("%llu\n", i);

  return 0;
}

int is_prime(long int num)
{
  int i;

  if(num == 2)
    return 1;

  if(num % 2 == 0)
    return 0;

  for(i = 3; i < sqrt(num) + 1; i += 2) {
    if(num % i == 0)
      return 0;
  }

  return 1;
}
