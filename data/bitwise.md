# 位运算核心知识点 

## 基础性质 

异或（XOR）核心特性：a ^ a = 0，a ^ 0 = a，可用于快速去重 Fig1

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

hdawohodh

dhiwaiodjoiajwd

dhwoauhdoawd

hdouiwahduaw

hugehauo

huiofwaho

hugawh

hoigwahgohwa

hoawhgohawogh

oghaowh

与运算（AND）：a & 1 可判断奇偶性（1为奇数，0为偶数） Fig2 

```cpp

// Fig2：Codeforces 典型优化示例（快速读入，避免超时）
#include <iostream>
using namespace std;

// 快速读入模板（CF中大数据量必备）
inline int read() {
    int x = 0, f = 1;
    char ch = getchar();
    while (ch < '0' || ch > '9') {
        if (ch == '-') f = -1;
        ch = getchar();
    }
    while (ch >= '0' && ch <= '9') {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}

int main() {
    int n = read();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += read();
    }
    cout << sum << endl;
    return 0;
}
```

dawhfhaoifhoiwahf

fiawfjawjfgiwafa

gioawghjiaoga



owiaghjagw

a

wgiawgoha

oghiwaogha

wghiwagh

aowgh



或运算（OR）：a | b 可用于置位（将指定位设为1） Fig3 

```cpp
// Fig3：边界案例测试示例（数组为空）
vector<int> getMin(vector<int>& nums) {
    if (nums.empty()) { // 边界案例：空数组
        return {};
    }
    int minVal = nums[0];
    for (int x : nums) {
        if (x < minVal) minVal = x;
    }
    return {minVal};
}
```

ghuaghuawg

aghuwa

ghawghwa

ghua

ogha

ghawghawhogha

oghuw

ghawhoa



## ## 经典应用 

1. 寻找数组中唯一出现一次的数字（其他数字出现两次） Fig4 

   ```cpp
   // Fig4：极端值测试（int最大值）
   #include <climits>
   
   int add(int a, int b) {
       // 避免溢出（极端值案例）
       if (b > 0 && a > INT_MAX - b) {
           return INT_MAX; // 溢出处理
       }
       if (b < 0 && a < INT_MIN - b) {
           return INT_MIN;
       }
       return a + b;
   }
   
   ```

   fhawofhaofh

   awf

   oawhf

   owafhawf

   hoahfoihwaf

   oawfioh

   aofhoafhu

   iowahfaowiufh

   awoh

2. 不使用临时变量交换两个整数 Fig5 

   ```cpp
   // Fig5：时间复杂度优化（O(n^2) → O(n)）
   // 原O(n^2)：寻找数组中两数之和等于target
   // 优化后O(n)：用哈希表存储已遍历元素
   vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<int, int> mp;
       for (int i = 0; i < nums.size(); i++) {
           if (mp.count(target - nums[i])) {
               return {mp[target - nums[i]], i};
           }
           mp[nums[i]] = i;
       }
       return {};
   }
   ```

   fwahufhaw

   faf

   awfauwfhauowf

   afhawhfoa

   whfhwafo

   awhfowafhoawfhu

   awfhwau

   fhaoufhafhwuo

   a

3. 计算一个数的二进制中1的个数（高效写法） Fig6 





