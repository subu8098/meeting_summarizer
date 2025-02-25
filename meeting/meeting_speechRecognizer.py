import speech_recognition as sr
import ollama
import time

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to summarize text using Ollama
def summarize_text(text):
    model = "gemma2:2b"  # Change to "mistral", "gemma", etc.
    response = ollama.chat(model=model, messages=[{"role": "user", "content": f"Summarize this: {text}"}])
    return response['message']['content']

# Function to listen for 5 minutes, transcribe, and summarize
def listen_transcribe_summarize():
    with sr.Microphone() as source:
        print("Listening... Speak freely for 5 minutes.")

        recognizer.adjust_for_ambient_noise(source)  # Helps filter background noise
        
        start_time = time.time()
        silence_timeout = 40  # Stop if silent for 40 seconds
        last_speech_time = start_time
        audio_data = []

        try:
            while (time.time() - start_time) < 5 * 60:
                print("Listening...")
                audio = recognizer.listen(source)  # Capture speech
                audio_data.append(audio)

                if (time.time() - last_speech_time) > silence_timeout:
                    print("No speech detected for 40 seconds. Stopping early.")
                    break

                last_speech_time = time.time()

        except KeyboardInterrupt:
            print("Listening manually stopped.")

    print("Finished listening. Transcribing audio...")

    transcribed_text = ""
    for audio_chunk in audio_data:
        try:
            text = recognizer.recognize_google(audio_chunk)
            transcribed_text += " " + text
        except sr.UnknownValueError:
            print("Could not understand some audio parts.")
        except sr.RequestError:
            print("Could not request results.")

    if transcribed_text:
        print("\nFull Transcription:\n", transcribed_text)
        print("\nSummarizing text...")

        summary = summarize_text(transcribed_text)
        print("\nSummary:\n", summary)
    else:
        print("No speech detected, nothing to summarize.")

# Run the process
listen_transcribe_summarize()
