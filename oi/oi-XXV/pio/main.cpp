#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

// cross-product of two vectors a*b
long long cross(std::pair<long long, long long> a, std::pair<long long, long long> b){
    return a.first*b.second - a.second*b.first;
}

long long scalar(std::pair<long long, long long> a, std::pair<long long, long long> b){
    return a.first*b.first + a.second*b.second;
}

bool ccw_of_two_points(std::pair<int,int>& a, std::pair<int,int>& b){
    if(a.first >= 0 and b.first < 0) return true;
    if(a.first < 0 and b.first >= 0) return false;
    if(a.first == 0 and b.first == 0) {
        if(a.second > 0 and b.second < 0) return true;
        else return false;
    }

    return cross(a,b) < 0;
}

unsigned long long euc_dist(std::pair<long long, long long> a, std::pair<long long, long long> b){
    return (a.first-b.first)*(a.first-b.first) + (a.second-b.second)*(a.second-b.second);
}

unsigned long long find_max_dist(std::vector<std::pair<int,int>>& v) {
    auto center_point = std::make_pair(0,0);
    unsigned long long max_dist = 0;
    long long x = 0;
    long long y = 0;
    unsigned int i = 0;

    for(unsigned int j = 0; j < v.size(); j++){
        while(cross(v[j], v[i]) < 0 || (cross(v[j], v[i]) == 0 and scalar(v[j], v[i]) >= 0)){
            x += v[i].first;
            y += v[i].second;
            i = (i+1)%v.size();
            max_dist = std::max(max_dist, euc_dist(center_point, std::make_pair(x, y)));
            if (i == j) break;
        }

        x -= v[j].first;
        y -= v[j].second;
        max_dist = std::max(max_dist, euc_dist(center_point, std::make_pair(x, y)));
    }
    
    return max_dist;
}

int main(){

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<std::pair<int,int>> v;    
    for(int i = 0; i < n; i++){
        int a,b;
        std::cin >> a >> b;
        if(a == b and a == 0) continue;
        v.push_back(std::make_pair(a,b));
    }
    if(v.size() == 0){
        std::cout << 0 << std::endl;
        return 0;
    }

    auto center_point = std::make_pair(0,0);

    std::sort(v.begin(), v.end(), [](std::pair<int,int> a, std::pair<int,int> b){
        return ccw_of_two_points(a,b);
    });

    std::vector<std::pair<int,int>> v2;
    for(auto p: v){
        if (!v2.empty() and cross(v2.back(), p) == 0 and scalar(v2.back(), p) > 0){
            auto d = v2.back();
            v2.pop_back();
            d.first += p.first;
            d.second += p.second;
            v2.push_back(d);
        }
        else{
            v2.push_back(p);
        }
    }
    v = v2;

    if(v.size() == 1){
        std::cout << euc_dist(center_point, v[0]) << std::endl;
        return 0;
    }

    auto max_dist = find_max_dist(v);

    v2.clear();
    for(auto p: v){
        v2.push_back(std::make_pair(p.first, -p.second));
    }

    std::sort(v.begin(), v.end(), [](std::pair<int,int> a, std::pair<int,int> b){
        return ccw_of_two_points(a,b);
    });

    max_dist = std::max(max_dist, find_max_dist(v2));
    std::cout << max_dist << std::endl;
    return 0;

}