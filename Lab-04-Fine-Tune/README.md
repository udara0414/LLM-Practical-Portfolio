
# Lab 04 – Fine-Tuning an LLM using LoRA/QLoRA

## Overview

This practical focuses on fine-tuning a small instruction-tuned Large Language Model using Parameter-Efficient Fine-Tuning (PEFT).

## Objectives

- Install the required libraries.
- Check GPU availability and memory.
- Select a suitable pre-trained language model.
- Create a domain-specific Q&A dataset containing at least 30 pairs.
- Configure LoRA and QLoRA with 4-bit quantization.
- Fine-tune the model using SFTTrainer.
- Evaluate and compare the original and fine-tuned models.

## Model

- **Model:** Qwen/Qwen2.5-0.5B-Instruct

## Dataset

A custom dataset containing 30 question-and-answer pairs based on a fictional computer shop named TechZone.

- Total Q&A pairs: 30
- Training samples: 24
- Evaluation samples: 6

## GPU Environment

- **GPU:** NVIDIA Tesla T4
- **GPU Memory:** Approximately 14.56 GB

A GPU accelerates matrix computations and helps reduce the time required for LLM fine-tuning.

## Fine-Tuning Configuration

- Method: QLoRA
- Quantization: 4-bit NF4
- LoRA rank: 8
- LoRA alpha: 16
- LoRA dropout: 0.05
- Training epochs: 3
- Learning rate: 2e-4
- Training framework: Hugging Face TRL SFTTrainer

## Evaluation Results

- Training loss: 3.0261
- Evaluation loss: 2.3823
- Mean token accuracy: 62.76%
- Independent unseen questions tested: 5

## Model Comparison

The original and fine-tuned models were tested using the same questions, including independent unseen questions.

The fine-tuned model generated more concise responses in some cases and provided more specific computer maintenance examples. However, some responses contained irrelevant or inaccurate information.

These results demonstrate domain adaptation through fine-tuning, while highlighting the need for further improvements and evaluation.

## Tools and Technologies

- Python
- Google Colab
- Hugging Face Transformers
- Hugging Face Datasets
- PEFT
- TRL
- Accelerate
- BitsAndBytes

## Project Structure

- `notebooks/` – Fine-tuning implementation.
- `screenshots/` – Practical implementation evidence.

## Status

Completed

