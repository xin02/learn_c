#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(){
	printf("Some number limits for this system:\n");
	printf("Biggest int: %d\n", INT_MAX);// int类型的最大值
	printf("Smallest long long: %lld\n", LLONG_MIN);//long long最小值
	printf("One byte = %d bits on this system.\n", CHAR_BIT);//char类型位数
	printf("Largest double: %e\n", DBL_MAX);//double类型的最大值
	printf("Smallest normal float: %e\n", FLT_MIN);//float类型的最大值
	printf("float precision = %d digits\n", FLT_DIG);//float类型最少有效数字位数
	printf("float epsilon = %e\n", FLT_EPSILON);//1.00和比1.00大的最小float类型值之间的差值
	return 0;
}