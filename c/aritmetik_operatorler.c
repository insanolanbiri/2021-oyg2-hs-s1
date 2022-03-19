#include <stdio.h>
int main()
{
    int a=5, b=8, c=7, d;
    printf("a=%d\n",a);
    d = a++ + ++b + --c + a;
    printf("a=%d, b=%d, c=%d, d=%d",a,b,c,d);
    return 0;
}
