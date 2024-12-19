class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int sum=0;
        int count=0;
        for(int i:costs){
            sum+=i;
            if(sum<=coins){
                count++;
            }
        }
        return count;
    }
}