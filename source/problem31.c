#include <stdio.h>

#define LIMIT 200

int main()
{
  int a;
  int b;
  int c;
  int d;
  int e;
  int f;
  int g;
  int h;
  int sum;

  sum = 0;

  for(a = 0; a <= LIMIT; a += 200)
    for(b = 0; a + b <= LIMIT; b += 100)
      for(c = 0; a + b + c <= LIMIT; c += 50)
	for(d = 0; a + b + c + d <= LIMIT; d += 20)
	  for(e = 0; a + b + c + d + e <= LIMIT; e += 10)
	    for(f = 0; a + b + c + d + e + f <= LIMIT; f += 5)
	      for(g = 0; a + b + c + d + e + f + g <= LIMIT; g +=2)
		for(h = 0; a + b + c + d + e + f + g + h <= LIMIT; h += 1)
		  if(a + b + c + d + e + f + g + h == LIMIT)
		    sum++;

  printf("%d\n", sum);

  return 0;
}
