# LAB - Class 16

## Project:  Serverless Functions

### Author: Johnny Backus

### Links and Resources

- [CodeFellows Python Lab Instructions](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/)
- [CodeFellows README template](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/README-template.html)
- [ChatGPT chat](https://chat.openai.com/c/cf341bae-d9b2-4aa6-83d0-f84f87221723)
- Also used ChatGPT to troubleshoot accessing desired data from json file.

- [Back-end server: Vercel](https://capital-finder-one-sigma.vercel.app/api)

### Setup

*.env requirements*
    - n/a

### How to initialize/run your application (where applicable)

1. import requests
2. npm install -g vercel (optional)
3. Access back-end server link above.
4. Test API and methods using browser. Below are some samples that demonstrate working code.
    - [test: Chile](https://capital-finder-one-sigma.vercel.app/api/by_name?name=Chile)
    - [test: Madagascar](https://capital-finder-one-sigma.vercel.app/api/by_name?name=Madagascar)
    - [test: Lima](https://capital-finder-one-sigma.vercel.app/api/by_capital?capital=Lima)
    - [test: Tokyo](https://capital-finder-one-sigma.vercel.app/api/by_capital?capital=Peru)
    - [test: Typo](https://capital-finder-one-sigma.vercel.app/api/by_name?name=Typo)
    - [test: Typo2](https://capital-finder-one-sigma.vercel.app/api/by_capital?capital=Typo2)
