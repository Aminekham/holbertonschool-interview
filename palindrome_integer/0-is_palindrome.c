#include "palindrome.h"
/**

*/
int is_palindrome(unsigned long n)
{
    char itself[100];
    int len;
    int i=0;
    sprintf(itself, "%ld", n);
    len = strlen(itself);
    for (i; i<len/2; i++) {
        if (*(itself + i) != *(itself + len - 1 - i)){
        return 0;
        }
    }
    return 1;
}