#include "stdio.h"

int main(int argc, char const *argv[])
{
    int a = 20000000;
    while(a > 0)
        a -= 1;
    printf("%d\n",a);
    return 0;
}