class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string temp[s.size()];
        for(int i=0;i<s.size();i++)
        {
            string a;
            for(int j=i;j<s.size();j++)
            {
                bool b = false;
                for(int k=0;k<a.size();k++)
                {
                    if(s[j] == a[k])
                        b = true;
                }
                if(b)
                    break;
                else
                    a+=s[j];
            }
            temp[i] = a;
        }
        int big = 0;
        for(int i=0;i<s.size();i++)
        {
            if(temp[i].size()>big)
                big = temp[i].size();
        }
        return big;
    }
};
