class Solution {
public:
    int differenceOfSums(int n, int m) {
        /*
        all      n * (n+1) / 2
        n_divs   n / m
        med_div  (m + (m * n_divs)) / 2
        divs     med_div * n_divs
        res      all - 2 * divs

        distribute the (2 * divs) multiplication to avoid .5 results
        in med_div and simplificate with the / 2
        */
        return (n * (n+1) / 2) - ((m + (m * (n / m))) * (n/m));
    }
};
