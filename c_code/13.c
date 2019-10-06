#include <stdio.h>
#define A "宏定义"
#define PI 3.14159

void main(){
	const int a = 10; //const限定符
	printf("%s\n", A);
	float area,circum,radius;
	printf("What is the radius of your pizza?\n");
	scanf("%f",&radius);
	area = PI * radius * radius;
	circum = 2.0 * PI * radius;
	printf("Your basic pizza parameters are as follows:\n");
	printf("circumference = %1.2f, area = %1.2f\n", circum,area);
}