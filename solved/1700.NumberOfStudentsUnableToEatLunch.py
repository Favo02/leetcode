class Solution:
  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    san = stu = 0
    skip = 0

    while san < len(sandwiches):
      if skip == len(students):
        break

      if students[stu] == sandwiches[san]:
        san += 1
        students[stu] = -1
        skip = 0
      else:
        skip += 1

      stu = (stu + 1) % len(students)
    return len(sandwiches) - san
