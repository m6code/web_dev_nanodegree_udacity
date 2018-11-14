# Web Dev Udacity

###### 01. Programming foundation with python
###### 02. Html and Css
###### 04. Responsive Design

Using twilio benfrank101 +18065471588
sid: AC5b213cabb4007b167882da6ba576db5d
authT: 404089f2a7fd84edb75fe7d89cc35328

Download Markdown Cheat sheet

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