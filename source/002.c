#include <stdio.h>

#define LIMIT 4000000

int even_fib_terms_sum(int, int, int);

int main() 
{
  int num1;
  int num2;
  int sum;

  num1 = 0;
  num2 = 1;

  sum = even_fib_terms_sum(num1, num2, LIMIT);

  printf("%d\n", sum);

  return 0;
}

int even_fib_terms_sum(int num1, int num2, int limit)
{
  if(num2 >= limit)
    return 0;

  if(num2 % 2 == 0)
    return num2 + even_fib_terms_sum(num2, num1 + num2, limit);

  return even_fib_terms_sum(num2, num1 + num2, limit);
}

