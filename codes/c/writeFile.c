/* 
 * This file provide a method to write log or debug files into pieces.
 * It is usefull when a debug outfile or log file is as large as terebytes,
 * but we just want to check some part and no need to store the whole file,
 * and need to split into pieces in program, instead of using split command 
 * in linux. We split it into pieces, so we can remove some unnecessary part 
 * and thus utilize the disk.
 *
 * AUTHOR : nianglao
 *
 */

#include <stdio.h>


int main()
{
    FILE *fp;

    /* file sequence number*/
    int fno = 0;

    /* file name buffer */
    char buf[128];

    /* each file size */
    long SIZE = 1024;

    /* number of files, for test */
    int nums = 3;

    /* Create nums files, each size is larger than SIZE */
    for (fno = 0; fno < 3; ++fno) {
        /* Get file name here. May use another variable to store the file prefix string */
        sprintf(buf, "temp_data_%d", fno);

        fp = fopen(buf, "w");
        long size = ftell(fp);
        while (size < SIZE) {
            fprintf(fp, "%x", 0xffffffff);
            size = ftell(fp);
        }
        fclose(fp);
        printf("File %s is %ld bytes.\n", buf, size);
    }
    return 0; 
}
