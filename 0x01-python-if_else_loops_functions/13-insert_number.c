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

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < temp->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	else
	{
		while (temp->next->n <= number && temp->next)
			temp = temp->next;
		if (temp->next->n >= number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
	}

		return (NULL);
}
