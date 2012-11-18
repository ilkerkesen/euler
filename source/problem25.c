#include <stdio.h>

#define SIZE 1000

void plus(char [], char [], char [], int);
void fibonacci(char [], char [], int);
char int_to_char(int);
int char_to_int(char);

int main()
{
  int i;
  int counter;
  
  char number1[SIZE];
  char number2[SIZE];

  for(i = 0; i < SIZE; i++) {
    number1[i] = int_to_char(0);
    number2[i] = int_to_char(0);
  }

  number1[SIZE-1] = int_to_char(1);
  number2[SIZE-1] = int_to_char(1);

  counter = 2;

  while(number2[0] == '0') {
    fibonacci(number1, number2, SIZE);
    counter++;
  }
  
  printf("%d\n", counter);

  return 0;
  
}

void plus(char number1[], char number2[], char result[], int size)
{
  int i;
  int sum;
  int remaining;

  for(i = size - 1, remaining = 0; i > -1; i--) {
    sum = (char_to_int(number1[i]) + char_to_int(number2[i]) + remaining) % 10;

    result[i] = int_to_char(sum);

    remaining = (char_to_int(number1[i]) + char_to_int(number2[i]) + remaining) / 10;
  }
}

void fibonacci(char number1[], char number2[], int size)
{
  int i;
  char result[1000];
  
  plus(number1, number2, result, size);

  for(i = 0; i < SIZE; i++) {
    number1[i] = number2[i];
    number2[i] = result[i];
  }
}

char int_to_char(int digit)
{
  return '0' + digit;
}

int char_to_int(char c)
{
  int i;

  for(i = 0; i < 10; i++)
    if(int_to_char(i) == c)
      return i;

  return -1;

}
