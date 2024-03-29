#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} node;

typedef struct CircularLL {
    node *head;
} CircularLL;

void input_long_int(CircularLL *);
node *create_node(int);
CircularLL *create_circularll();
void insert_start(CircularLL *, int);
void long_int_view(CircularLL *);
void add_long_int(CircularLL *, CircularLL *, CircularLL *);
void delete_circularll(CircularLL *);

int main() {
    CircularLL *ans, *L1, *L2;
    L1 = create_circularll();
    L2 = create_circularll();
    ans = create_circularll();

    printf("\t\tAddition of long positive integers using circular linked list\n");
    input_long_int(L1);
    input_long_int(L2);

    add_long_int(ans, L1, L2);
    printf("Sum: ");
    long_int_view(ans);

    delete_circularll(L1);
    delete_circularll(L2);
    delete_circularll(ans);
    return 0;
}

void input_long_int(CircularLL *LL) {
    char chr;
    int digit;
    printf("Enter a positive integer addend: ");
    scanf("%1c", &chr);
    while (chr != '\n') {
        if (isdigit(chr) == 0) {
            printf("Invalid input\n");
            delete_circularll(LL);
            exit(1);
        }
        digit = chr - '0';
        insert_start(LL, digit);
        scanf("%1c", &chr);
    }
}

node *create_node(int data) {
    node *temp = (node *) malloc(sizeof(node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

CircularLL *create_circularll() {
    CircularLL *LL = (CircularLL *) malloc(sizeof(CircularLL));
    LL->head = create_node(0);
    LL->head->next = LL->head;

    return LL;
}

void insert_start(CircularLL *LL, int digit) {
    node *new_node = create_node(digit);
    LL->head->data += 1;
    new_node->next = LL->head->next;
    LL->head->next = new_node;
}

void long_int_view(CircularLL *LL) {
    node *temp = LL->head->next;
    while (temp != LL->head) {
        printf("%d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void add_long_int(CircularLL *ans, CircularLL *L1, CircularLL *L2) {
    int carry = 0, sum, digit;
    node *left_over, *last_node;

    if (L1->head->data == 0 && L2->head->data == 0)
        return;
    if (L1->head->data == 0) {
        ans->head = L2->head;
        return;
    }
    if (L2->head->data == 0) {
        ans->head = L1->head;
        return;
    }

    node *p = L1->head->next;
    node *q = L2->head->next;
    while (p != L1->head && q != L2->head) {
        sum = p->data + q->data + carry;
        digit = sum % 10;
        carry = sum / 10;

        insert_start(ans, digit);
        p = p->next;
        q = q->next;
    }

    if (p != L1->head) {
        left_over = p;
        last_node = L1->head;
    } else {
        left_over = q;
        last_node = L2->head;
    }

    while (left_over != last_node) {
        sum = left_over->data + carry;
        digit = sum % 10;
        carry = sum / 10;

        insert_start(ans, digit);
        left_over = left_over->next;
    }

    if (carry)
        insert_start(ans, carry);
}

void delete_circularll(CircularLL *LL) {
    node *next_node = NULL;
    node *current_node = LL->head->next;
    while (current_node != LL->head) {
        next_node = current_node->next;
        free(current_node);
        current_node = next_node;
    }
    free(current_node);
}