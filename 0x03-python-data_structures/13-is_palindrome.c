#include "lists.h"

/**
 * reverse_linked_list - linked list reversed
 * @head: pointer to node
 *
 * Return: pointer to first node
 */
void reverse_linked_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next = NULL;
	listint_t *prev = NULL;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checked a linked list to see if it is palindrome
 * @head: double pointer to list
 *
 * Return: 1 if it is, and returns 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *first_1 = *head, *up = *head, *temp = *head, *duplicate = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		up = up->next->next;
		if (!up)
		{
			duplicate = first_1->next;
			break;
		}
		if (!up->next)
		{
			duplicate = first_1->next->next;
			break;
		}
		first_1 = first_1->next;
	}
	reverse_linked_list(&duplicate);
	while (duplicate && temp)
	{
		if (temp->n == duplicate->n)
		{
			duplicate = duplicate->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!duplicate)
		return (1);

	return (0);
}
