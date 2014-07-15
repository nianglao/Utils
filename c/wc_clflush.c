/* Test for write-combining vs clflush.
 * 
 * Compile:
 *    gcc -o test wc_clflush.c  
 * */

#include <stdint.h> 
#include <stdio.h>
#include <sys/time.h> /* For struct timeval and gettimeofday */

static inline
void asm_sse_write_block64(volatile uint64_t *addr, uint64_t *val)
{
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[0]):"r"(val[0]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[1]):"r"(val[1]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[2]):"r"(val[2]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[3]):"r"(val[3]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[4]):"r"(val[4]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[5]):"r"(val[5]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[6]):"r"(val[6]));
    __asm__ __volatile__("movnti %1, %0":"=m"(*&addr[7]):"r"(val[7]));
}

static inline
void asm_wb_write_block64(volatile uint64_t *addr, uint64_t *val)
{
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[0]):"r"(val[0]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[1]):"r"(val[1]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[2]):"r"(val[2]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[3]):"r"(val[3]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[4]):"r"(val[4]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[5]):"r"(val[5]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[6]):"r"(val[6]));
    __asm__ __volatile__("mov %1, %0":"=r"(*&addr[7]):"r"(val[7]));
}
static inline
void asm_clflush(volatile uint64_t *addr)
{
    __asm__ __volatile__("clflush %0"::"m"(*addr));
}

static inline
void asm_mfence(void)
{
    __asm__ __volatile__("mfence");
}

static inline
void asm_sfence(void)
{
    __asm__ __volatile__("sfence");
}

/********************************************************/

#define BYTES_PER_LINE 8
uint64_t addr[BYTES_PER_LINE];
uint64_t val[BYTES_PER_LINE];

int main()
{
    struct timeval start_time;
    struct timeval stop_time;
    double wc_time = 0.0;
    double cl_time = 0.0;
    double loop_time = 0.0;

    int i, j;
    int repeat = 1000000;
    
    /* Init the addr and val array */
    for (i = 0; i < BYTES_PER_LINE; ++i){
        addr[i] = (uint64_t)&(val[i]); 
        printf("addr[%d] = %lx\n", i, addr[i]);
        val[i] = i;
    }

    /* Test for movnti */
    gettimeofday(&start_time, NULL);
    for (j = 0; j < repeat; ++j){
        asm_sse_write_block64(addr, val);
        asm_mfence();
    }
    gettimeofday(&stop_time, NULL);
    wc_time = (stop_time.tv_sec - start_time.tv_sec)
            + (stop_time.tv_usec - start_time.tv_usec) * 1.0 / 1000000;

    /* Test for clflush */
    gettimeofday(&start_time, NULL);
    for (j = 0; j < repeat; ++j){
        val[0] = 0; 
        val[1] = 0;
        val[2] = 0;
        val[3] = 0;
        val[4] = 0;
        val[5] = 0;
        val[6] = 0;
        val[7] = 0;
        // asm_wb_write_block64(addr, val); //slower than directly write to the val[]
        asm_clflush(val);
        asm_mfence();
    } 
    gettimeofday(&stop_time, NULL);
    cl_time = (stop_time.tv_sec - start_time.tv_sec)
            + (stop_time.tv_usec - start_time.tv_usec) * 1.0 / 1000000;

    /* Test for loop_time */
    gettimeofday(&start_time, NULL);
    for (j = 0; j < repeat; ++j){
        val[0] = 0; 
        val[1] = 0;
        val[2] = 0;
        val[3] = 0;
        val[4] = 0;
        val[5] = 0;
        val[6] = 0;
        val[7] = 0;
    } 
    gettimeofday(&stop_time, NULL);
    loop_time = (stop_time.tv_sec - start_time.tv_sec)
            + (stop_time.tv_usec - start_time.tv_usec) * 1.0 / 1000000;
    /* Print stats */
    printf("*********************\n");
    printf("repeat  : %d\n", repeat);
    printf("movnti  : %lf\n", wc_time);
    printf("clflush : %lf\n", cl_time);
    printf("loop    : %lf\n", loop_time);
    printf("flush   : %lf\n", cl_time - loop_time);
    printf("lp/clf  : %lf\n", loop_time / cl_time);
    printf("fl/clf  : %lf\n", (cl_time - loop_time) / cl_time);
    printf("*********************\n");

    return 0;
}
