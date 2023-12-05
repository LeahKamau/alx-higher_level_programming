#include "lists.h"

/**
 * is_palindrome - checks if a singly linked
 * list is a plaindrome
 * @head: pointer to head node
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int *ptr, i = 0, j;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	curr = *head;
	while (curr)
	{
		i++;
		curr = curr->next;
	}
	ptr = malloc(sizeof(int) * i);
	curr = *head;
	for (j = 0; j < i; j++)
	{
		ptr[j] = curr->n;
		curr = curr->next;
	}
	curr = *head;
	i--;
	while (curr)
	{
		if (curr->n != ptr[i])
		{
			free(ptr);
			return (0);
		}
		i--;
		curr = curr->next;
	}
	free(ptr);
	return (1);
}
