<a id="readme-top"></a>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PensiveEagle">
    <img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/main/readme_assets/general_assets/pensiveeagle-logo-green.svg" alt="Pensive Eagle Logo" width="200" height="auto">
  </a>

<h3 align="center">Webcam Motion Detector</h3>

  <p align="center">
    A simple python app that uses a computer webcam to monitor for motion and sends an alert to a specified email address

  <!--  <a href="https://github.com/PensiveEagle/webcam-motion-detector"><strong>Explore the docs »</strong></a> -->
  <!--  <a href="https://github.com/PensiveEagle/webcam-motion-detector">View Demo</a>
    &middot;
    <a href="https://github.com/PensiveEagle/webcam-motion-detector/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/PensiveEagle/webcam-motion-detector/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple python app that uses a computer webcam to monitor for motion and sends an alert to a specified email address


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][python-shield]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.14
* Gmail Account
    * <a href="https://myaccount.google.com/apppasswords" target="_blank">Gmail Application Password</a>

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PensiveEagle/webcam-motion-detector.git
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create an `.env` file at the application root directory
5. Add the following values to the `.env` file
   ```
   GMAIL_PASSWORD = "<your-gmail-app-password>"
   SENDER_EMAIL = "<your-gmail-address>"
   RECIPIENT_EMAIL = "<email-address-for-alerts>"
   EMAIL_FREQUENCY = 60
   ```
   `EMAIL_FREQUENCY` is set to 60 here so emails are sent every 60 seconds if motion is detected. You can change this to change the frequency of emails.
6. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin PensiveEagle/webcam-motion-detector
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Run the app
   ```sh
   python app.py
   ```
2. The webcam video should show in a pop-out window and any motion detected should show in green boxes emails will be sent automatically when motion is detected at the frequency set in the `.env` file

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Python Mega Course: Build 20 Real-World Apps and AI Agents - Ardit Sulce](https://www.udemy.com/course/the-python-mega-course/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<div align="center"><img src="https://raw.githubusercontent.com/PensiveEagle/repo-assets/869e68466915785fdc1c44c324f2d84de119e5f1/readme_assets/general_assets/makers_mark_circle.svg" width="50"></div>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PensiveEagle/webcam-motion-detector.svg?style=for-the-badge
[contributors-url]: https://github.com/PensiveEagle/webcam-motion-detector/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PensiveEagle/webcam-motion-detector.svg?style=for-the-badge
[forks-url]: https://github.com/PensiveEagle/webcam-motion-detector/network/members
[stars-shield]: https://img.shields.io/github/stars/PensiveEagle/webcam-motion-detector.svg?style=for-the-badge
[stars-url]: https://github.com/PensiveEagle/webcam-motion-detector/stargazers
[issues-shield]: https://img.shields.io/github/issues/PensiveEagle/webcam-motion-detector.svg?style=for-the-badge
[issues-url]: https://github.com/PensiveEagle/webcam-motion-detector/issues
[license-shield]: https://img.shields.io/github/license/PensiveEagle/webcam-motion-detector.svg?style=for-the-badge
[license-url]: https://github.com/PensiveEagle/webcam-motion-detector/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jameshall-profile
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[kubernetes-shield]: https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white
[kubernetes-url]: https://kubernetes.io/
[docker-shield]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[streamlit-shield]: https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[streamlit-url]: https://streamlit.io/
[python-shield]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org/
[gradio-shield]: https://img.shields.io/badge/gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white
[gradio-url]: https://www.gradio.app/
[flask-shield]: https://img.shields.io/badge/flask-3BABC3?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/stable/
[jupyter-shield]: https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white
[jupyter-url]: https://jupyter.org/

---
# References

1. [[Software Development]]