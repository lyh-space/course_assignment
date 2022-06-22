误差函数（也称之为高斯误差函数，error function or Gauss error function）是一个非基本函数（即不是初等函数），其在概率论、统计学以及偏微分方程中都有广泛的应用。它的表达式为
<img src="https://latex.codecogs.com/svg.image?\operatorname{erf}(x)=\frac{2}{\sqrt{\pi}}&space;\int_{0}^{x}&space;e^{-\eta^{2}}&space;d&space;\eta" title="https://latex.codecogs.com/svg.image?\operatorname{erf}(x)=\frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-\eta^{2}} d \eta" />  
请用C++编程，输出[-2, 2]区间误差函数的值。

## 1.问题分析
以上误差函数的定义式包含一个积分，不利于编程。我们将它转换成级数表达式  
<img src="https://latex.codecogs.com/svg.image?\operatorname{erf}(x)=\frac{2}{\sqrt{\pi}}&space;\sum_{n=0}^{\infty}(-1)^{n}&space;\frac{x^{2&space;n&plus;1}}{n&space;!(2&space;n&plus;1)}" title="https://latex.codecogs.com/svg.image?\operatorname{erf}(x)=\frac{2}{\sqrt{\pi}} \sum_{n=0}^{\infty}(-1)^{n} \frac{x^{2 n+1}}{n !(2 n+1)}" />  
我们将问题分为两部分：误差函数迭代求解与误差函数的输出。其中，误差函数级数中有阶乘与幂次方表达式，又可被编程成两个独立的函数。课本已经有阶乘与幂次方的函数，如下

```cpp
#include <iostream>
using namespace std;
const double sqrt_PI=1.77245385; //sqrt_PI是PI的开方
double factorial(long int n)
{
	double f=1.0;
	for(int i=2;i<=n; i++)f *= (double)i;
	return f;
}
double power(double x, int n)
{
	if (x == 0.) return 0.;
	double product=1.;
	if (n >= 0)
		while (n > 0){ product *= x;n--;}
	else
		while (n < 0){product /= x;n++;}
	return product;
}
void main()
{
}

```

## 2.误差函数迭代求解

仿照以上两个函数的结构，添加一个函数计算erf(x)。可参考以下流程图，写成do-while循环。其中步骤“用n求addf”需要调用阶乘函数与幂次方函数。

![](https://i.bmp.ovh/imgs/2022/03/47865a898370f0ea.png)


## 3.误差函数的输出

参考以下流程图，写一个循环for循环输出x与erf(x)。

![](https://i.bmp.ovh/imgs/2022/03/0062b7085ee4c341.png)

## 完整源代码
```cpp
#include<iostream>
#include<iomanip> //该头文件用于流操纵算子
#include<cmath>
using namespace std;

const double sqrt_PI=1.77245385; //sqrt_PI是PI的开方

//阶乘函数
double factorial(long int n)
{
	double f=1.0;
	for(int i=2;i<=n; i++)f *= (double)i;
    // (double)i是C语言的风格，意为将int型的i强制转换为double型，C++风格写为double (i)
	return f;
}

//幂函数
double power(double x, int n)
{
	if (x == 0.) return 0.;
	double product=1.;
	if (n >= 0)
		while (n > 0){ product *= x;n--;}
	else
		while (n < 0){product /= x;n++;}
	return product;
}

//误差迭代函数
double erf(double x)
{
    int n = 0;
    double f = 0;
    double addf;
    do
    {
        addf = power(-1, n) * power(x, 2 * n + 1) / (factorial(n) * (2 * n + 1));
        f += addf;
        addf = fabs(addf);
        n++;
    } while (addf > 10e-6);
    return 2 / sqrt_PI * f;
}

int main()
{
    for(int i = -20; i <= 20; i++)
    {
        double x = 0.1 * double (i);
        double f = erf(x);
        cout << fixed << setprecision(1) << setw(4) << x << "   ";
        cout << fixed << setprecision(6) << setw(9) << f << endl;
        //此处使用流操纵算子进行格式化输出，需要<iomanip>头文件
        //如果不想用流操纵算子，可以使用 C 风格的格式化输出函数 printf() 进行格式化输出
        //如果不在意输出结果是否美观，可以不使用格式化输出，直接用：cout << x << "  " << f << endl;
    }
    return 0;
}
```

输出结果为：

```
输出结果为：
//其中第二列为自定义函数的输出，第三列为标准库中的erf()函数的输出
-2.0   -0.995322   -0.995322
-1.9   -0.992791   -0.992790
-1.8   -0.989090   -0.989091
-1.7   -0.983789   -0.983790
-1.6   -0.976348   -0.976348
-1.5   -0.966105   -0.966105
-1.4   -0.952285   -0.952285
-1.3   -0.934008   -0.934008
-1.2   -0.910313   -0.910314
-1.1   -0.880206   -0.880205
-1.0   -0.842701   -0.842701
-0.9   -0.796908   -0.796908
-0.8   -0.742101   -0.742101
-0.7   -0.677801   -0.677801
-0.6   -0.603856   -0.603856
-0.5   -0.520500   -0.520500
-0.4   -0.428392   -0.428392
-0.3   -0.328627   -0.328627
-0.2   -0.222703   -0.222703
-0.1   -0.112463   -0.112463
0.0    0.000000    0.000000
0.1    0.112463    0.112463
0.2    0.222703    0.222703
0.3    0.328627    0.328627
0.4    0.428392    0.428392
0.5    0.520500    0.520500
0.6    0.603856    0.603856
0.7    0.677801    0.677801
0.8    0.742101    0.742101
0.9    0.796908    0.796908
1.0    0.842701    0.842701
1.1    0.880206    0.880205
1.2    0.910313    0.910314
1.3    0.934008    0.934008
1.4    0.952285    0.952285
1.5    0.966105    0.966105
1.6    0.976348    0.976348
1.7    0.983789    0.983790
1.8    0.989090    0.989091
1.9    0.992791    0.992790
2.0    0.995322    0.995322

```
