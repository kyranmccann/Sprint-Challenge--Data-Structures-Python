Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method? O(n), as it visits every node in the tree once.

2. What is the space complexity of your `depth_first_for_each` function? O(n), as it depends on the height of the tree

3. What is the runtime complexity of your `breadth_first_for_each` method? O(n), as it visits every node in the tree once

4. What is the space complexity of your `breadth_first_for_each` method? O(n), as it depends on the number of nodes in the tree


5. What is the runtime complexity of the provided code in `names.py`?
 <!-- duplicates = []
 for name_1 in names_1: O(n)
     for name_2 in names_2: O(n)
         if name_1 == name_2: O(1)
             duplicates.append(name_1) O(1)-->
O(n^2), thanks to nested for loops.

6. What is the space complexity of the provided code in `names.py`? Assuming the two lists have different lengths: O(n*m)

7. What is the runtime complexity of your optimized code in `names.py`?
Now that I don't have anything nested and am just creating a dictionary with all of the names in one of the lists, I think it's O(n)
8. What is the space complexity of your optimized code in `names.py`?
Now that I am creating a dictionary to store the names from one of the list, I believe it is O(n), since that dictionary will need to be as large as the list being stored.
O(n * n+m)
