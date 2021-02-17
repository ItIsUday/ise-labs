#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

void first_fit(int *, int *, int, int);
void best_fit(int *, int *, int, int);
void worst_fit(int *, int *, int, int);

int main() {
    int block_count, process_count;
    printf("Enter the number of free blocks: ");
    scanf("%d", &block_count);
    printf("Enter the number of processes: ");
    scanf("%d", &process_count);

    int blocks[block_count];
    int processes[process_count];

    printf("\nEnter the size of the free blocks\n");
    for (int i = 0; i < block_count; i++) {
        printf("Enter the size of block %d: ", i + 1);
        scanf("%d", &blocks[i]);
    }

    printf("\nEnter the size of processes\n");
    for (int i = 0; i < process_count; i++) {
        printf("Enter the size of process %d: ", i + 1);
        scanf("%d", &processes[i]);
    }

    first_fit(blocks, processes, block_count, process_count);
    best_fit(blocks, processes, block_count, process_count);
    worst_fit(blocks, processes, block_count, process_count);

    return 0;
}

void best_fit(int *blocks, int *processes, int block_count, int process_count) {
    printf("\n\t\t\tBEST FIT\n\n");
    int min, index;
    int b[block_count];
    for (int i = 0; i < block_count; i++)
        b[i] = blocks[i];

    printf("Process\tProcess size\tBlock\tHole size\tResidue\n");
    for (int i = 0; i < process_count; i++) {
        printf("P%d\t%d\t\t", i + 1, processes[i]);
        min = INT_MAX, index = -1;
        for (int j = 0; j < block_count; j++) {
            if (b[j] < min && b[j] >= processes[i]) {
                index = j;
                min = b[j];
            }
        }
        if (index != -1) {
            b[index] -= processes[i];
            printf("%d\t%d\t\t%d\n", index + 1, b[index] + processes[i], b[index]);
        } else {
            printf("N/A\tN/A\t\tN/A\n");
        }
    }
}

void worst_fit(int *blocks, int *processes, int block_count, int process_count) {
    printf("\n\t\t\tWORST FIT\n\n");
    int max, index;
    int b[block_count];
    for (int i = 0; i < block_count; i++)
        b[i] = blocks[i];

    printf("Process\tProcess size\tBlock\tHole size\tResidue\n");
    for (int i = 0; i < process_count; i++) {
        printf("P%d\t%d\t\t", i + 1, processes[i]);
        max = INT_MIN, index = -1;
        for (int j = 0; j < block_count; j++) {
            if (b[j] > max && b[j] >= processes[i]) {
                index = j;
                max = b[j];
            }
        }
        if (index != -1) {
            b[index] -= processes[i];
            printf("%d\t%d\t\t%d\n", index + 1, b[index] + processes[i], b[index]);
        } else {
            printf("N/A\tN/A\t\tN/A\n");
        }
    }
}

void first_fit(int *blocks, int *processes, int block_count, int process_count) {
    printf("\n\t\t\tFIRST FIT\n\n");
    int b[block_count];
    bool allocated;
    for (int i = 0; i < block_count; i++)
        b[i] = blocks[i];

    printf("Process\tProcess size\tBlock\tHole size\tResidue\n");
    for (int i = 0; i < process_count; i++) {
        printf("P%d\t%d\t\t", i + 1, processes[i]);
        allocated = false;
        for (int j = 0; j < block_count; j++) {
            if (b[j] >= processes[i]) {
                b[j] -= processes[i];
                allocated = true;
                printf("%d\t%d\t\t%d\n", j + 1, b[j] + processes[i], b[j]);
                break;
            }
        }
        if (!allocated)
            printf("N/A\tN/A\t\tN/A\n");
    }
}
