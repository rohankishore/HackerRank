import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    updated_grades = []
    for grade in grades:
        if grade >= 38:
            next_5_multiple = (math.ceil(grade / 5)) * 5
            if (next_5_multiple - grade) < 3:
                updated_grades.append(next_5_multiple)
            else:
                updated_grades.append(grade)
        else:
            updated_grades.append(grade)
    return updated_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    for value in result:
        print(value)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
