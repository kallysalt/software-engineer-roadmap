#include <iostream>
#include <string>
#include <unordered_map>

class Test {

public:
    void test() {
        
        // create hashmap
        std::unordered_map<int, std::string> hmap;

        // add element
        // time complexity: O(1)
        hmap[1] = "hanmeimei";
        hmap[2] = "lihua";
        hmap[3] = "siyangyuan";

        print_map(hmap);

        // update element
        // time complexity: O(1)
        hmap[1] = "bishi";

        print_map(hmap);

        // remove element
        // time complexity: O(1)
        hmap.erase(1);  

        print_map(hmap);

        // get value
        // time complexity: O(1)
        if (auto it = hmap.find(3); it != hmap.end()) {
            std::cout << it->second << "\n";
        } else {
            std::cout << "Key 3 not found\n";
        }

        // check if given key exists 
        // time complexity: O(1)
        std::cout << (hmap.count(3) ? "True" : "False") << "\n";

        // get length
        // time complexity: O(1)
        std::cout << hmap.size() << "\n";

        // is empty
        // time complexity: O(1)
        std::cout << (hmap.empty() ? "True" : "False") << "\n";

        // iterate (key–value pairs)
        // time complexity: O(n)
        for (const auto& [key, value] : hmap) {
            std::cout << key << ": " << value << "\n";
        }
    }

private:
    static void print_map(const std::unordered_map<int, std::string>& m) {
        std::cout << "{";
        bool first = true;
        for (const auto& [k, v] : m) {
            if (!first) std::cout << ", ";
            std::cout << k << ": " << v;
            first = false;
        }
        std::cout << "}\n";
    }
};

int main() {
    Test t;
    t.test();
    return 0;
}
