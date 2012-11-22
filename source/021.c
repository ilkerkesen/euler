#include <stdio.h>

int d(int);
int is_amicable(int);

int main()
{
  int i;
  int sum;

  sum = 0;

  for(i = 2; i < 10000; i++) {
    if(is_amicable(i) == 1)
      sum += i;
  }

  printf("%d\n", sum);

  return 0;
}

int d(int number)
{
  int i;
  int result;

  result = 0;

  for(i = 1; i <= number / 2; i++) {
    if(number % i == 0) {
      result += i;
    }
  }

  return result;
}

int is_amicable(int number) {
  if(number == d(d(number)) && d(number) != number)
    return 1;

  return 0;
}
