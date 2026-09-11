class Solution {
public:

    void Solve(vector<int>&digits, vector<int>&vis, string s,set<string>&st, int n){
        //step - 1 base case
        if(s.size() == 3){
            int val = s[2]-'0';
            if(val % 2 == 0) st.insert(s);
            return;
        }

        for(int i = 0 ; i < n ; i++){
            if(vis[i]==0){
                if(s.size()== 0 && digits[i]== 0){
                    continue;
                }
                s.push_back(digits[i] + '0');
                vis[i] = 1;
                Solve(digits,vis,s,st,n);
                s.pop_back();
                vis[i]=0;
            }
        }
    }
    int totalNumbers(vector<int>& digits) {
        int n = digits.size();
        vector<int>vis(n,0);

        string s;
        set<string>st;
        Solve(digits,vis,s,st,n);   
        return st.size();
    }
};