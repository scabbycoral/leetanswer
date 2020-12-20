class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string s;
		vector<string> vec;
		dfs(n, n, vec, s);
		return vec;
	}

	void dfs(int left, int right, vector<string> &vec, string s) {
		if (left < 0 || right < 0 || left >  right) {  //控制(生成在末尾
			return;
		}
		if (left == 0 && right == 0) {
			vec.push_back(s);
			return;
		}

		s.push_back('(');
		dfs(left - 1, right, vec, s);
		s.pop_back();
		s.push_back(')');
		dfs(left, right - 1, vec, s);
		//s.pop_back();

    }
};
