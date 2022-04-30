#include <stdio.h>
int main()
{
    int id1[5]; // değerler rastgele
    int id2[]={3,5,6}; // 3 eleman
    int id3[5]={1,5}; // diğer elemanlar 0 (varsayılan)
    printf("boyut id1 (byte): %d\n",sizeof(id1));
    printf("boyut id2 (byte): %d\n",sizeof(id2));
    printf("boyut id3 (byte): %d\n",sizeof(id3));
    printf("eleman id3: %d\n",sizeof(id3)/sizeof(int));
    printf("%d,%d,%d,%d,%d,%d,%d,%d,%d\n",
    sizeof(int),
    sizeof(float),
    sizeof(char),
    sizeof(double),
    sizeof(short)
    );
    // char dizisi=karakter dizisi=dizge
    char ad[]="eren";
    char soyad[20];
    scanf("%s",soyad);
    printf("merhaba %s %s\n",ad,soyad);
    int i=0;
    printf("aa:%d,%d,%d,%d\n",i++,i++,++i,++i)

    return 0;
}
