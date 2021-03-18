#include <stdio.h>
#include <stdlib.h>

typedef struct ProcessTable {
    int process_count;
    int *burst_time;
} ProcessTable;

void fcfs(ProcessTable *);
void sjf(ProcessTable *);
void priority(ProcessTable *);
void round_robin(ProcessTable *);

int main() {
    ProcessTable *pt = (ProcessTable *) malloc(sizeof(ProcessTable));
    printf("\t\tCPU scheduling\n");
    printf("Enter the number of process: ");
    scanf("%d", &pt->process_count);

    pt->burst_time = (int *) malloc(pt->process_count * sizeof(int));
    printf("Enter the Burst time for each process\n");
    for (int i = 0; i < pt->process_count; i++) {
        printf("\tP%d: ", i + 1);
        scanf("%d", &pt->burst_time[i]);
    }

    fcfs(pt);
    sjf(pt);
    round_robin(pt);
    priority(pt);
    return 0;
}

void fcfs(ProcessTable *pt) {
    printf("\nFirst come first serve\n");
    int total_turnaround_time = 0, total_waiting_time = 0;

    printf("\tProcess\tBurst time\tWaiting time\tTurnaround time\n");
    for (int waiting_time, turnaround_time = 0, i = 0; i < pt->process_count; i++) {
        turnaround_time += pt->burst_time[i];
        waiting_time = turnaround_time - pt->burst_time[i];
        total_waiting_time += waiting_time;
        total_turnaround_time += turnaround_time;
        printf("\tP%d\t%d\t\t%d\t\t%d\n", i + 1, pt->burst_time[i], waiting_time, turnaround_time);
    }

    printf("\n\tThe average waiting time is %0.2f\n",
           (float) total_waiting_time / (float) pt->process_count);
    printf("\tThe average turnaround time is %0.2f\n",
           (float) total_turnaround_time / (float) pt->process_count);
}

void sjf(ProcessTable *pt) {
    printf("\nShortest job first\n");
    int total_turnaround_time = 0, total_waiting_time = 0;
    int burst_time[pt->process_count], processes[pt->process_count];

    for (int i = 0; i < pt->process_count; i++) {
        burst_time[i] = pt->burst_time[i];
        processes[i] = i + 1;
    }

    for (int i = 0; i < pt->process_count; i++) {
        for (int j = 0; j < pt->process_count - i - 1; j++) {
            if (burst_time[j] > burst_time[j + 1]) {
                burst_time[j] += burst_time[j + 1];
                burst_time[j + 1] = burst_time[j] - burst_time[j + 1];
                burst_time[j] = burst_time[j] - burst_time[j + 1];

                processes[j] += processes[j + 1];
                processes[j + 1] = processes[j] - processes[j + 1];
                processes[j] = processes[j] - processes[j + 1];
            }
        }
    }

    printf("\tProcess\tBurst time\tWaiting time\tTurnaround time\n");
    for (int waiting_time, turnaround_time = 0, i = 0; i < pt->process_count; i++) {
        turnaround_time += burst_time[i];
        waiting_time = turnaround_time - burst_time[i];
        total_waiting_time += waiting_time;
        total_turnaround_time += turnaround_time;
        printf("\tP%d\t%d\t\t%d\t\t%d\n",
               processes[i], burst_time[i], waiting_time, turnaround_time);
    }

    printf("\n\tThe average waiting time is %0.2f\n",
           (float) total_waiting_time / (float) pt->process_count);
    printf("\tThe average turnaround time is %0.2f\n",
           (float) total_turnaround_time / (float) pt->process_count);
}

void priority(ProcessTable *pt) {
    printf("\nPriority scheduling\n");
    int total_waiting_time = 0, total_turnaround_time = 0;
    int burst_time[pt->process_count], priority[pt->process_count], processes[pt->process_count];

    printf("\tEnter Priority for each process\n");
    for (int i = 0; i < pt->process_count; i++) {
        printf("\t\tP%d: ", i + 1);
        scanf("%d", &priority[i]);
    }

    for (int i = 0; i < pt->process_count; i++) {
        burst_time[i] = pt->burst_time[i];
        processes[i] = i + 1;
    }

    for (int i = 0; i < pt->process_count; i++) {
        for (int j = 0; j < pt->process_count - i - 1; j++) {
            if (priority[j] > priority[j + 1]) {
                priority[j] += priority[j + 1];
                priority[j + 1] = priority[j] - priority[j + 1];
                priority[j] = priority[j] - priority[j + 1];

                burst_time[j] += burst_time[j + 1];
                burst_time[j + 1] = burst_time[j] - burst_time[j + 1];
                burst_time[j] = burst_time[j] - burst_time[j + 1];

                processes[j] += processes[j + 1];
                processes[j + 1] = processes[j] - processes[j + 1];
                processes[j] = processes[j] - processes[j + 1];
            }
        }
    }

    printf("\tProcess\tBurst time\tPriority\tWaiting time\tTurnaround time\n");
    for (int waiting_time, turnaround_time = 0, i = 0; i < pt->process_count; i++) {
        turnaround_time += burst_time[i];
        waiting_time = turnaround_time - burst_time[i];
        total_waiting_time += waiting_time;
        total_turnaround_time += turnaround_time;
        printf("\tP%d\t%d\t\t%d\t\t%d\t\t%d\n",
               processes[i], burst_time[i], priority[i], waiting_time, turnaround_time);
    }

    printf("\n\tAverage Waiting Time = %0.2f\n",
           (float) total_waiting_time / (float) pt->process_count);
    printf("\tAverage Turnaround Time = %0.2f\n",
           (float) total_turnaround_time / (float) pt->process_count);
}

void round_robin(ProcessTable *pt) {
    printf("\nRound robin\n");
    int time_quantum, total_waiting_time = 0, total_turnaround_time = 0, remaining = pt->process_count;
    int remaining_time[pt->process_count];

    for (int i = 0; i < pt->process_count; i++)
        remaining_time[i] = pt->burst_time[i];

    printf("\tEnter time quantum: ");
    scanf("%d", &time_quantum);

    printf("\tProcess\tBurst time\tWaiting time\tTurnaround time\n");
    for (int waiting_time, turnaround_time = 0, i = 0; remaining != 0; i = (i + 1) % pt->process_count) {
        if (remaining_time[i] > 0 && remaining_time[i] <= time_quantum) {
            turnaround_time += remaining_time[i];
            remaining_time[i] = 0;
            remaining--;
            waiting_time = turnaround_time - pt->burst_time[i];
            total_waiting_time += waiting_time;
            total_turnaround_time += turnaround_time;
            printf("\tP%d\t%d\t\t%d\t\t%d\n",
                   i + 1, pt->burst_time[i], waiting_time, turnaround_time);
        } else if (remaining_time[i] > time_quantum) {
            remaining_time[i] -= time_quantum;
            turnaround_time += time_quantum;
        }
    }

    printf("\n\tAverage Waiting Time = %0.2f\n",
           (float) total_waiting_time / (float) pt->process_count);
    printf("\tAverage Turnaround Time = %0.2f\n",
           (float) total_turnaround_time / (float) pt->process_count);
}

