#include <stdio.h>
int main()
{
    /*
    tam sayılar
    - int, short, char, long
    ondalıklı
    - float, double, long double
    */
    int i1=3.8;
    float f1=33;
    char c1='s'; // ""  olmaz
    long int li1=1e12;
    printf("s=%d\n",32/5);
    printf("s=%f\n",(float)(32/5));
    printf("s=%f\n",(float)32/5);
    printf("s=%f\n",32/5.0);
    printf("s=%d\n",32/5.0);
    printf("i1=%d\n",i1);
    printf("f1=%f\n",f1);
    printf("c1=%d,c1=%f\n",c1,c1);
    printf("c1=%d,c1=%f\n",c1+1,c1+2);
    printf("li1=%d\n",li1);
    printf("li1=%ld\n",li1);
    return 0;
}
