#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: points to head node
 * @number: integer
 *
 * Return: address of new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr;
	listint_t *new;
	listint_t *prev;

	curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (curr != NULL)
	{
		if (curr->n > number)
			break;
		prev = curr;
		curr = curr->next;
	}

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = curr;
		if (curr == *head)
			*head = new;
		else
			prev->next = new;
	}

		return (new);
}
