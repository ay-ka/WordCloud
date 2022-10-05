<div id="top"></div>


[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ay-ka/WordCloud">
    <img style="float:left" src="images/wordcloud.jpg" alt="wordcloud" width="400" height="300">
    <img src="images/wordcloud.png" alt="wordcloud" width="400" height="300">
  </a>
  <h4 align="center">visual representation of words used to highlight popular words and phrases based on frequency and relevance</h4>
</div>

<br />
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Prerequisites-Installation">Prerequisites & Installation</a></li>
        <li><a href="#How-To-Run">How To Run</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


<div align="center">
<img src="images/screenshot.png" alt="wordcloud" width="300" height="300">
</div>
  
A word cloud (also known as a tag cloud) is a visual representation of words. Cloud creators are used to highlight popular words and phrases based on frequency and relevance. They provide you with quick and simple visual insights that can lead to more in-depth analyses.

<h6>(*** important: the project mainly developed for persian words but with selecting proper english font & adding proper stopwords, it works for          english data too)</h6>


<p align="right">(<a href="#top">back to top</a>)</p>



## Getting Started

this section explain instructions which should be followed to setting up the project. it is easier to run scripts from the terminal by passing arguments with the help of argparse library and this project also follow this pattern.

### Prerequisites-Installation

<ul>
  <li>
    there is a json format file inside <b>src/data</b> named <b>data</b>. it is initially used as sample data to create wordcloud. it can be replaced by       any other json format file extracted from <b>telegram</b> after cloning the repo. for doing so:
    <ol type="1">
      <li>enter a (chat\channel\group) in your telegram. on the right corner of the page, there is menu; open it</li>
      <li>on the opened menu, click on export chat history</li>
      <li>on the newely opened menu, click on export</li>
      <li>after finishing download, replace it with cs_stack</li>
    </ol>
  </li>
  <li>inside data directory, there is file named <b>font.ttf</b> which is used initially as a base font, it can be replaced by any other font file with .ttf format after cloning the repo</li>
  <li>inside <b>src/data folder</b>, there are two files <b>stopwords_per.txt</b> and <b>stopwords_en.txt</b>; if there are words that should be ignored and not displayed on theoutput result, those words could be added to these files on a seperate line for each word </li>
  <li>install all libraries specified whithin requirement.txt file on your virtual env</li>
</ul>

### How To Run

```sh
git clone https://github.com/ay-ka/WordCloud.git
cd WordCloud
export PYTHONPATH=$PWD
python src/main.py
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing


If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

aidin kazempour - [linkdin](https://www.linkedin.com/in/aidin-kazempour-b647811ba/) - aydinkazempour7@gmail.com

Project Link: [https://github.com/ay-ka/WordCloud](https://github.com/ay-ka/WordCloud)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [pytopia - a platform for learning python](https://www.pytopia.ai/)


<p align="right">(<a href="#top">back to top</a>)</p>


[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/aidin-kazempour-b647811ba/
[product-screenshot]: images/screenshot.png
