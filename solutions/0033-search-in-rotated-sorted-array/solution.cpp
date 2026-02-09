class Solution {
public:
    int search(vector<int>& v, int t) {
        int n = v.size();
        int l = 0, r = n - 1, o = -1;
        while (l <= r) {
            int m = (l + r) >> 1;
            if (v[m] == t) { o = m; break; }
            bool s = v[l] <= v[m];
            bool d = s ? (v[l] <= t && t < v[m]) : !(v[m] < t && t <= v[r]);
            d ? (r = m - 1) : (l = m + 1);
        }
        return o;
    }
};

