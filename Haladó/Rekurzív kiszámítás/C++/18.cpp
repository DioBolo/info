#include <iostream>
#include <vector>

int main(){
    int n;
    std::vector<int> v={0,2,4,10};
    std::cin >> n;
    for(int i=4;i<(n+1);i++){
        v.push_back((2*(v.at(i-1))+2*(v.at(i-3)))%20210108);
    }
    std::cout << v.at(n);
    return 0;
}