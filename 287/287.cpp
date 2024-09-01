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

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int length=nums.size();

        int start = 1;
        int end = length - 1;
        while(end >= start)
        {
            int middle = ((end - start) >> 1) + start;
            int count = countRange(nums, length, start, middle);
            if(end == start)
            {
                if(count > 1)
                    return start;
                else
                    break;
            }

            if(count > (middle - start + 1))
                end = middle;
            else
                start = middle + 1;
        }
        return -1;
    }

    int countRange(vector<int>& nums, int length, int start, int end)
    {
        int count = 0;
        for(int i = 0; i < length; i++)
            if(nums[i] >= start && nums[i] <= end)
                ++count;
        return count;
    }
};

