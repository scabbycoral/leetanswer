class Solution {
public:
    int findRepeatDocument(vector<int>& documents) {
        unordered_map<int, bool> map;
        for(int i:documents){
            if(map[i]){
                return i;
            }
            map[i]=true;
        }
        return -1;
    }
};

/**
class Solution {
public:
    int findRepeatDocument(vector<int>& documents) {
        int i = 0;
        while(i < documents.size()) {
            if(documents[i] == i) {
                i++;
                continue;
            }
            if(documents[documents[i]] == documents[i])
                return documents[i];
            swap(documents[i],documents[documents[i]]);
        }
        return -1;
    }
};
**/

