🚀 Building an AI Agent for Meeting Summarization 🎙️📄
In my journey to develop an AI-powered Meeting Summarization Agent, I explored multiple approaches to capture and transcribe audio efficiently. Here’s what I discovered:

🔍 Three Approaches I Explored
1️⃣ SpeechRecognition for both listening & transcription

Used speech_recognition to capture and transcribe external microphone audio.
Faced challenges with noisy environments and inconsistent accuracy.
![image](https://github.com/user-attachments/assets/c1cc7283-a690-4fe2-98a1-50adce95ee28)

2️⃣ SpeechRecognition for listening & OpenAI's Whisper for transcription

Combined speech_recognition for capturing and Whisper for transcription.
Whisper significantly improved accuracy but still required an external microphone.
![image](https://github.com/user-attachments/assets/eec9a4ee-d4ad-4cd5-bbcb-9d9011c17813)

3️⃣ Capturing System Audio using Stereo Mix & Whisper for Transcription

Leveraged Stereo Mix to capture internal system audio.
Used Whisper for transcription, overcoming microphone dependency.
Integrated Ollama (Llama 3.2) for AI-powered summarization.
Successfully built a real-time AI agent that listens to meetings, transcribes, and generates concise summaries.
💡 Challenges & Breakthroughs
🔹 Detecting system audio input via Stereo Mix setup.
🔹 Ensuring long-duration listening with a 40s silent timeout for efficient processing.
🔹 Optimizing Whisper transcription for high accuracy.
🔹 Summarizing meeting transcripts using Ollama's LLM to generate key insights.
![image](https://github.com/user-attachments/assets/a4e45e72-682c-4196-a78e-986c61d87a55)

🎯 Final Outcome
With this setup, I successfully implemented an AI-powered Meeting Summarization Agent that listens to internal system audio, transcribes it using Whisper, and generates concise summaries using Llama 3.2.
