#include <stdio.h>

void main(){
	/*
		short int 短整型
		long int 长整型
		long long int 双长整型
		unsigned int 无符号
		signed int 有符号
		%u 无符号整型占位符
		float、double
	*/
	int x = 100;
	printf("dec = %d; octal = %o; hex = %X\n",x,x,x);
	printf("dec = %#d; octal = %#o; hex = %#X\n",x,x,x);
}