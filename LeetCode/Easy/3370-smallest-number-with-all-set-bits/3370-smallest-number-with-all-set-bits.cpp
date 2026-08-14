class Solution {
public:
    int smallestNumber(int n) {
        int answer=0;
        while (n>0){
        answer=(answer<<1)|1;
        n=n>>1;}
    return answer;}
};