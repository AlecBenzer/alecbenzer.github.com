---
layout: post
title: Double pointers
---

Here's a pretty standard linked-list implementation in C:

{% highlight c %}
typedef struct _node_t {
  int data;
  struct _node_t* next;
} node_t;

typedef struct {
  node_t* head;
} list_t;

void init(list_t* list) {
  list->head = NULL;
}

void append(list_t* list, int data) {
  // corner-case: initially empty list
  if (list->head == NULL) {
    list->head = malloc(sizeof(node_t));
    list->head->data = data;
    list->head->next = NULL;
    return;
  }

  // find the tail
  node_t* node;
  for (node = list->head; node->next != NULL; node = node->next);

  // sad duplication :(
  node->next = malloc(sizeof(node_t));
  node->next->data = data;
  node->next->next = NULL;
}
{% endhighlight c %}

We have to write the code that creates a new node twice to deal with the corner case of appending to an empty list.

We could try abstacting that out:

{% highlight c %}
void create_node(node_t** node, int data) {
  *node = malloc(sizeof(node_t));
  (*node)->data = data;
  (*node)->next = NULL;
}

void append(list_t* list, int data) {
  // corner-case: initially empty list
  if (list->head == NULL) {
    create_node(&list->head, data);
    return;
  }

  // find the tail
  node_t* node;
  for (node = list->head; node->next != NULL; node = node->next);

  create_node(&node->next, data);
}
{% endhighlight %}
