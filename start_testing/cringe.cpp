#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        size_t numElements = nums.size();
        for (int i = 0; i < numElements; i++) {
            if (s.find(nums[i]) != s.end()) {
                return true;
            }
            s.insert(nums[i]);
        }
        return false;
    }
};

int main() {
    // Test cases
    vector<int> nums1 = {1, 2, 3, 4, 5};     // No duplicates
    vector<int> nums2 = {1, 2, 3, 1, 4};     // Contains duplicate (1)
    vector<int> nums3 = {10, 20, 30, 30};    // Contains duplicate (30)
    
    Solution sol;

    cout << "Test case 1: " << boolalpha << sol.containsDuplicate(nums1) << endl;
    cout << "Test case 2: " << boolalpha << sol.containsDuplicate(nums2) << endl;
    cout << "Test case 3: " << boolalpha << sol.containsDuplicate(nums3) << endl;

    return 0;
}
