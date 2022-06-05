/**
 * bilsemde böyle bişey yapmadık ama canım sıkılmış olsa gerek,
 * evde böyle bişey yapmışım.
 */

#include <stdlib.h>
#include <stdio.h>

/**
 * @brief sürekli bellek allocate ederek bilgisayarı sapıttırma fonksiyonu.
 * @return işlemin başarılı olup olmadığı
 */
int main(int argc, char const *argv[])
{
    /** yumuşak ğe.
     * konumuzla alakası yok ama
     * c ve pythonda değişik karakterli değişkenler sorunsuz çalışıyor
     */
    int ğ = 0, 👍 = 5;

    int *ü = malloc(sizeof(int));
    if (ü == NULL)
        return 1;
    while (1)
        *ü = malloc(sizeof(int) * 1000000);
    return 0;
}
