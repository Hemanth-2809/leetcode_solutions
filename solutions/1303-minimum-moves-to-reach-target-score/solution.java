class Solution {
    public int minMoves(int target, int maxDoubles) {
        int steps = 0;

        if(maxDoubles == 0 || target == 1){
            return target-1;
        }
        while(target!=1){
            if(maxDoubles == 0 || target == 1){
            return target-1+steps;
        }
            if(target%2 == 0 && maxDoubles!=0){
                target = target/2;
                maxDoubles--;
                steps++;

            }
            else{
                target--;
                steps++;

            }
        }
        return steps;
    }
}
