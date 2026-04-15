# 位运算核心知识点 

## 基础性质 

异或（XOR）核心特性：a ^ a = 0，a ^ 0 = a，可用于快速去重 Fig1

与运算（AND）：a & 1 可判断奇偶性（1为奇数，0为偶数） Fig2 

或运算（OR）：a | b 可用于置位（将指定位设为1） Fig3 

## ## 经典应用 

1. 寻找数组中唯一出现一次的数字（其他数字出现两次） Fig4 

2. 不使用临时变量交换两个整数 Fig5 

3. 计算一个数的二进制中1的个数（高效写法） Fig6 

```cpp 
// Fig1：异或核心性质示例 
#include <iostream> 
using namespace std; 
int main() {
	int a = 5; // 二进制 101    
	cout << (a ^ a) << endl; // 输出 0    
	cout << (a ^ 0) << endl; // 输出 5    
	return 0; 
}
```
```cpp

// Fig2：与运算判断奇偶性 

bool isOdd(int x) {    

	return x & 1; // 1: 奇数，0: 偶数 

}

```

```cpp
// Fig3：或运算置位（将第3位设为1，从0开始计数）
int setBit(int x) {
    return x | (1 << 3); // 1<<3 是 8（二进制 1000）
}
```

```cpp
// Fig4：寻找唯一出现一次的数字
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int x : nums) {
        res ^= x; // 异或抵消，最终剩下唯一数
    }
    return res;
}
```

```cpp
// Fig5：不使用临时变量交换两个整数
void swap(int &a, int &b) {
    a ^= b;
    b ^= a;
    a ^= b;
}
```

