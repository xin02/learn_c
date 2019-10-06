#include <stdio.h>

int main(){
	char ch;
	_Bool a = true;
	printf("Please enter a character.\n");
	scanf("%c",&ch);
	printf("The code for %c in %#x.\n", ch,ch);
	if (a)
	{
		printf('a');
	}
	return 0;
}