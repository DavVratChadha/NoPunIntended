# WhySoPunny
## Pun Detection using RoBERTa and DeBERTa
This repository contains code for implementing RoBERTa and DeBERTa models to locate puns in a given sentence. In addition to the pun detection script, it also includes scripts for collecting and preprocessing data to train, validate and test the models.

## Data Collection
The repository includes a Python script for web scraping data from social media platforms like Reddit. The script collects pun-related data and saves it to a text file for further processing.

## Data Preprocessing
The collected data is preprocessed using techniques such as tokenization and POS tagging to improve the accuracy of the models. The preprocessed data is included in the repository in the form of pickle files containing sentences annotated with the location of puns.

## Model Training and Testing
The preprocessed dataset is used to fine-tune and test pretrained RoBERTa and DeBERTa models for pun detection. The pun detection script uses the trained models to provide predictions and metrics for each input sentence, indicating the presence and location of puns. The script also includes functionality for evaluating the accuracy and performance of the models using various metrics.

## Usage
To use this repository, clone it to your local machine and run the scripts provided to collect, preprocess and train the data. The preprocessed dataset and trained models can then be used for pun detection.

## Conclusion
This repository provides a comprehensive set of tools for collecting, processing, and analyzing data related to puns in text, and can be used by researchers, data scientists, and NLP enthusiasts for further experimentation and development.
