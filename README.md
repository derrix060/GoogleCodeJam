# GoogleCodeJam

folder to solved problems in Google Code Jam by derrix060


## A - Oversized Pancake Flipper
### Problem

Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly **K** consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than **K** pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first **K** - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each consists of one line with a string **S** and an integer **K**. **S** represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).

### Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.

### Limits

1 ≤ **T** ≤ 100.
Every character in **S** is either + or -.
2 ≤ **K** ≤ length of **S**.

*Small dataset*: 2 ≤ length of **S** ≤ 10.

*Large dataset*: 2 ≤ length of **S** ≤ 1000.

### Sample
Input    |       Output
--- | --- 
3            |
---+-++- 3   |   Case #1: 3
+++++ 4      |   Case #2: 0
-+-+- 4      |   Case #3: IMPOSSIBLE




## B - Tidy Numbers

### Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to *N*. What was the last tidy number she counted?

### Input

The first line of the input gives the number of test cases, *T*. *T* lines follow. Each line describes a test case with a single integer *N*, the last number counted by Tatiana.

### Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

### Limits

1 ≤ *T* ≤ 100.

**Small dataset**: 1 ≤ *N* ≤ 1000.
**Large dataset**: 1 ≤ *N* ≤ 10^18.


### Sample

Input | Output 
--- | --- 
4 |  
132 | Case #1: 129
1000 | Case #2: 999
7 | Case #3: 7
111111111111111110 | Case #4: 99999999999999999


*Note that the last sample case would not appear in the Small dataset.*



## C - Bathroom Stalls

### Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall **S**, they compute two values **LS** and **RS**, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those **S** for which min(**LS**, **RS**) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(**LS**, **RS**) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

**K** people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(**LS**, **RS**) and min(**LS**, **RS**) be?

### Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

### Input

The first line of the input gives the number of test cases, **T**. **T** lines follow. Each line describes a test case with two integers **N** and **K**, as described above.

### Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(**LS**, **RS**), and z is min(**LS**, **RS**) as calculated by the last person to enter the bathroom for their chosen stall S.

### Limits

1 ≤ **T** ≤ 100.
1 ≤ **K** ≤ **N**.
*Small dataset 1*: 1 ≤ **N** ≤ 1000.
*Small dataset 2*: 1 ≤ **N** ≤ 10^6.
*Large dataset*: 1 ≤ **N** ≤ 10^18.


### Sample


Input | Output
--- | --- 
5 | 
4 2 | Case #1: 1 0
5 2 | Case #2: 1 0
6 2 | Case #3: 1 1
1000 1000 | Case #4: 0 0
1000 1 | Case #5: 500 499


*In Case #1, the first person occupies the leftmost of the middle two stalls, leaving the following configuration (O stands for an occupied stall and . for an empty one): O.O..O. Then, the second and last person occupies the stall immediately to the right, leaving 1 empty stall on one side and none on the other.*

*In Case #2, the first person occupies the middle stall, getting to O..O..O. Then, the second and last person occupies the leftmost stall.*

*In Case #3, the first person occupies the leftmost of the two middle stalls, leaving O..O...O. The second person then occupies the middle of the three consecutive empty stalls.*

*In Case #4, every stall is occupied at the end, no matter what the stall choices are.*

*In Case #5, the first and only person chooses the leftmost middle stall.*