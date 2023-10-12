### <span style="color: #03ce14;">Exceptions</span>
* <span style="color: #ff1199;">Exceptions</span>
   * A Siple IndexError in list and ValueError in input method
* <span style="color: #ff1199;">Handling Exceptions</span>
   * Try / except clause 
     
   * Using as statement we can print the reason of exception
   * Use type to get info about error class
* <span style="color: #ff1199;">Handling Different Exceptions</span>
   * A simple error of Zero Division x = 10 / age
   * We can add more except clause to handel other kind of errors
   * Also we can put more error kind in front of except clause inside parentheses
* <span style="color: #ff1199;">Cleaning Up</span>
   * A finally clause always execute after a try/except clause
     
* <span style="color: #ff1199;">The With Statement</span>
   * With statement automatically release resources
     
   * Any kind of objects that have Context Management Protocol(CMP) in case of using with statement python automatically call __exit__() method for it
   * We can open multiple file using one with statement
* <span style="color: #ff1199;">Raising Exceptions</span>
   * We can write our function and get exceptions by raise statement
   * Try block can get our raise exception error as variable which we define
     
* <span style="color: #ff1199;">Cost of Raising Exceptions</span>
   * Using timeit library to calculate time
   * If we are building a simple app we can use raise exception and try block but in complex program with lots of processes or users it's better to handle problem without try or raise clauses
