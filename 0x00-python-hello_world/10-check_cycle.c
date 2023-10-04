#include "lists.h"
/**
 *check_cycle - a function to check if ther is a cycle in a linked list
 *@list: The linked list to be checked
 *Return: 0 on not finding a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *node;
listint_t *node_2;

node = list;
node_2 = node;
if (node == NULL || node_2 == NULL)
	return (0);

while (node != NULL && node_2 != NULL && node_2->next != NULL)
{

node_2 = node_2->next->next;
node = node->next;
	if (node == node_2)
	{
		return (1);
	}
}
return (0);
}
