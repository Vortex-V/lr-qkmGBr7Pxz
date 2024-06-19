#include <ctime>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 1024

int main (int argc, char *argv [])
{
    int fd, bout;
    fd = open("file1", O_RDWR | O_CREAT | O_APPEND, 0777);
    
    time_t currentTime = time(NULL);
    char *stringTime = ctime(&currentTime);
    write(fd, stringTime, strlen(stringTime));
    write(fd, "\n", 1);
    
    close(fd);
}