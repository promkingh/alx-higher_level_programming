#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 *
 * Return: (1) if there is a cycle and (1) otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
