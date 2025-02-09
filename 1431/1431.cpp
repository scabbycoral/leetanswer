// C++ file for number 1431 
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies) {
        int k = ranges::max(candies) - extraCandies;
        vector<bool> ans;
        ans.reserve(candies.size()); // 预分配空间
        for (int c : candies) {
            ans.push_back(c >= k);
        }
        return ans;
    }
};