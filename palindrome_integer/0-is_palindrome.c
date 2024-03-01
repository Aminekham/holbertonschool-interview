#include "palindrome.h"
/**

*/
int is_palindrome(unsigned long n)
{
    char itself[100];
    sprintf(itself, "%ld", n);
    int len = strlen(itself);
    for (int i=0;i<len/2;i++) {
        if (*(itself + i) != *(itself + len - 1 - i)){
        return 0;
        }
    }
    return 1;
}