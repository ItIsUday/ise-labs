#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t seat;
sem_t chopstick[5];

void *live_life(void *person) {
    int philosopher = *(int *) person;

    sem_wait(&seat);
    printf("Philosopher %d has taken seat\n", philosopher);
    sem_wait(&chopstick[philosopher]);
    sem_wait(&chopstick[(philosopher + 1) % 5]);

    printf("Philosopher %d started eating\n", philosopher);
    sleep(1);

    sem_post(&chopstick[(philosopher + 1) % 5]);
    sem_post(&chopstick[philosopher]);
    sem_post(&seat);

    printf("Philosopher %d finished eating and is now thinking\n", philosopher);
    sleep(1);

    return NULL;
}

int main() {
    int i, philosophers[5];
    pthread_t threads[5];
    printf("\t\tDining Philosophers problem using semaphores\n");

    sem_init(&seat, 0, 4);
    for (i = 0; i < 5; i++)
        sem_init(&chopstick[i], 0, 1);

    for (i = 0; i < 5; i++) {
        philosophers[i] = i;
        pthread_create(&threads[i], NULL, live_life, (void *) &philosophers[i]);
    }
    for (i = 0; i < 5; i++)
        pthread_join(threads[i], NULL);

    sem_destroy(&seat);
    for (i = 0; i < 5; i++)
        sem_destroy(&chopstick[i]);
}
