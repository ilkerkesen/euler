#include <stdio.h>
#include <math.h>

int gauss(int);
int divisor_count(int);

int main()
{
  int i;

  for(i = 0; divisor_count(gauss(i)) <= 500; i++);

  printf("%ld\n", gauss(i));

  return 0;
}

int gauss(int number)
{
  return number * (number + 1) / 2;
}

int divisor_count(int number)
{
  int i;
  int count;

  count = 0;

  for(i = 1; i <= sqrt(number); i++) {
    if(number % i == 0) {
      count++;
      if(number / i != i)
	count++;
    }
  }

  return count;
}
