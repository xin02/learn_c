#include <stdio.h>
#include <inttypes.h>

int main(){
	int32_t me32;
	me32 = 45933945;
	printf("First, assume int32_t is int:\n");
	printf("me32 = %d\n", me32);
	printf("Next, let's not make any assumptions.\n");
	printf("Instead,use a \"macro\" from inttypes.h\n:");
	printf("me32 = %" PRId32 "\n", me32);

	return 0;
}