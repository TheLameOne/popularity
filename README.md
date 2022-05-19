<div id="top"></div>
<br />
<div align="center">

<h3 align="center">popularity</h3>

  <p align="center">
    Instagram Followers visualizer for an Institution/Organization/Community.
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="images/screenshot.png" alt="ss" width="800" height="800">

<br>
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Instaloader](https://github.com/instaloader/instaloader)
* Python
* HTML
* CSS
* [D3JS](https://d3js.org/d3.v6.js)
* SQlite

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
This project scrapes Instagram user followers.

### databasegenerator.py
```
This generate SQLite database having Schema accounts(username, trust, followers)
```
### Sources.py
```
It makes a text file containing all the similar accounts of the target Institution 
```
### Resources.py
```
This fetches all the followers of a particular Instagram account and insert it to the Database and if a user follows multiple account of same Institution then its trust value will increase by 1.
```
### followers.py
```
This file fetches all the account having 0 followers and updates followers through Instaloader
```
### Jsonconvert.py
```
This fetches account having particular trust value and followers from database and creates a JSON file.
```
### bubble.js
```
This generates our Frontend containg bubbles sized according to the followers value
```
### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python
* Sqlite
* Instaloader

<p align="right">(<a href="#top">back to top</a>)</p>



