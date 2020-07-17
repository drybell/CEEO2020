#!/bin/sh 

# I write comments like this, it's like python! 
echo "This is my first ever shell script!"

##########################################################
###  Variables 

FIRST_VARIABLE="HELLO WORLD"
echo $FIRST_VARIABLE

##########################################################
###  Input from User 

echo "What is your name?"
read USER_NAME
echo "Hello $USER_NAME, thanks for following my tutorial"

##########################################################
###  Command Line Arguments 

echo "Positional Parameters"
echo '$0 = ' $0     # the command itself
echo '$1 = ' $1     # the first argument
echo '$2 = ' $2     # the second argument
echo '$3 = ' $3     # the third argument 

# Test if you have command line arguments
# More on conditionals below 
if [ $# -gt 0 ]; then
    echo "Your command line contains $# arguments"
else
    echo "Your command line contains no arguments"
fi

# You can run any shell command either in a script or in the terminal

# Uncomment this next line to create a file with the name of the user
# touch ${USER_NAME}_file.txt

# Note the curly brackets that allow the variable to be appended to _file.txt
# If USER_NAME was 'steve', then the file would be steve_file.txt

##########################################################
###  For Loops 

for i in 1 2 3 4 5
do
  echo "Looping ... number $i"
done

# This is how you iterate through a range of values, and
# how to write inline for loops
END=5
for i in {1..$END}; do echo $i; done

# What do you think happens when this code is executed? 
for i in hello 1 * 2 goodbye 
do
  echo "Looping ... i is set to $i"
done

##########################################################
###  While Loops 

INPUT_STRING=hello
while [ "$INPUT_STRING" != "bye" ]
do
  echo "Please type something in (bye to quit)"
  read INPUT_STRING
  echo "You typed: $INPUT_STRING"
done

# SWITCH CASES 
# esac is just the opposite of case, it ends the switch case statement
while read f
do
  case $f in
	hello)		echo English	;;
	howdy)		echo American	;;
	gday)		echo Australian	;;
	bonjour)	echo French	;;
	"guten tag")	echo German	;;
	*)		echo Unknown Language: $f
		;;
   esac
done < myfile
# Note the < operator allowing you to read input from a file named myfile

# Try and modify the code to pass in a command-line argument which holds the file name 


##########################################################
###  IF-Else Syntax  

# Simple syntax, uncomment and add something in the ... to try out
# if [ ... ]
# then
#   # if-code
# else
#   # else-code
# fi


# inline if; then syntax 

# if [ ... ]; then
#   # do something
# fi

# elif syntax, same as python

# if  [ something ]; then
#  echo "Something"
#  elif [ something_else ]; then
#    echo "Something else"
#  else
#    echo "None of the above"
# fi

# from https://www.linuxtechi.com/compare-numbers-strings-files-in-bash-script/

# Numeric comparisons 
# num1 -eq num2 check  if 1st  number is equal   to   2nd number
# num1 -ge num2 checks if 1st  number is greater than or  equal to 2nd number
# num1 -gt num2 checks if 1st  number is greater than 2nd number
# num1 -le num2 checks if 1st  number is less    than or  equal to 2nd number
# num1 -lt num2 checks if 1st  number is less    than 2nd number
# num1 -ne num2 checks if 1st  number is not     equal to 2nd number

# String comparisons
# var1 = var2     checks if var1 is the same as string var2
# var1 != var2    checks if var1 is not the same as var2
# var1 < var2     checks if var1 is less than var2
# var1 > var2     checks if var1 is greater than var2
# -n var1             checks if var1 has a length greater than zero
# -z var1             checks if var1 has a length of zero

# file comparisons
# -d file              checks if the file exists and is it’s a directory
# -e file              checks if the file exists on system
# -w file              checks if the file exists on system and if it is writable
# -r file              checks if the file exists on system and it is readable
# -s file              checks if the file exists on system and it is not empty
# -f file              checks if the file exists on system and it is a file
# -O file              checks if the file exists on system and if it’s is owned by the current user
# -G file              checks if the file exists and the default group is the same as the current user
# -x file              checks if the file exists on system and is executable
# file A -nt file B    checks if file A is newer than file B
# file A -ot file B    checks if file A is older than file B


if [2 -gt 3]
     then
     print "2 is greater"
     else
     print "2 is not greater"
fi

# Script to do numeric comparisons
var1=10
var2=20
if [ $var2 -gt $var1 ]
    then
        echo "$var2 is greater than $var1"
fi
# Second comparison
if [ $var1 -gt 30 ]
    then
        echo "$var is greater than 30"
    else
        echo "$var1 is less than 30"
fi

# script to check string comparisons
var1=a
var2=z
var3=Z
if [ $var1 \> $var2 ]
        then
                echo "$var1 is greater"
        else
                echo "$var2 is greater"
fi
# Lower case  & upper case comparisons
if [ $var3 \> $var1 ]
        then
                echo "$var3 is greater"
        else
                echo "$var1 is greater"
fi

# test if file is folder 
dir=/home/Documents
if [ -d $dir ]
        then
                echo "$dir is a directory"
                cd $dir
                ls -a
        else
                echo "$dir is not exist"
fi



