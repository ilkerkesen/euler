#include <stdio.h>
#include <math.h>

#define LIMIT 2000000

int is_prime(long int);

int main(){
  long i;
  long sum;

  sum = 0;
  for(i = 2; i < LIMIT; i++) 
    if(is_prime(i))
       sum += i;

  printf("%lu\n", sum);

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
