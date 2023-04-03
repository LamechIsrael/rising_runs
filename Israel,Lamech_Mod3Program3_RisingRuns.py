#############################################
# CS 1110A - Programming in Python          #
# Module 3 - Project 3 - Rising Runs        #
# Author: Lamech Israel                     #
#                                           #
#############################################


def rising_runs(s):
    run1 = 1
    run2 = 0
    
    if len(s) == 0:
        return False
    else:
        for i in range(len(s)-1):
            # If the letter is the same as the next, add 1 to the first run
            if s[i] == s[i+1] and i != len(s)-2:
                run1 += 1
  
            # If the letter is not the same as the next, execute this function
            else:
                
                # If the reason we're here is this is the second to last character, execute this
                if i == len(s)-2:
                    # If the second-to-last character is the same as the last, add 1
                    if s[i] == s[i+1]:
                        run1+=1
                    # Else, make conditions to exit code
                    else:
                        run2 = run1
                        run1 = 1
                    
                
                # If this run is greater than the last run, store the new run
                if run1 >= run2:
                    run2 = run1
                    run1 = 1

                
                # Else, end the string and tell the user
                else:
                    print('This string is not rising')
                    
                    return True

        
        print('This string is rising')
        return True 

# Begin Program
Running = True

print('Does a string contain rising runs?')

while Running:
    
    Running = rising_runs(input('\nEnter a string: '))
    
print('\nDone!\n')

exit()
