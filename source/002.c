#include <stdio.h>

#define LIMIT 4000000

int main() 
{
  int number1;
  int number2;
  int sum;

  num1 = 0;
  num2 = 1;

  sum = even_valued_fibonacci_terms_sum(number1, number2, LIMIT);

  printf("%d\n", sum);

  return 0;
}

int even_valued_fibonacci_terms_sum(int number1, int number2, int limit)
{
  if(number2 >= limit)
    return 0;

  if(number2 % 2 == 0)
    return number2 + even_fib_values_sum(number2, number1 + number2, limit);

  return even_fib_values_sum(number2, number1 + number2, limit);
}

