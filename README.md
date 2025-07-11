# 📰 Text Summarizer: End-to-End Project.

This project demonstrates an **end-to-end NLP pipeline** to perform **abstractive text summarization** using the **`google/pegasus-cnn_dailymail`** model from [Hugging Face 🤗](https://huggingface.co/google/pegasus-cnn_dailymail). PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive Summarization Sequence-to-Sequence models) is designed specifically for summarization tasks.

- Summarizing large documents, articles, or news.
- Building LLM-based assistants or pipelines for research.
- Content compression in email/news/chat applications.

---

### 🚀 Features

- 📚 Uses PEGASUS: state-of-the-art pre-trained transformer for summarization.
- 🔧 Clean, notebook-based implementation.
- 💡 Modular & extendable for web deployment (Streamlit/FastAPI).
- 🧪 Easy experimentation with long texts.
- 📦 Hugging Face integration (no training required).

---

### 📁 Project Structure
```
├───.github
│   └───workflows
├───config
├───research
├───src
│   ├───textSummarizer
│   │   ├───components
│   │   ├───config
│   │   ├───constants
│   │   ├───entity
│   │   ├───logging
│   │   ├───pipeline
│   │   ├───utils
```

The project structure is organized as follows:

- ```config.yaml```: Configuration file that contains project-specific settings and parameters.
- ```research```: Contains notebook experiments which were performed before modular code implementation
- ```params.yaml```: Parameter file that stores model-specific parameters and configurations.
- ```entity```: Directory containing entity definitions and related files.
- ```src/config```: Directory containing the configuration manager for accessing project configurations.
- ```components```: Directory containing various components used in the text summarization pipeline.
- ```pipeline```: Directory containing the main text summarization pipeline implementation.
- ```main.py```: Main script that orchestrates the text summarization process.

---

### 🛠️ Tech Stack

| Tool           | Purpose                                |
|----------------|----------------------------------------|
| Python 🐍       | Programming Language                   |
| HuggingFace 🤗  | Pretrained Transformer Library         |
| PEGASUS 🧠       | Abstractive Text Summarization Model   |
| Jupyter 📒      | Notebook-based Workflow                |

---

### 🔍 Model Details

- **Model Name**: [`google/pegasus-cnn_dailymail`](https://huggingface.co/google/pegasus-cnn_dailymail).
- **Type**: Transformer-based Seq2Seq.
- **Task**: Abstractive Summarization.
- **Dataset**: CNN / DailyMail News Articles.
- **Tokenizer**: SentencePiece.

---


### 📌 Sample Result

**Input**
> "NASA’s upcoming mission is scheduled for 2027. The agency is designing a new telescope capable of exploring deeper regions of space and potentially identifying signs of life on exoplanets..."

**Summary**
> "NASA plans to launch a new telescope in 2027 to explore deep space and search for extraterrestrial life."

---

### 🔮 Future Enhancements

- 🌐 Add a Streamlit UI to upload articles and generate summaries live.
- 📁 Support for PDF/Text file input.
- 🧾 Add batch processing mode for summarizing multiple documents.
- ⚡ Deploy as a REST API using FastAPI.


---

### 🙌 Ideal For
- Data Science Portfolio Projects
- Educational Research Analytics
- Deployment Practice with Streamlit
- Interview preparation (EDA → Modeling → Deployment flow)

### 📫 Connect with Me

- LinkedIn: [Hariharan Balasubramanian](https://www.linkedin.com/in/hariharan-balasubramanian97)
- Email: hariharanbalasubramanian4@gmail.com

---

### ⭐ If You Like This Project
If this project helped or inspired you, please ⭐ star the repo and share it!


---


### 🙏 Thank You...!!!
