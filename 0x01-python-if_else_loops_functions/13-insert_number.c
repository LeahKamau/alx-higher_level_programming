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
	listint_t *temp;
	listint_t *new;

	if (*head == NULL)
		return (NULL);

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (temp->next->n < number && temp)
		temp = temp->next;
	if (temp->next->n > number)
	{
		new->next = temp->next;
		temp->next = new;
		return (new);
	}

	return (NULL);
}
