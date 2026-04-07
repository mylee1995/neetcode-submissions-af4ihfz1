class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int key = target - nums[i];
            if (map.count(key)) {
                return {map.at(key), i};
            } else {
                map.insert({nums[i], i});
            }
        }
        return {};
    }
};