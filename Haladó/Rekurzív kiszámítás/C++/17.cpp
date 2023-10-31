#include <iostream>
#include <vector>
int main(){
    int n;
    std::vector<int> v={0,3,10};
    std::cin >> n;
    for(int i=3;i<(n+1);i++){
        v.push_back((3*(v.at(i-1))+(v.at(i-2)))%20210108);
    }
    std::cout << v.at(n);
    return 0;
}