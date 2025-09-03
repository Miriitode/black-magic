#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <time.h>
#include <limits.h>

typedef struct TreapNode {
    int val;
    uint64_t prio;
    struct TreapNode *l;
    struct TreapNode *r;
} TreapNode;


typedef struct Set {
    struct TreapNode *bst;
    uint32_t size;
} Set;


/*
split
merge
insert
remove
*/

uint64_t rand_prio() {
    uint64_t res = 0;
    for (int i = 0; i < 4; i++) {
        res = (res << 15) ^ rand();
    }
    res = (res << 4) ^ (rand() % 16);
    return res;
}

void shuffle(int *array, size_t n) {
    // https://stackoverflow.com/questions/6127503/shuffle-array-in-c
    if (n > 1) {
        size_t i;
        for (i = 0; i < n - 1; i++) {
          size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
          int t = array[j];
          array[j] = array[i];
          array[i] = t;
        }
    }
}

TreapNode *make_node(int v) {
    TreapNode *t = (TreapNode*) malloc(sizeof(TreapNode));
    t->val = v;
    t->prio = rand_prio();
    t->l = t->r = NULL;
    return t;
}

bool t_contains(TreapNode *t, int val) {
    if (t == NULL) {
        return false;
    }
    else if(val < t->val) {
        return t_contains(t->l, val);
    }
    else if(val > t->val) {
        return t_contains(t->r, val);
    }
    else {
        return true;
    }
}

int t_height(TreapNode *t) {
    if (t == NULL) {
        return 0;
    }
    int left = 1 + t_height(t->l);
    int right = 1 + t_height(t->r);
    if (left > right) {
        return left;
    }
    else {
        return right;
    }
}

void t_split(TreapNode *t, int x, TreapNode **l, TreapNode **r) {
    // l contains x_i < x, r contains x_i >= x
    if (t == NULL) {
        *l = *r = NULL;
        return;
    }
    else if (x < t->val) {
        *r = t;
        t_split(t->l, x, l, &(t->l)); 
        return;
    }
    else if (x > t->val) {
        *l = t;
        t_split(t->r, x, &(t->r), r);
        return;
    }
    else { // x == t->val
        *l = t->l;
        *r = t;
        assert(t != NULL && x == t->val);
        t->l = NULL;
        return;
    }
}

TreapNode *t_merge(TreapNode *l, TreapNode *r) {
    // assume all x_i in l < all x_i in r
    if (l == NULL) {
        return r;
    }
    else if (r == NULL) {
        return l;
    }
    else if (l->prio > r->prio) {
        l->r = t_merge(l->r, r);
        return l;
    }
    else {
        r->l = t_merge(l, r->l);
        return r;
    }
}


TreapNode *t_insert(TreapNode *t, int val) {
    // assumes t does not contain val
    TreapNode *l = NULL;
    TreapNode *r = NULL;
    TreapNode *n = make_node(val);
    t_split(t, val, &l, &r);
    return t_merge(l, t_merge(n, r));
}


TreapNode *t_remove(TreapNode *t, int val) {
    // assumes val is in t
    if (val == t->val) {
        TreapNode *nt = t_merge(t->l,  t->r);
        free(t);
        return nt;
    }
    else if(val < t->val) {
        t->l = t_remove(t->l, val);
        return t;
    }
    else {
        t->r = t_remove(t->r, val);
        return t;
    }
}

Set *s_create() {
    Set *s = (Set*) malloc(sizeof(Set));
    s->bst = NULL;
    s->size = 0;
    return s;
}


bool s_contains(Set *s, int val) {
    return t_contains(s->bst, val);
}


bool s_add(Set *s, int val) {
    if (s_contains(s, val)) {
        return false;
    }
    else {
        s->bst = t_insert(s->bst, val);
        s->size++;
        return true;
    }
}


bool s_remove(Set *s, int val) {
    if (s_contains(s, val)) {
        s->bst = t_remove(s->bst, val);
        s->size--;
        return true;
    }
    else {
        return false;
    }
}


int s_height(Set *s) {
    return t_height(s->bst);
}


int main() {
    srand(time(NULL));
    const int ARR_SIZE = 10000;
    int arr[ARR_SIZE];
    for(int i = 0; i < ARR_SIZE; i++) {
        arr[i] = i + 1;
    }
    // shuffle(arr, ARR_SIZE);
    Set *s1 = s_create();
    for(int i = 0; i < ARR_SIZE; i++) {
        bool yes = s_add(s1, arr[i]);
        if (!yes) {
            printf("failed to add element %d to set\n", arr[i]);
            // this will print if there is an error
        }
    }
    printf("Set size: %d\n", s1->size);
    printf("BST height: %d\n", s_height(s1));
    for(int i = 0; i < ARR_SIZE; i++) {
        bool yes = s_remove(s1, arr[i]);
        if (!yes) {
            printf("failed to remove element %d from set\n", arr[i]);
            // this will print if there is an error
        }
    }

    return 0;
}