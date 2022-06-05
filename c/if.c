#include <stdio.h>
int main()
{
    int yas;
    printf("yaş gir: ");
    scanf("%d",&yas);
    if (yas<=0)
    {
        fprintf(stderr,"doğru düzgün gir\n");
        return 1;
    }

    if (yas<18 && yas>10)
    {
        printf("ehliyet yok\n");
    }
    else if (yas <=10)
    {
        printf("daha çocuksun\n");
    }
    else
    {
        printf("ehliyet var\n");
    }

    return 0;
}
