#cpp的string是可变元素，可以将本题的空间复杂度降为O(1)
class Solution {
public:
    string pathEncryption(string path) {
        /*originalLength 为字符串str的实际长度*/
        int originalLength = path.size();
        int numberOfBlank = 0;
        for(int i=0;i<path.size();i++)
        {

            if(path[i] == '.')
                ++ numberOfBlank;

        }

        /*newLength 为把空格替换成'%20'之后的长度*/
        int newLength = originalLength;

        int indexOfOriginal = originalLength;
        int indexOfNew = newLength;

        while(indexOfOriginal >= 0)
        {
            if(path[indexOfOriginal] == '.')
            {
                path[indexOfNew --] = ' ';
            }
            else
            {
                path[indexOfNew --] = path[indexOfOriginal];
            }

            -- indexOfOriginal;
        }
        return path;
    }
};
#里面的参数都有其含义，可以通过修改长度或者参数以达到用xxx替换yy的目的
#如果xxx和yy长度不一样，说明新旧string长度不一样，while循环需要增加判断new和original的大小，比如xx替换y，需要增加&& new>original，和path[indexOfNew--]=''