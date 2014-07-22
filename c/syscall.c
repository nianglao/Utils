#include <stdio.h>
#include <unistd.h>     // For syscall()
#include <sys/syscall.h>// For SYS_getpid
#include <sys/types.h>  // For pid_t

int main() 
{
    pid_t pid;
    pid = syscall(SYS_getpid);
    printf("SYS_getpid = %d ; pid = %u\n", SYS_getpid, pid);
    return 0;
}
