class Solution {
    public int averageValue(int[] nums) {
        int total = 0;
        int count = 0;

        for (int num : nums) {
            if (num % 6 == 0) {
                total += num;
                count++;
            }
        }

        if (count == 0) {
            return 0;
        }

        return total / count;
    }
}