class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length-1;
        int w = j;
        int maxx = 0;
        while(i<j){
            maxx = Math.max(maxx,(w*Math.min(height[i],height[j])));
            if (height[i]<height[j]){
                i++;
                w--;
            }
            else{
                j--;
                w--;
            }
            

            
        }
        return maxx;
        
    }
}
