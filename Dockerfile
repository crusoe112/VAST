from python:3.10
ADD vigilant_session_interview_question_2.py /vigilant_session_interview_question_2.py

RUN RANDOM_SEED=$(od -vAn -N2 -tu2 < /dev/urandom |xargs) \
    && echo -n "$RANDOM_SEED" > seed

CMD ["python", "./vigilant_session_interview_question_2.py"]

