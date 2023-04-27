#include <deque>
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int length = rooms.size();
        vector<int> answer(length, 0);
        
        answer[0] = 1;
        
        deque<int> queue;
        for (int i = 0; i < rooms[0].size(); i++) {
            queue.push_back(rooms[0][i]);
            answer[rooms[0][i]] = 1;
        }
        
        while (!queue.empty()) {
            int N = queue.size();
            for (int i = 0; i < N; i++) {
                auto popped = queue.front();
                queue.pop_front();
                for (int j = 0; j < rooms[popped].size(); j++) {
                    if (answer[rooms[popped][j]] == 0)
                        queue.push_front(rooms[popped][j]);
                        answer[rooms[popped][j]] = 1;
                }
                    
            }
        }
        
        
        for (int i = 0; i < length; i++) {
            if (!answer[i])
                return false;
        }
        return true;
    }
};