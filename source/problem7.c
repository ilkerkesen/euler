#include <stdio.h>
#include <math.h>

int is_prime(int);

int main(){
  int i;
  int term;

  term = 0;
  
  for(i = 1; term != 10001;) {
    if(is_prime(++i))
      term++;
  }

  printf("%d\n", i);

  return 0;
}

int is_prime(int num)
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
