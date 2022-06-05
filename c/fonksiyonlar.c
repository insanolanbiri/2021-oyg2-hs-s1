#include <stdio.h>

/**
 * donus_tipi fonksiyon([parametreler]){olay;[return;]}
*/

void test(int a)
{
    a+=1;
}

void test2(int *a)
{
    *a+=1;
}

void test3(int a[])
{
    a[0]=30;
}



int main(int argc, char const *argv[])
{
    int s1=10;
    int s2=15;
    printf("s1=%d;s2=%d\n",s1,s2);
    test(s1);
    test2(&s2);
    printf("s1=%d;s2=%d\n",s1,s2);

    int dizi[5]={20,30,45,60,75};
    printf("dizi[0]=%d\n",dizi[0]);
    test3(dizi);
    printf("dizi[0]=%d\n",dizi[0]);

    char *isim="eren";
    printf("isim=%d-*-*-%c\n",*isim+1,*isim+1);
    printf("isim=%d-*-*-%c\n",*(isim+1),*(isim+1));
    printf("a1=%p,a2=%p\n",isim,isim+1);

    return 0;
}

