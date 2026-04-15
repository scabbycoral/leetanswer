# 位运算知识点 - 异或性质

：a ^ a = 0 - 找唯一数

：利用 xor - 代码例子

： 

```cpp 
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int x : nums) res ^= x;
    return res;
}
```

