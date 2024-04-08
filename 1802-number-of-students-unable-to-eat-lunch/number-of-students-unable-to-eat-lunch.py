class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for sandwich in sandwiches:
            if sandwich in students:
                students.remove(sandwich)
            else:
                return len(students)
        
        return 0