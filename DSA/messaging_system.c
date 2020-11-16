#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct queue {
    int queue_size, message_size;
    char **messages;
    int front, rear;
};
typedef struct queue Queue;

void create_queue(Queue *, int, int);
bool is_full(Queue *);
bool is_empty(Queue *);
void enqueue(Queue *, char *);
char *dequeue(Queue *);
void display_queue(Queue *);

int main() {
    Queue que;
    int choice;
    int queue_size, max_message_size;

    printf("Enter the size of the queue: ");
    scanf("%d", &queue_size);
    printf("Enter the length of the maximum message: ");
    scanf("%d", &max_message_size);
    max_message_size++;

    char msg[max_message_size];
    create_queue(&que, queue_size, max_message_size);
    printf("\nQueue of size %d created\n", queue_size);

    while (true) {
        printf("\n--------------------------\n");
        printf("1: IsFull\n2: IsEmpty\n3: Display contents\n");
        if (!is_full(&que)) {
            printf("4: Enqueue\n");
            if (!is_empty(&que))
                printf("5: Dequeue\n");
        } else
            printf("4: Dequeue\n");
        printf("-1: Exit\n");
        printf("Select an operation: ");
        scanf("%d", &choice);

        if (is_empty(&que) && choice == 5) {
            printf("Invalid option\n");
            continue;
        }
        if (is_full(&que)) {
            if (choice == 4)
                choice++;
            else if (choice == 5) {
                printf("Invalid option\n");
                continue;
            }
        }

        switch (choice) {
            case 4:
                printf("Enter the message to be enqueued: ");
                getchar();
                scanf("%[^\n]s", msg);
                enqueue(&que, msg);
                display_queue(&que);
                break;
            case 5:
                strcpy(msg, dequeue(&que));
                if (strcmp(msg, ""))
                    printf("The dequeued message is: %s\n", msg);
                display_queue(&que);
                break;
            case 1:
                if (is_full(&que))
                    printf("The queue is full\n");
                else
                    printf("The queue is not full\n");
                break;
            case 2:
                if (is_empty(&que))
                    printf("The queue is empty\n");
                else
                    printf("The queue is not empty\n");
                break;
            case 3:
                display_queue(&que);
                break;
            case -1:
                exit(0);
            default:
                printf("Invalid option\n");
                break;
        }
    }
}

void create_queue(Queue *q, int size, int msize) {
    q->messages = (char **)malloc(size * sizeof(char *));
    for (int i = 0; i < size; i++) {
        q->messages[i] = (char *)malloc(msize * sizeof(char));
    }

    q->queue_size = size;
    q->message_size = msize;
    q->front = -1;
    q->rear = -1;
}

bool is_full(Queue *q) {
    return (q->rear + 1) % q->queue_size == q->front;
}

bool is_empty(Queue *q) {
    return q->front == -1 && q->rear == -1;
}

void enqueue(Queue *q, char *message) {
    if (q->front == -1 && q->rear == -1) {
        q->front = 0;
        q->rear = 0;
    } else if (is_full(q)) {
        printf("QUEUE FULL\n");
        return;
    } else {
        q->rear = (q->rear + 1) % q->queue_size;
    }
    strcpy(q->messages[q->rear], message);
}

char *dequeue(Queue *q) {
    if (is_empty(q)) {
        printf("QUEUE EMPTY\n");
        return "";
    }
    char *message = q->messages[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % q->queue_size;
    }

    return message;
}

void display_queue(Queue *q) {
    if (is_empty(q)) {
        printf("QUEUE EMPTY\n");
        return;
    }
    printf("\nQueue: [");
    int i = q->front;
    while (i != q->rear) {
        printf("\"%s\"", q->messages[i]);
        printf(", ");
        i = (i + 1) % q->queue_size;
    }
    printf("\"%s\"]\n", q->messages[q->rear]);
}