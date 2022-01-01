import java.util.Arrays;

public class containsDuplicate {
    public static void main(String[] args) {
        System.out.println(containsDuplicate(new int[] {0, 1, 2, 0}));
    }

    public static boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] == nums[j]) return true;
            }
        }
        return false;
    }

}