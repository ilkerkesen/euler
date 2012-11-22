#include <stdio.h>

#define SIZE 100

int max_sum(int [][SIZE], int);

int main()
{
  FILE *fp;
  int array[SIZE][SIZE];

  int i;
  int j;

  if((fp = fopen("067.txt", "r")) == NULL) {
    return 0;
  } 
  
  for(i = 0; !feof(fp); i++) 
    for(j = 0; j <= i; j++)
      fscanf(fp, "%d", &array[i][j]);

  printf("%d\n", max_sum(array, 98));

  return 0;
}

int max_sum(int array[][SIZE], int index)
{
  int i;

  for(i = 0; i < index+1; i++) {
    if(array[index + 1][i] > array[index + 1][i + 1])
      array[index][i] += array[index + 1][i];
    else
      array[index][i] += array[index + 1][i + 1];
  }

  if(index != 0)
    return max_sum(array, index-1);
  else
    return array[0][0];
}
