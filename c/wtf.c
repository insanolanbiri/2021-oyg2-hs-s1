/**
 * bilsemde böyle bişey yapmadık ama canım sıkılmış olsa gerek,
 * evde böyle bişey yapmışım.
 */

#include <stdio.h>

/**
 * @brief bilim olimpiyatları sorusu kendisi (2016 Bilgisayar A kitapçığı soru 42). nasıl olduğunu çözebilmiş değilim.
 */
int main(){
    int d[][3][2]={4,5,6,7,8,9,10,11,12,13,14,15,16};
    int i=-1;
    int j;
    j=d[i++][++i][++i]; // neden 4 (yani d[0][0][0])
    printf("%d",j);
    return 0;
}
