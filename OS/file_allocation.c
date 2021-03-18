#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Memory {
    int block_count;
    int block_size;
    int *arr;
} Memory;

typedef struct Files {
    int file_count;
    int *file_sizes;
} Files;

Memory *initialize();
Files *get_files_data();
int file_size_to_blocks(Memory *, int);
void wipe_memory(Memory *);
void sequential(Memory *, Files *);
void linked(Memory *, Files *);
void indexed(Memory *, Files *);

int main() {
    printf("\t\tFile allocations\n");
    Memory *memory = initialize();
    printf("Storage capacity: %dKB\n", memory->block_size * memory->block_count);
    Files *files = get_files_data();

    sequential(memory, files);
    wipe_memory(memory);
    linked(memory, files);
    wipe_memory(memory);
    indexed(memory, files);
    wipe_memory(memory);
}

Memory *initialize() {
    Memory *memory = (Memory *) malloc(sizeof(Memory));
    printf("Enter the number of blocks: ");
    scanf("%d", &memory->block_count);
    printf("Enter the block size (in KB): ");
    scanf("%d", &memory->block_size);

    memory->arr = (int *) malloc(memory->block_count * sizeof(int));
    for (int i = 0; i < memory->block_count; i++)
        memory->arr[i] = -1;

    return memory;
}

int file_size_to_blocks(Memory *mem, int file_size) {
    int blocks_needed = file_size / mem->block_size;
    if (file_size * 1.0 / mem->block_size != blocks_needed)
        blocks_needed++;
    return blocks_needed;
}

void wipe_memory(Memory *mem) {
    for (int i = 0; i < mem->block_count; i++)
        mem->arr[i] = -1;
}

Files *get_files_data() {
    Files *files = (Files *) malloc(sizeof(Files));
    printf("Enter the number of files: ");
    scanf("%d", &files->file_count);
    files->file_sizes = (int *) malloc(files->file_count * sizeof(int));

    for (int i = 0; i < files->file_count; i++) {
        printf("Enter the size of file %d (in KB): ", i + 1);
        scanf("%d", &files->file_sizes[i]);
    }

    return files;
}

int get_free_block(Memory *mem) {
    bool seen[mem->block_count], is_all_seen = false;
    int index;

    for (int i = 0; i < mem->block_count; i++)
        seen[i] = false;

    while (!is_all_seen) {
        index = rand() % mem->block_count;
        if (mem->arr[index] == -1)
            return index;
        seen[index] = true;

        is_all_seen = seen[0];
        for (int i = 1; i < mem->block_count; i++)
            is_all_seen = seen[i] && is_all_seen;
    }

    return -1;
}

void sequential(Memory *mem, Files *files) {
    printf("\nSequential file allocation\n");
    int blocks_needed, free_blocks, j;
    bool allocated;

    for (int i = 0; i < files->file_count; i++) {
        blocks_needed = file_size_to_blocks(mem, files->file_sizes[i]);
        allocated = false;
        free_blocks = 0;
        j = 0;
        printf("\tFile %d: ", i + 1);
        while (j < mem->block_count) {
            if (mem->arr[j] == -1) {
                j++;
                free_blocks++;
            } else {
                j += file_size_to_blocks(mem, files->file_sizes[mem->arr[j]]);
                free_blocks = 0;
            }
            if (free_blocks == blocks_needed) {
                mem->arr[j - free_blocks] = i;
                allocated = true;
                break;
            }
        }
        if (allocated) {
            printf("Allocation successful, used %d blocks and they are: ", blocks_needed);
            for (int k = 0; k < blocks_needed; k++)
                printf("%d ", j - blocks_needed + k);
            printf("\n");
        } else
            printf("Allocation failed\n");
    }
}

void linked(Memory *mem, Files *files) {
    printf("\nLinked file allocation\n");
    int blocks_needed, *blocks;
    bool allocation_possible;

    for (int i = 0; i < files->file_count; i++) {
        blocks_needed = file_size_to_blocks(mem, files->file_sizes[i]);
        allocation_possible = true;
        blocks = (int *) malloc(blocks_needed * sizeof(int));
        printf("\tFile %d: ", i + 1);

        for (int j = 0; j < blocks_needed; j++) {
            blocks[j] = get_free_block(mem);
            if (blocks[j] == -1) {
                allocation_possible = false;
                for (int k = 0; k < j; k++)
                    mem->arr[blocks[k]] = -1;
                break;
            }
            mem->arr[blocks[j]] = -2;
        }
        if (allocation_possible) {
            printf("Allocation successful, used %d blocks and they are: ", blocks_needed);
            for (int j = 0; j < blocks_needed - 1; j++)
                printf("%d->", blocks[j]);
            printf("%d\n", blocks[blocks_needed - 1]);
        } else
            printf("Allocation failed\n");
        free(blocks);
    }
}

void indexed(Memory *mem, Files *files) {
    printf("\nIndexed file allocation\n");
    int blocks_needed, **file_blocks;
    bool allocation_possible;
    file_blocks = (int **) malloc(files->file_count * sizeof(int *));

    for (int i = 0; i < files->file_count; i++) {
        allocation_possible = true;
        blocks_needed = file_size_to_blocks(mem, files->file_sizes[i]) + 1;
        file_blocks[i] = (int *) malloc(blocks_needed * sizeof(int));
        printf("\tFile %d: ", i + 1);

        for (int j = 0; j < blocks_needed; j++) {
            file_blocks[i][j] = get_free_block(mem);
            if (file_blocks[i][j] == -1) {
                allocation_possible = false;
                for (int k = 0; k < j; k++)
                    mem->arr[file_blocks[i][k]] = -1;
                break;
            }
            if (j == 0)
                mem->arr[file_blocks[i][j]] = i;
            else
                mem->arr[file_blocks[i][j]] = -2;
        }
        if (allocation_possible) {
            printf("Allocation successful, used %d blocks and they are: ", blocks_needed);
            printf("%d->(", file_blocks[i][0]);
            for (int j = 1; j < blocks_needed - 1; j++)
                printf("%d ", file_blocks[i][j]);
            printf("%d)\n", file_blocks[i][blocks_needed - 1]);
        } else
            printf("Allocation failed\n");
    }
}
