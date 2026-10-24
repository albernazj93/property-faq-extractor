# This repository contains a project that receives a document (pdf, png, docx, text) and return a list of FAQ (questions, answers, citations). It utilizes an LLM to read and extract the content by specifying what it needs to do in a prompt.

## INPUT

User can input multiple documents at the time of any supported format that contains houses rules, contracts, guideline, recommendations, etc.

### Formats

- PDF
- PNG
- Docx
- Free text

## OUTPUT

It returns a list of FAQ (question, answer, citations) in JSON format. 

### Properties

- Question - A question that may have been extracted and reworded, or simply created to answer an affirmation from the text.
- Answer - An extracted answer that may have been reworded taken from an affirmation in the text. 
- Citations - A list that contains the original document texts that the LLM used to created the question and answer. 

### Example

'''
[
    {
        "question":"Qual a rede e senha do WiFi?",
        "answer":"Rede 701 ou 701 2G. Senha: cerimonial",
        "citation":[
            "701 / 701 2G Senha: cerimonial"
        ]
    },
    {
        "question":"Como entrar no prédio?",
        "answer":"Use o tag azul na 1ª porta; empurre, a 2ª abre sozinha",
        "citation":[
            "Posicione o tag azul para abrir a primeira porta de vidro, empurre a porta e automaticamente irá abrir a segunda porta."
        ]
    },
    {
        "question":"Como abrir a porta do apartamento?",
        "answer":"Não usar a fechadura da parte superior",
        "citation":[
            "Porta do apartamento: não usar a fechadura da parte superior."
        ]
    }
]
'''

## INVOCATION

This project is built in Python which can be easily deployed on AWS as a Lambda function. Once deployed, it can be invoked in many different ways such as Lambda URL directly, EventBridge/S3 in an event driven architecture once a file lands in S3 or anything else happens in the environment, an external API using API Gateway, etc.
In this project we will be invoking the Python files manually for test and learning purpose.

## ERROR TREATMENT

Once an error happens we will be notifying whoever/whatever is invoking the application by throwing an exception or simply adding a message to the returned object depending on the criticality of the issue. Some of the errors that may happen: document with unreadable texts, incomplete answers, invalid citations, duplicated answers/questions, limited tokens, unresponsive LLM, etc.

## TODO

Limit the size of the object the end user can submit. We want to keep the cost at minimum until we learn more how the tool is behaving and costing. 