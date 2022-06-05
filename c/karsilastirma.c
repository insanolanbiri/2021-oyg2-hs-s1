#include <stdio.h>
int main()
{
    /**karşılaştırma operatörleri
     * <
     * >
     * <=
     * >=
     * !=
     * ! (0 ise 1 değilse 0)
     * &&
     * ||
    */
    printf("%d\n",!'\0'); // sonuçta '\0' da bellekte 00000000 -> mantıksal değeri 0
    int a=5, b=8, c;
    c = 3< a+b >9;
    printf("c=%d\n",c);
    return 0;
}
