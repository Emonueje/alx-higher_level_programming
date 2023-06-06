#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - function that checks if
 * a singly linked list has a cycle in it.
 *
 * @list: pointer to the singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_node, *fast_node;

	slow_node = list;
	fast_node = list;

	while (slow_node && fast_node && fast_node->next)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;
		if (slow_node == fast_node)
			return (1);
	}
	return (0);
}
