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
	if ((*head)->next == NULL)
	{
		new_node->next = (*head)->next;
		(*head) = new_node;
		return (new_node);
	}
	while (current_node->n <= number)
		current_node = current_node->next;
	new_node->next = current_node;
	current_node = new_node;
	return (new_node);
}
