### <span style="color: #03ce14;">Data Structures</span>
* <span style="color: #ff4909;">Lists</span>
   * A sequence of objects. one or two or More dimensional Lists
   * zeros = [0] * 100 / Use + to concatenate or * to multiply 
   * Use list() method to convert objects to list: num = list(range(20))
   * Use len() method to get length of a list
* <span style="color: #ff4909;">Accessing Items</span>
   * lst[0] , lst[-1]
   *  Use assign item to change list Items lst[1] = "B"
   *  Use [:] to get a range of items in list / [::2]
   *  Use [::-1] to reverse list(range(20))
* <span style="color: #ff4909;">List Unpacking</span>
   * first, second, third = lst / left and right must be equal in number
   * first, second, *other = lst / first, *other, last = lst
* <span style="color: #ff4909;">Lopping Over List</span>
   * Use for to loop over a list
   * enumerate() unpack list item to key and value
     
* <span style="color: #ff4909;">Adding or Removing Items</span>
   * Use .append() method to add an item to end of a list
   *  Use .insert() method to add item at specific position in list / lst.insert(1, "D")
   *  Use .pop() method to remove an item from end of a list / .pop() .pop(0)
   *  Use .remove("b") to remove first occurrence of that item / remove without index
   *  to remove all "b" in the list you should loop over list
   *  Use del lst[0] to delete an item or del lst[:3] to delete a range of items ==> this is difference between pop and del
   *  use lst.clear() to delete all items in the list.
* <span style="color: #ff4909;">Finding Items</span>
   * To find index of an item use lst.index("item")
   * .index() method return ValueError when try to find an item that is not exist.
   * Use if .. in .. to prevent this error
   * Use lst.count("item") to check existence of an item
* <span style="color: #ff4909;">Sorting Lists</span>
   * Use lst.sort(key, reverse=True|False) method to sort a list
   * To sort a list without changing the original list use sorted(lst) function / sorted(lst, reverse=True)
   * To sort a list of unordered items like list of tuples we should write a function and pass use sort item and pass all items to this function
 * <span style="color: #ff4909;">Lambda Functions</span>
   * A one line anonymous function we can pass to other functions
   * ... = lambda parameters:expression
     
  * <span style="color: #ff4909;">Map Functions</span>
   * Use mapping to map a list to make another better list
   * In ordinary way we define another list and append all second item to the new list
     
 * <span style="color: #ff4909;">Filter Functions</span>
   * To filter a list to a particular list contain some special items we use filter function
   * Regular way is looping over and separate elected items and add it to a new list
 * <span style="color: #ff4909;">List Comprehension</span>
   * "[expression for item in items] / [item[1] for item in lst]
   * To convert filtered list to comprehension do this: [item for item in lst if item[1] >= 10]
   * We can use if .. else statement in comprehension at first part of clause
* <span style="color: #ff4909;">Zip Function</span>
   * To combine two or more equal list (equal in list member) and make a new list, use zip function
   * Zip function return a tuple for each member contain all same index items
* <span style="color: #ff4909;">Stacks</span>
   * A LIFO data structure 
   * Website's pages visiting hierarchy is good simple fore Stack
   * We can use . append(), .pop() methods for simulating stack and stc[-1] and not stc to check it
* <span style="color: #ff4909;">Queues</span>
   * A FIFO data structure
   * We use deque for optimize Using queue
     
* <span style="color: #ff4909;">Tuples</span>
   * Tuple is a read only list and we use () to define it
   * if we remove () Python Assume it as tuple like 1, or 1,2
   * We can multiple or concatenate tuples
   * We can convert a list or any iterable into a Tuple using tuple()
   * We cannot mutate tuples and assign a value of tuple to a new value
* <span style="color: #ff4909;">Swapping Variables</span>
   * x, y = Y, x
   * This clause works as unpacking in tuples x, y = (11, 10)
* <span style="color: #ff4909;">Arrays</span>
   * If we deal with large sequence of numbers we should use Array
   * Array take less memory and work a little bit faster
   * For the using array we should import it
   * Array(typecode, iterable) 
   * All members in array should be the same type
* <span style="color: #ff4909;">Sets</span>
   * Set is a unordered collection of data without duplicates
   *  By converting a List to set we can remove all duplicates / set()
     
   *  Shining usage of sets is in mathematics
   *  To make union of Two sets print(set1 | st2) / print(set1 & st2) / print(set1 - st2) / print(set1 ^ st2)
   *  Sets items not in sequence and we cannot access them by index
   *  We can existence of a value by using if .. in statement
* <span style="color: #ff4909;">Dictionaries</span>
   * Dictionary is a key value per collection of data
   * In dictionary keys can only be an integer of string and value can be kind of anything
   * We can define a dictionary using dict() function
    
* <span style="color: #ff4909;">Dictionary Comprehension</span>
   * We can use Comprehension for sets and dictionaries
   * Val = {x : x*2 for x in range(5)}
* <span style="color: #ff4909;">Generators</span>
   * Generator object like list is a iterable but generate value in each iteration
   * Generators don't store all values in memory
     
   * Generators objects has no len
* <span style="color: #ff4909;">Unpacking Operators</span>
   * We can print Items of a list in unpacked using [*numbers]
     
   * We can use unpacking operators to combine list
