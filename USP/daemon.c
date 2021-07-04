#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>

void daemonize() {
    pid_t pid;

    if (getppid() == 1) // If already a daemon
        return;

    pid = fork();
    if (pid < 0)
        exit(EXIT_FAILURE);
    if (pid > 0) {
        printf("pid of the daemon process is %d\n", pid);
        exit(EXIT_SUCCESS);
    }

    if (setsid() < 0)
        exit(EXIT_FAILURE);

    umask(0);

    if ((chdir("/")) < 0)
        exit(EXIT_FAILURE);

    freopen("/dev/null", "r", stdin);
    freopen("/dev/null", "w", stdout);
    freopen("/dev/null", "w", stderr);
}

int main() {
    daemonize();
    sleep(20);
}
