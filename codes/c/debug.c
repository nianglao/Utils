/* gcc -o test debug.c 
 */
#include <stdio.h>

#define __DEBUG

#ifdef __DEBUG
# define DEBUG_PRINT_POS()  do{ fprintf(stderr, "%s(%d) {%s}\n", \
                                __FILE__, __LINE__, __func__); fflush(NULL);}while(0)
#else
# define DEBUG_PRINT_POS()
#endif


int test()
{
    DEBUG_PRINT_POS();
    return 0;
}
int main()
{
    DEBUG_PRINT_POS();
    test();
    return 0;
}
