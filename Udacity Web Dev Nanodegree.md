# Web Dev Udacity

###### 01. Programming foundation with python
###### 02. Html and Css
###### 04. Responsive Design
###### 05. Shell Workshop
###### 06. Version Control with Git
###### 07. Github and How to Collaborate on a VCS Project



Using twilio benfrank101 +18065471588
sid: AC5b213cabb4007b167882da6ba576db5d
authT: 404089f2a7fd84edb75fe7d89cc35328

Download Markdown Cheat sheet
bashrcgenerator.com 
Download Version control cheatsheet

### RESPONSIVE DESIGN FUNDAMENTALS    

For Responsiveness
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Relative positions instead of absolute positions e.g width=100%

Use relative unit - set in your css
```css
img, embed, object, video {
    max-width:100%;
}
```
For touch/tap input
make buttons 48px by 48px
```css
nav, a, button{
    min-width:  48px;
    min-height: 48px;
    padding: 1.5em
}
```

Start Small
Prioritize content i.e only important stuff to the user

Media Queries : Applying different styles to different devices.
To change media query on device demand add an additional css style based on the device screen
```html
<!--Changing css based on screen size in html- creates a smaller fill with more request -->
<link rel="stylesheet" media="screen and (min-width: 300px)" href="pattern.css">
```
```css
/*Changing css based on screen size in css - Creates a larger file with fewer request*/

@media screen and (min-width: 500px) {
    body{ background-color:cadetblue }
}
@media screen and (min-width: 800px) {
    body{background-color: darkolivegreen}
}
```

#### Breakpoints
This is where the site changes on resizing
##### Rules for adding breakpoints
* Start Small
* Resize until the content looks out of place
* add a css that fixes the element out place
#### Flexbox
Fixes the space around it
```css
.container{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
}
```
###### Flex item Order
```css
@media screen and (min-width: 700px){
    .dark_blue{order: 4;}
    .light_blue{order: 5;}
    .green {order:2;}
    .orange {order: 3;}
    .red {order: 1;}
}
```
###### Flexbox Deconstructed
```css
@media screen and (min-width: 360px){
    cyan{width: 100%; order: 1; background-color: cyan;}
    .red{width: 50%; order: 2; background-color: red;}
    .orange{width: 50%; order: 3; background-color: orange;}
    teal{width: 100%; order: 4; background-color: teal;}
    .light_blue{width: 20%; order: 5; background-color: lightblue;}
    .dark_blue{width: 60%; order: 6; background-color: darkblue;}
    .green{width: 60%; order: 7; background-color: green; }
}
```

### Shell WorkShop
* ; concatinate and run multiple commands at once
* ~ home directory
* ls -l : detailed list all files in directory
* mkdir : create a new directory
* mv 'from/folder to/folder' : move files
* curl -o google.html -L 'https://google.com' : downloads google.com and saves to a file google.html
* less file.ext :   to view a file line by line
* cat file.ext :    to view full file
* rm filename :     to remove a file permanently
* rm -i filename :  to remove file with interaction
* rmdir directory:  to remove directory

### Version Control with Git
Centralized : one computer controls the rest

Distributed : every other computer has it's own file

HEAD : Points to the branch that is currently being worked on
###### Areas
* Working Directory : contains file you're currently working on
* Staging Index : contains all the files that are about to be committed
* Repository: contains all saved/committed files
###### Unfamiliar Commands
* git log --oneline : list changes in a single line
* git log --stat : list the files changed
* git log -p : list the changes or patches made to file
* git tag -a v1.0 
* git merge : combine changes
* git commit --amend : Alter the most recent commit
* git revert : Reverse a commit
* git reset --hard HEAD~1: Deletes changes
* git reset --soft HEAD~1: reset changes to the stagging area
* git reset --hard HEAD~1: reset changes to the working area

### Github and How to Collaborate on a VCS Project
Before rebasing create a branch of the master

rebasing squash / combine commits into one
###### Unfamiliar Commands
* git remote add origin "repoURL" : to add remote origin
* git push -u origin master : push to the master branch on the remote
* git rebase -i HEAD~3 : squash 3 commit into one

