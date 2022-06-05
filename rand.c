/**
 * bilsemde böyle bişey yapmadık ama canım sıkılmış olsa gerek,
 * evde böyle bişey yapmışım.
 */

#include <stdlib.h>
#include <stdio.h>

#define forever for (;;) // daha güzel

/**
 * @brief ekrana sonsuza kadar boş boş rastgele sayı yazdırma fonksiyonu.
 */
int main(int argc, char const *argv[])
{
    forever
    {
        printf("%x\n", rand());
    }
    return 0;
}
