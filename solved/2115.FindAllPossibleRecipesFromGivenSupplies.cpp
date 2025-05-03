#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_set<string> supp(supplies.begin(), supplies.end());
        vector<string> res;

        int last = supp.size();
        while (true) {
            for (int i = 0; i < recipes.size(); i++) {
                if (recipes[i].length() == 0) continue;

                bool valid = true;
                for (auto ing : ingredients[i]) {
                    if (!supp.count(ing)) {
                        valid = false;
                        break;
                    }
                }

                if (valid) {
                    supp.insert(recipes[i]);
                    res.push_back(recipes[i]);
                    recipes[i] = "";
                }
            }
            if (supp.size() == last) break;
            last = supp.size();
        }

        return res;
    }
};
