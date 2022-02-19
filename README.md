<p align="center">
  <h3 align="center">Piper</h3>
  <p align="center">Remote Access Tool that uses steganography to keep it's malicious codes.</p>
  <p align="center">
    <a href="https://www.python.org/">
      <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
    </a>
  </p>
</p>

<hr>


__Disclaimer:__ This project should be used for authorized testing or educational purposes only. :shipit:


## About

### ://Name 

The name of this project was inspired by the [Pied Piper of Hamelin](https://en.wikipedia.org/wiki/Pied_Piper_of_Hamelin).

### ://Project

The idea of this project is to create a RAT that does not contain any malicious code embedded on it, keeping it as undetectable as possible. Any suspicious code will be stored encrypted in images and will be loaded on runtime.


## Install & Run

Use the pre written script to initialize install the required products and setup your environment. Then activate the virtual environment.

### Building project
```sh
$ chmod +x install.sh
$ ./install.sh
$ . ./activate
```

### Generating a payload
```sh
$ python piper.py
```