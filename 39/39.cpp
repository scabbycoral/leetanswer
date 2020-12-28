class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> mid_vector;
        vector<vector<int>> result;
        solve(candidates, 0, 0, target, mid_vector, result);
        return result;
}

    void solve(vector<int>& candidates, int mid_target, int index, int target, vector<int>& mid_vector, vector<vector<int>>& result) {
        if (mid_target == target) {
            result.push_back(mid_vector);
            return;
        }
        if (mid_target > target) {
            return;
        }
        for (int i = index; i < candidates.size(); i++) {
            mid_vector.push_back(candidates[i]);
            //mid_target+=candidates[i];
            solve(candidates, mid_target + candidates[i], i, target, mid_vector, result);
            //solve(candidates, mid_target, i, target, mid_vector, result);
            mid_vector.pop_back();
        }
    }
};
