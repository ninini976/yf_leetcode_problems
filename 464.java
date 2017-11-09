// use dp to solve the problem
// map from a game state to a bool-> first player win or lose
// game state is represented by a boolean vector used[] converted to an integer

// For this problem, by applying the memo, we at most compute for every subproblem once, and there are O(2^n) subproblems, so the complexity is O(2^n) after memorization. (Without memo, time complexity should be like O(n!)

public class Solution {
    // global var 
    Map<Integer, Boolean> map;
    boolean[] used;
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        int sum = (1+maxChoosableInteger)*maxChoosableInteger/2;
        if(sum < desiredTotal) return false;
        if(desiredTotal <= 0) return true;
        
        map = new HashMap();
        used = new boolean[maxChoosableInteger+1];
        return helper(desiredTotal);
    }
    
    public boolean helper(int desiredTotal){
        // base case
        if(desiredTotal <= 0) return false;
        // convert used[] to key
        int key = format(used);
        // dp doesn't record the state
        if(!map.containsKey(key)){
            // try every unchosen number as next step
            for(int i=1; i<used.length; i++){
                if(!used[i]){
                    used[i] = true;
                    // check whether this lead to a win (i.e. the other player lose)
                    if(!helper(desiredTotal-i)){
                        map.put(key, true);
                        // backtrace
                        used[i] = false;
                        return true;
                    }
                    // backtrace
                    used[i] = false;
                }
            }
            map.put(key, false);
        }
        return map.get(key);
    }
   
    // transfer used[] to an Integer 
    public int format(boolean[] used){
        int num = 0;
        for(boolean b: used){
            num <<= 1;
            if(b) num |= 1;
        }
        return num;
    }
}
