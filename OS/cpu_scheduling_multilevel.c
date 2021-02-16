#include <stdio.h>
#include <stdlib.h>

int p;

void fcfs(int *burst_time, int initial_waiting_time, int process_count) {
    int total_turnaround_time = 0, total_waiting_time = 0;

    printf("\tProcess\tBurst time\tWaiting time\tTurnaround time\n");
    for (int waiting_time, turnaround_time = initial_waiting_time, i = 0; i < process_count; i++) {
        turnaround_time += burst_time[i];
        waiting_time = turnaround_time - burst_time[i];
        total_waiting_time += waiting_time;
        total_turnaround_time += turnaround_time;
        printf("\tP%d\t%d\t\t%d\t\t%d\n", i + 1, burst_time[i], waiting_time, turnaround_time);
    }

    printf("\n\tThe average waiting time is %0.2f\n",
           (float) total_waiting_time / (float) process_count);
    printf("\tThe average turnaround time is %0.2f\n",
           (float) total_turnaround_time / (float) process_count);
}

int main() {
    int p1, p2;
    printf("Enter priority for Queue 1: ");
    scanf("%d", &p1);
    printf("Enter priority for Queue 2: ");
    scanf("%d", &p2);
    int np1, np2, i, w1 = 0, w2 = 0;
    if (p1 == p2) {
        printf("Priority cannot be the same\n");
        exit(1);
    }

    printf("Queue 1\n");
    printf("\tEnter the number of process: ");
    scanf("%d", &np1);
    int q1[np1];
    for (i = 0; i < np1; i++) {
        printf("\tEnter the burst time for Process %d: ", i + 1);
        scanf("%d", &q1[i]);
        w1 += q1[i];
    }

    printf("Queue 2\n");
    printf("\tEnter the number of process: ");
    scanf("%d", &np2);
    int q2[np2];
    for (i = 0; i < np2; i++) {
        printf("\tEnter the burst time for Process %d: ", i + np1 + 1);
        scanf("%d", &q2[i]);
        w2 += q2[i];
    }

    if (p1 < p2) {
        printf("\nQueue 1:\n");
        p = 1;
        fcfs(q1, 0, np1);
        printf("\nQueue 2:\n");
        fcfs(q2, w1, np2);
    } else {
        printf("\nQueue 2:\n");
        p = np1 + 1;
        fcfs(q2, 0, np2);
        printf("\nQueue 1:\n");
        p = 1;
        fcfs(q1, w2, np1);
    }
    return 0;
}