#include <stdio.h>
int main()
{
    int a=5, b=8, c=7, d;
    printf("a=%d\n",a);
    d = a++ + ++b + --c + a;
    /**
     * ++birsey : önce arttır sonra kullan
     * birsey++ : önce kullan sonra arttır
     */
    printf("a=%d, b=%d, c=%d, d=%d\n",a,b,c,d);
    return 0;
}
