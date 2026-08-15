class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> lst;

        for (int i = 0; i < nums.size(); i++) {
            int leftSum = accumulate(nums.begin(), nums.begin() + i, 0);
            int rightSum = accumulate(nums.begin() + i, nums.end(), 0) - nums[i];

            int ans = abs(leftSum - rightSum);
            lst.push_back(ans);
        }

        return lst;
    }
};