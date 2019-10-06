#include <stdio.h>
#include <string.h>

int main(){
	long long int v7;
	char v8[] = ":\"AL_RT^L*.?+6/46";

	v7 = 28537194573619560LL;
	int i;
	for ( i = 0; i < strlen(v8); ++i ){
		char a = (char)(*((unsigned char *)&v7 + i % 7) ^ v8[i]);
		printf("%c",a);
	}
	
	return 0;
}
