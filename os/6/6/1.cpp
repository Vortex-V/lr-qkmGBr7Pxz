#include <fcntl.h>
#include <unistd.h>

#define BUF_SIZE 1024

int main (int argc, char *argv [])
{
    if (argc <= 2) {
        return 1;
    }
    
    int input_fd, output_fd;
    int bytes_in, bytes_out;
    char rec [BUF_SIZE];
    input_fd = open(argv [1], O_RDONLY);
    if (input_fd==-1) {
         return 2;
    }
        
    output_fd = open(argv [2], O_WRONLY | O_CREAT, 0666);
    if (output_fd==-1) {
         return 3;
    }
    
    while ((bytes_in = read(input_fd, rec, BUF_SIZE)) > 0) {
        bytes_out = write (output_fd, rec, bytes_in);
        if (bytes_in != bytes_out) {
            return 4;
        }

        close(input_fd);
        close(output_fd);
        return 0;
    }
}