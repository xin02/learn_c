#include <stdio.h>

int main(){
	printf("已经处理了:");
	int i;
	for(i = 1; i <= 100; i++) {
		if(i==1){
			//数字占3格，%占一格
			printf("%3d%%",i);
		}else{
			//退4格
			printf("\b\b\b\b%3d%%",i);
		}
		//即时标准输出(不带\n，不刷新不行)
		fflush(stdout);
		//延时10000微妙 = 10豪秒 = 0.01 秒
		//usleep(10000);
		//延时模拟
		int times = 10000000;
		while(times-->0){
			
		} 
	}
	return 1;
}