class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> map;
        for(int i = 0; i < nums.size(); i++) {
            if (map.contains(nums[i])) {
                return true;
            }
            map.insert(nums[i]);
        }
        return false;
    }
};