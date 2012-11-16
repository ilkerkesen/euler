#include <stdio.h>

long collatz(long);

int main()
{
  long i;
  long max;
  long hold;
  long res;

  max = 0;

  for(i = 1; i < 1000000; i++) {
    hold = collatz(i);
    if(hold > max) {
      max = hold;
      res = i;
    }
  }

  printf("It is %ld with %ld terms.\n", res, max);
  
  return 0;
}

long collatz(long number)
{
  if(number == 1)
    return 1;

  if(number % 2 == 0)
    return 1 + collatz(number / 2);
  else
    return 1 + collatz(3 * number + 1);
}
