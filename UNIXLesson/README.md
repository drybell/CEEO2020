# Welcome to the UNIX Tutorial/Workshop! 

This README will help you navigate your way through Unix-like machines, and for people already familiar with working with Terminal/`sh`, a set of challenges to try out and work on new bash skills. If you think you're a pro, try out some [challenges](#challenges) and skip my massive wall of text. 

## For PC users that want to try this out but don't want to dual-boot/get a VM/emulate: 

Try out https://cocalc.com/ or https://bellard.org/jslinux/. These online Unix emulators allow you to experience some basic functionality so you can follow along. 

## Table of Contents 

1. [Cheat Sheet](#cheat-sheet)
2. [Walkthrough of Essential Commands](#walkthrough-of-essential-commands)
3. [Permissions](#permissions)
4. [Compression](#compression)
5. [Test Your Knowledge](#test-your-knowledge)
6. [Challenges](#challenges)
7. [Extra Resources and Further Hacking](#extra-resources-and-further-hacking)

### A quick aside...

If you ever have any issues with a command, or don't know where to look for, there's tons of resources online to help out! Here are a couple: https://www.techonthenet.com/unix/index.php, https://files.fosswire.com/2007/08/fwunixref.pdf, http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/unix_cheatsheet.html and obviously [stack overflow](https://www.youtube.com/watch?v=dQw4w9WgXcQ) has all the answers to your questions. 

As I'm making this guide, I'm watching ASCII Star Wars in my Terminal by typing the command  `telnet towel.blinkenlights.nl`. Feel free to give it a watch **AFTER** the lesson.

## Cheat Sheet  

Below is a list of commands and respective flags that you should have in your toolbox. Use this cheat sheet when solving problems listed below. 

- **`ls`**: list all files (within your current directory). You can also list files in a specified folder name with `ls path/to/your/folder/here/` 
    * **`-a`**: Display all files, even hidden ones (that start with a period --> .gitignore)
    * **`-l`**: Display files in long format, with permissions 
    * **`-r`**: Display files in reverse order 
    * **`-u`**: Display files by access time 
    * **`-R`**: Display all subfolders and their respective files in an organized fashion

**Note:** You can mix and match `ls` **and most other** command flags to fulfill your craziest wishes. If you need to list all files and their subfolders in long format, while also filtering them by access time, you can do that with `ls -laRu` or `ls -l -a -R -u` 

- **`cd`**: Change directory. Moves a hypothetical pointer of where your Terminal window is currently working in to a specified folder. **All commands that you execute require for you to be in the proper working directory and understand the file-structure.** This is probably the most used command other than `ls`. Examples: `cd ~` --> change to home directory. `cd ..` --> change to the parent directory. `cd /path/to/folder` --> change your working directory to the folder specified. Simply typing `cd` will change you back to the home directory.

- **`pwd`**: Print working directory. If you don't know where you currently are, simply type in `pwd` and it will print something like `/Users/your_username_here/path/that/you/got/stuck/in/and/now/you/don't/know/where/you/are/`. You can then use `cd` to get back to the home directory or chain `cd ../../../../..` to move back (in this case) 5 parent directories. The amount of `..` indicates the amount of parent directories you're jumping up. 

**Pro Hacker Move:** If you have a couple hours, bored with your life, and are browsing insecure websites, real-life hacking awaits! In a form that you think potentially doesn't scrub its input, you can type in a set of chaining `../` and `/etc/shadow` to try and get the server to respond with a list of password hashes. You could try and crash our own Onshape App if you'd like (good luck)! For example, an attempt could be `../../../../../../etc/shadow`. If you don't have a form, you can still query the server with a well-crafted [URI](https://en.wikipedia.org/wiki/URI_scheme). Example: `http://example.com/../../../../../../etc/shadow` or `http://target/..%u2216..%u2216directory/file` to get through servers that scrub Unicode encoded characters. Remember, ethical hacking is ok, but doing this stuff on real websites is illegal. However, you can always message the site and tell them that you're a security expert and successfuly found the list of credit cards they're improperly storing in order to recieve a nice payout. I'd recommend not doing that unless you know what you're doing. Instead, test your hacker skills by spinning up your own server! 

- **`mv`**: Move or rename a file. Example: `mv file-that-should-be-somewhere-else.txt ../here` will move the file up one directory to a folder named `here`
    * **`-v`**: Verbose output, basically has `mv` explain what's being done. Useful for debugging a faulty `mv` command 
    * **`-f`**: Allows you to forcefully move source files to a destination folder. Basically forces the move without a prompt asking if it's ok to overwrite files with the same names. Useful when you know the contents inside a folder are useless.

    Examples: `mv file1.txt my-api-keys 5G_corona_build.pkg backdoor-to-nsa.sh file5.tsx ~/Documents` moves all files to the Documents folder (the `~` is a shortcut for your home directory).

- **`man`**: Your dedicated manual. Type in `man any-executable` and it will give you documentation that the authors of the script wrote. Press q to quit

**Tip:** If you don't know what commands you have, go ahead and `ls /bin` to see what default commands come with your distribution of Terminal. Use `ls /usr/local/bin` to see any extra commands that you've downloaded over the years. If you have `brew` installed, you can check the executables you downloaded with `brew list`. You can also `man brew`. Try and `man` something, you'll learn a couple new tricks. Everything is manpageable! 

- **`cp` and `scp`**: Copy a file or directory. Sort of like `mv` but you keep the original source files/folders. `scp` is used if you need to copy stuff to a remote directory (for example, a homework server or an AWS instance that you have to get to by running `ssh`) and has basically the same functionality as `cp`
	* **`-r`**: Recursive, copy directories and all sub-files (and folders). Example: `cp -r my_folder1 ~/Downloads` **copies** my_folder1 and all its contents to the Downloads folder. 
    * `scp` example: `scp robot@117.8.2.4:~/Documents/main.py .` will first prompt you for your password for the `ssh` instance and then copy over the file `main.py` from your Lego EV3 to the current working directory (that's what the `.` is doing)

- **`rm`**: **WARNING:** this command will remove and permanently delete files from your machine. Use with extreme caution. 
    * **`-r`**: Recursive, delete the directory and all of its contents. Example: `rm -r my-past-mistakes/` to remove the directory `my-past-mistakes`. It does not go to your Trash bin, its bits will forever dissolve into the aether. 
    * **`-f`**: Forcibly remove contents, without prompting for user permission. A common tactic to make new enemies is to go over to an unsuspecting person and type `rm -rf *` into their Terminal to promptly delete everything (More on * functionality later). If you're smart, you will use `chmod` to remove execute permissions of the folder.

- **`chmod`**: Change permission of a file or directory. More information on usage in [Permissions](#permissions)

- **`sudo`**: Your go to root command. If you need elevated permission to view, execute, or read files, precede a command with `sudo`. You will be prompted to type in your password. Example: `sudo mv restricted-file restricted-directory` will move a restricted file to a restricted directory. If you need to switch to root, type in `sudo su` (don't forget to switch back out by running the same command). 

- **`cat`**: Print out a file's contents. Example: `cat main.py` will output your genius code to the terminal. If you want to redirect the output to a new file, try `cat main.py > new_file.txt` or append with `cat main.py >> logs`. 

- **`diff`**: Find the differences of two files. Example `diff text1.txt text2.txt` will print out all of the lines that are different. Useful when you're writing tests (with correct answers) and checking your script output to see if your code is correct. 

- **`zip`, `unzip`, `gunzip`, `tar`**: Zipping and unzipping files the Terminal way. More info in [Compression](#compression)

- **`curl`**: Your very own postman! Query stuff online. Useful tips [here](https://curl.haxx.se/docs/manual.html). Example: `curl http://wttr.in/LOCATION` to find out the weather in LOCATION (Try `curl http://wttr.in/Boston`). You can flex on Chris Rogers by crafting a SystemLink POST call with curl (I won't give you the answer, this one's on you). 
    * **`-h` or `--header`**: Craft your own API header. Example: `curl --header 'content-type: application/json'` 
    * **`--request`**: Specify the request method. Example: `curl --request GET --url http://blah-blah.com`
    * **`--url`**: The url you want to send a cURL to. 
    * **`-s`**: silent mode.
    * **`-S`**: Show errors. 
    Example: `curl -sS "https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo?action=raw"` allows you to view the list of olympic medalists in judo. 

If you don't believe the powers of cURL, I've taken the freedom to try out some of the commands for you. Here's the output: 

![weather](./images/weather.png) ![moon](./images/moon.png) ![judo](./images/judo.png)






## Walkthrough of Essential Commands


## Permissions

## Compression

## Test Your Knowledge


## Challenges

## Extra Resources and Further Hacking










Psst... jealous of my decked out terminal? Go ahead and download https://ohmyz.sh/ to get your outdated terminal a snazzy new look.

If you always use multiple terminals and need a better way of managing them, try out tmux! `brew install tmux` if you dare. 