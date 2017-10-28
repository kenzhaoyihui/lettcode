import java.util.HashMap;
import java.util.Map;

public class TwoSum{
    public static void main(String [] args){
        TwoSum t = new TwoSum();
        int[] a = {1,2,3,9};
        int target = 5;
        int []b = t.twoSum(a, target);
        System.out.println(b[0] + ", " + b[1]);

    }

    public int[] twoSum(int[] nums, int target){
        int [] result = new int[2]; //存放返回值
        Map<Integer,Integer> map = new HashMap<>();

        for(int i=0;i<nums.length;i++){
            map.put(nums[i], i);
            if(map.containsKey(target-nums[i])){
                result[1] = i;
                result[0] = map.get(target-nums[i]);
                return result;
            }

            //map.put(nums[i], i+1);
        }

        return result;

    }
}