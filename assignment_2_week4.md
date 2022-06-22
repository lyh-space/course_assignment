题目一：以下是用于计算圆周率的程序。程序中，用到了求解公式“π/4=1-1/3+1/5-1/7+...”，循环求解到最后一项的绝对值小于0.00001。请先测试程序准确无误，再将其中的for循环改成while循环。  
```c++
#include <stdio.h> 
#include<math.h>
#define N 1000000

void main( ) 
{
    int i; 
    double pi, ifloat, dpi;
    pi = 1.0;
    for(i = 1; i < N; i++)
    {
        dpi = 1.0 / (2.0 * i + 1.0);
	    if(dpi < 0.00001) break;
	    printf("增量=%13.10f pi=%13.10f\n", dpi, 4.0 * pi);
	    pi = pi + pow(-1.0, i) * dpi;
    }
    printf("pi=%f\n", 4.0 * pi);
}
```
原题目中给的代码包含了很多c语言的风格，下面的代码我将采用c++风格。     
code：  
```c++
#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int i = 1;
    double pi = 1.0, dpi = 1.0 / 3.0;
    while(dpi >= 0.00001)
    {
        dpi = 1.0 / (2.0 * i + 1.0);
        cout <<"增量=" << fixed << setw(13) <<setprecision(10) << dpi;
        cout <<" pi=" << fixed << setw(13) <<setprecision(10) << (4.0 * pi) << endl;
        //在这里为了体现c++风格使用了流操纵算子进行格式化输出
        //但实际上在此处使用格式化输出函数printf()更为方便：
        //printf("增量=%13.10f pi=%13.10f\n", dpi, pi*4.0)
        pi = pi + pow(-1.0, i) * dpi;
        i++;
    }
    cout << "pi=" << ((pi + pow(-1.0, i) * dpi) * 4.0) << endl;
    //由于在while循环中达到精度要求后pi又进行了一步运算，因此最后输出时减去该步运算

    cin.get();
    return 0;
} 
```

题目二：请写一个程序，输出所有这样的三位数，它们等于它们的各位数字的立方和。例如：  
153=13+53+33。  

code：  
```c++
#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int hun, ten, ind, n;
    for(n = 100; n < 1000; n++>)
    {
        hun = 0 / 100;
        ten = (n - hun * 100) / 10;
        ind = n % 10;
        if(n == pow(hun, 3) + pow(ten, 3) + pow(ind, 3))
            cout << n << endl;
    }

    cin.get();
    return 0;
}
```

题目三：输入N个整数，输出其中最大数和最小数（它们共占一行）。   

code:  
```c++
#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int i, j, n, max, min;

    //读取数值
    cout << "请输入n的值：" << endl;
    cin >> n;
    int number[n];
    for(i = 0; j < n; i++)
    {
        cout << "请输入第" << (i + 1) <<"个数：";
        cin >> number[i];
    }

    //比较大小
    max = min = number[0];
    for(j = 0; j < n; j++)
    {
        if(number[j] > max)
            max = number[j];
        if(number[j] < min)
            min = number[j];
    }

    cout << "最大值为" << max << ", 最小值为" << min << endl;

    cin.get();
    return 0;
}
```
