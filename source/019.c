#include <stdio.h>

int get_day(int, int);

int main()
{
  int i;
  int j;

  int current;
  int counter;

  current = 1;
  counter = 0;

  for(i = 1900; i < 2001; i++) {
    for(j = 1; j <= 12; j++) {
      if(current % 7 == 0 && i != 1900) {
	counter++;
      }
      current += get_day(j, i);
    }
  }

  printf("%d\n", counter);

  return 0;
}

int get_day(int month, int year)
{
  if(month == 4 || month == 6 || month == 9 || month == 11)
    return 30;
  else if(month != 2)
    return 31;
  else
    if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 100))
      return 29;
    else
      return 28;
}
