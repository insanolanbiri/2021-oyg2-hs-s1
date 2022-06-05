/**
 * bilsemde böyle bişey yapmadık ama canım sıkılmış olsa gerek,
 * evde böyle bişey yapmışım.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * @brief asal sayı bulma şeyi, sanırsam `sieve of eratostenes` diye geçiyor
 * @param max asal sayıların bulunacağı maksimum değer
 * @return işlemin başarılı olup olmadığı
 */
int asal(int max)
{
    if (max < 2)
    {
        return 1;
    }

    int durum[max + 1];
    int len = sizeof(durum) / sizeof(int);

    durum[0] = durum[1] = 0;

    for (int i = 2; i < len; i++)
        durum[i] = 1;

    for (int i = 2; i < len; i++)
        if (durum[i])
            for (int j = i + 1; j < len; j++)
                if (j % i == 0)
                    durum[j] = 0;

    for (int i = 0; i < len; i++)
        if (durum[i])
            printf("%d\n", i);

    return 0;
}

/**
 * @brief verilen 1. argümana kadar olan asal sayıları yazdıran main method.
 * çalıştırırken argüman veriyorsunuz: `./a.out <max>` gibi.
 */
int main(int argc, char const *argv[])
{
    if (argc == 2)
    {
        int given_max = (int)strtol(argv[1], NULL, 10);
        printf("max: %d\n", given_max);
        asal(given_max);
        return 0;
    }

    printf("bana bir sayı vermen lazım\n");
    return 1;
}
