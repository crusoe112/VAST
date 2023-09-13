# Vigilant Cyber Systems Applicant Screening Challenge

## Introduction:
**Please read the challenge sections of this README before starting the challenges.**

This set of challenges is designed to test your ability to analyze source code and identify vulnerabilities. The challenges are designed to be similar to the types of vulnerabilities you may encounter during a pentest. You are also encouraged to automate the exploit process as much as possible.

Completing all challenges is not required. If you are unable to complete a challenge, please document your thought process and the steps you took in your attempt. You will be asked to explain your process during the interview later, so be sure to take good notes.

## Requirements:
- Python 3 - `sudo apt install python3`
- Docker - `sudo apt install docker.io && sudo systemctl enable docker --now`

## Challenge 1:

### Background:
During an authorized pentest, you have discovered a remotely accessible authentication service running on an IoT device within the corporate network. By analyzing the device firmware, you were able to discover the source code for the authentication service. The source code is written in Python and is available in the file `vigilant_session_interview_question_1.py`.

### Instructions:
Run the program with the command `python vigilant_session_interview_question_1.py`. The goal is to bypass the authentication mechanism and gain access to the device. You can play around with the source code all you want, but your final solution may not rely on modifying the source code. As you go, document your thought process and the steps you took to solve the challenge. You will be asked to explain your process during the interview later, so be sure to take good notes.

### Hints:
- Don't think too hard for this one. You don't need to be a crypto expert to solve this challenge. Bonus points for having a simple solution for this one.

### Troubleshooting:
- If you are having trouble running the program, make sure you have Python 3 installed. If you are still having trouble, reach out to us and we will help you out.

## Challenge 2:

### Background:
Great work on the last pentest! The company reached out to the vendor who implemented a solution to the authentication bypass vulnerability you discovered. The vendor says the new version uses military-grade encryption and doesn't use hardcoded values like the last one. Once again, you managed to gain access to the source code for the authentication service. The source code is written in Python and is available in the file `vigilant_session_interview_question_2.py`.

### Instructions:
This challenge is similar to the last one, but runs within a Docker container. Build the container with the command `docker build -t vigilant_session_interview_question_2 .` and then run it with the command `docker run --rm -it vigilant_session_interview_question_2` (you may need to run this command as root). The goal is to bypass the authentication mechanism and gain access to the device. You can play around with the Docker container, but your final solution must not rely on modifying the Python file, Dockerfile, or anything within the container. Make sure to document your process as you go. There are multiple solutions to this challenge. Bonus points for writing a script to automate the exploit.

### Hints:
- Look for any bugs that may make the encryption less secure.
- Think of what class of cipher is being used, and look for common vulnerabilities in that class.
- The crypto variables may no longer be hardcoded, but is there a way to discover them? (Note: getting it by poking around the container doesn't count)

### Troubleshooting:
- If you are having trouble running the program, make sure you have Docker installed. If you are still having trouble, reach out to us and we will help you out.
- If you are having trouble with the Dockerfile, make sure you are running the commands from the same directory as the Dockerfile.
- You may need to run Docker as root.