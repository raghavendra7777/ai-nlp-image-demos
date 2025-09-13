# ai-nlp-image-demos
A collection of Python scripts demonstrating Natural Language Processing (NLP) and Generative AI tasks using Hugging Face Transformers and Diffusers. Includes text generation, summarization, question answering, sentiment analysis, named entity recognition (NER), and text-to-image generation with Stable Diffusion.
# 🚀 AI NLP & Image Generation Demos

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Transformers-yellow)](https://huggingface.co/transformers/)  
[![Diffusers](https://img.shields.io/badge/HuggingFace-Diffusers-orange)](https://huggingface.co/docs/diffusers)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A collection of **Natural Language Processing (NLP)** and **Generative AI** demos built with Hugging Face **Transformers** and **Diffusers**.  
This repository showcases hands-on implementations of **text generation, summarization, question answering, sentiment analysis, named entity recognition (NER),** and **AI-powered image generation** with Stable Diffusion.  

---

## 📂 Project Structure
```bash
.
├── test1.py     # Text Generation (GPT-2)
├── test2.py     # Text Summarization (BART)
├── test3.py     # Question Answering
├── test4.py     # Named Entity Recognition (NER)
├── test5.py     # Sentiment Analysis
├── deftest2.py  # Stable Diffusion Image Generation

✨ Features

📝 Text Generation → Creative writing with GPT-2

📚 Summarization → Extractive + abstractive summaries with BART

❓ Question Answering → Retrieve answers from given contexts

🏷️ Named Entity Recognition → Identify people, places, and organizations

😀 Sentiment Analysis → Classify text emotions with confidence scores

🎨 Stable Diffusion → Generate images from text prompts

⚡ Getting Started
1. Clone the repository
git clone https://github.com/your-username/ai-nlp-image-demos.git
cd ai-nlp-image-demos

2. Install dependencies
pip install -r requirements.txt


(You can also install directly if requirements.txt is not included):

pip install transformers diffusers torch accelerate


💡 Note: For Stable Diffusion, a CUDA-enabled GPU is recommended.

🚀 Usage

Run any of the demo scripts:

# Text Generation
python test1.py  

# Summarization
python test2.py  

# Question Answering
python test3.py  

# Named Entity Recognition
python test4.py  

# Sentiment Analysis
python test5.py  

# Image Generation with Stable Diffusion
python deftest2.py


When running deftest2.py, you’ll be prompted to enter a text description. An image will be generated and saved as generated_image.png.

📊 Example Outputs

🔹 Sentiment Analysis

Input: "kid is very bad and cunning guy"
Output: NEGATIVE (confidence: 0.99)


🔹 NER

Elon Musk -> PERSON (0.99)
SpaceX -> ORG (0.98)
USA -> LOC (0.97)


🔹 Summarization

"Alexander inherited a powerful army and pursued his father’s dream of conquering Persia."


🔹 Image Generation

Prompt: "A futuristic cityscape at sunset"
Output: generated_image.png (saved + displayed)

📖 Tech Stack

Python 3.8+

🤗 Transformers

🤗 Diffusers

PyTorch

🌟 Portfolio Value

This repo demonstrates:

Hands-on experience with Hugging Face’s most popular NLP pipelines

Integration of text-to-image generation models (Stable Diffusion)

Modular scripts useful for learning, experimenting, or extending into projects

🤝 Contributing

Pull requests, feature requests, and improvements are always welcome.

