#include "lists.h"

/**
 * insert_node - inserts a node to a sorted list
 *
 * @head: pointer to the head node
 *
 * @number: data of the node to be add
 *
 * Return: the pointer to the added node
 * or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	new_node->n = number;
	new_node->next = NULL;

	current_node = (*head);
	if ((*head) == NULL) /* means head points to null and no list exist yet */
	{
		(*head) = new_node;
		return (new_node);
	}
	if ((*head)->n > number) /*check if first node data is greater than new node data */
	{ /* if it is point new_node link to head pointer
	     then point head to new =_node link */
		new_node->next = (*head);
		(*head) = new_node;
		return (new_node);
	}
	while (current_node->next != NULL && current_node->next->n <= number) /* find fit position */
		current_node = current_node->next;
	/* point new_node to the node that contains a higher data
	 * then point the current node link to new_node */
	new_node->next = current_node->next;
	current_node->next = new_node;
	return (new_node);
}
