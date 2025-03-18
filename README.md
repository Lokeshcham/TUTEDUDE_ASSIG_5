# README

## Task 1: Create a Dictionary of Student Marks
### Problem Statement
Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.

### Code Explanation
1. **Creating the Dictionary:**
   - A dictionary `student_marks` is initialized with student names as keys and marks as values.

2. **Taking User Input:**
   - The program prompts the user to enter a student’s name.

3. **Retrieving Marks:**
   - It checks if the entered name exists in the dictionary.
   - If found, it prints the marks.
   - If not found, it prints an appropriate message.

### Usage
1. Run the script.
2. Enter a student's name when prompted.
3. The program will display the corresponding marks or a "Student not found" message.

### Example Output
```
Enter the student's name: Bob
Bob's marks: 90
```
```
Enter the student's name: John
Student not found in the records.
```

---

## Task 2: Demonstrate List Slicing
### Problem Statement
Write a Python program that:
1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list.
3. Reverses these extracted elements.
4. Prints both the extracted list and the reversed list.

### Code Explanation
1. **Creating the List:**
   - A list `numbers` is initialized with values from 1 to 10 using `range(1, 11)`.

2. **Extracting the First Five Elements:**
   - Using list slicing `numbers[:5]`, the first five elements are stored in `first_five`.

3. **Reversing the Extracted Elements:**
   - The extracted list is reversed using slicing `[::-1]` and stored in `reversed_five`.

4. **Displaying the Output:**
   - The extracted and reversed lists are printed.

### Usage
1. Run the script.
2. The program will extract the first five numbers and reverse them.
3. The results are displayed.

### Example Output
```
First five elements: [1, 2, 3, 4, 5]
Reversed first five elements: [5, 4, 3, 2, 1]
