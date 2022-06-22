题目一：分别使用 puts, printf, cout 函数输出如下图案  
```
******************  
***How are you?***
******************  
```
code:  
```cpp
#include<iostream>
#include<cstdio>
using namespace std;

int main() 
{ 
    // puts 函数
    puts("******************");
    puts("***How are you?***");
    puts("******************");
    
    // printf 函数
    printf("******************\n");
    printf("***How are you?***\n");
    printf("******************\n");
    
    // cout 对象
    cout << "******************" << endl;
    cout << "***How are you?***" << endl;
    cout << "******************" << endl;
    
    return 0;
}
```
一些说明：  
* `iostream`标准库中提供了`cout`的输出方法，`cstdio`标准库提供了`puts`和`printf`函数；
* `cstdio`库是将C语言中`stdio.h`头文件转为C++风格，二者完全等同；
* 有些IDE的编译环境会默认自动将`stdio.h`连接到源代码中，但是还是推荐自己在代码中写上；
* `printf`函数需要手动加上换行符`\n`才会换行，`puts`函数不需要加换行符，会自动换行。
    
    
题目二：定义一整数a和一双精度实数b，分别用函数scanf及cin从键盘输入这两数的值，用printf及cout从屏幕输出两数值，并输出两数所占存储空间大小（sizeof函数），达到如下效果：
```
Please input the values
键盘输入 1 2.3
a = 1, b = 2.300000
Size of a is: 4, Size of b is: 8
```
code:  
```cpp
#include<iostream>
#include<cstdio>
using namespace std;

int main() 
{ 
    int a;
    double b;
    
    // printf & scanf 
    printf("Please input the values\n");
    scanf("%d %lf",&a,&b);
    printf("a = %d, b = %lf\n",a,b);
    printf(“Size of a is: %lu, Size of b is: %lu\n",sizeof(a),sizeof(b));
    
    // cout & cin
    cout<<"Please input the values"<<endl;
    cin>>a>>b;
    cout<<"a = "<<a<<", b = "<<b<<endl;
    cout<<"Size of a is: "<<sizeof(a)<<", Size of b is: "<<sizeof(b)<<endl;

    return 0;
} 
```
  
  
题目三：从键盘输入圆的半径值，计算圆的面积和周长，并从屏幕输出。使用常量定义方法 define及scanf,printf/cin,cout, 效果如下：
```
Please input the radius
键盘输入 2
area = 12.566370, circumference = 12.566370
```
code:
```cpp
#include<iostream>
#include<cstdio>
#define PI 3.1415926
using namespace std;

int main() 
{ 
    double r,area,circumference;
    
    // printf & scanf 
    printf("Please input the radius\n");
    scanf("%lf",&r);
    area = PI*r*r;
    circumference = 2.0*PI*r;
    printf("area = %lf, circumference = %lf\n",area,circumference);
    
    // cout & cin
    cout<<"Please input the radius"<<endl;
    cin>>r;
    area = PI*r*r;
    circumference = 2.0*PI*r;
    cout<<"area = "<<area<<", circumference = "<<circumference<<endl;
    
    return 0;
}
```
注意：使用`#define`定义常数时，后面不需要加分号（;）
