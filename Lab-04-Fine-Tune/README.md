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

Qwen/Qwen2.5-0.5B-Instruct

## Dataset

A custom dataset containing 30 question-and-answer pairs based on a fictional computer shop named TechZone.

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
