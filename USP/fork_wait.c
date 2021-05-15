#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

void func() {
    pid_t child = fork();

    if (child == 0) {
        pid_t process_id = getpid();
        pid_t parent_id = getppid();
        int command_size = 512;
        char command[command_size];

        printf("Hello from the child process\n");
        printf("Child process ID: %d\n", process_id);
        printf("Parent process ID: %d\n", parent_id);

        printf("Enter a command: ");
        scanf("%[^\n]s", command);

        printf("Executing the command: \n\n");
        system(command);
        printf("\n");
    } else {
        wait(NULL);
        printf("Hello from the parent process\n");
        printf("Parent process ID: %d\n", getpid());
        printf("Parent process created child process with ID: %d\n", child);
    }
}

int main() {
    func();
    return 0;
}