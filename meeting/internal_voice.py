import os
import speech_recognition as sr
import whisper
import ollama
import time

# Ensure FFmpeg is available
ffmpeg_path = r"D:\Meeting_summarizing\ffmpeg-7.1-full_build\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Load Whisper Model
whisper_model = whisper.load_model("small")  # Options: tiny, base, small, medium, large

# Initialize recognizer
recognizer = sr.Recognizer()

# Specify the correct device index for Stereo Mix
device_index = 1  # Adjust based on your system audio list

# Function to summarize text using Ollama
def summarize_text(text):
    model = "llama3.2"  # Change if needed (mistral, gemma, etc.)
    prompt = (
        "Summarize this meeting transcript and provide a concise short note with key points:\n\n"
        f"{text}"
    )

    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        print("Error in summarization:", str(e))
        return "Summarization failed."

# Function to listen, transcribe using Whisper, and summarize
def listen_transcribe_summarize():
    with sr.Microphone(device_index=device_index) as source:
        print("Listening to system audio...")

        recognizer.adjust_for_ambient_noise(source)  # Helps filter background noise

        start_time = time.time()
        silence_timeout = 40  # Stop if silent for 40 seconds
        last_speech_time = start_time
        audio_data = []

        try:
            while True:
                print("Listening for speech...")
                audio = recognizer.listen(source)  # Capture audio
                audio_data.append(audio)

                # Update last speech time when audio is captured
                last_speech_time = time.time()

                # Check for 40 seconds of silence
                if (time.time() - last_speech_time) > silence_timeout:
                    print("No speech detected for 40 seconds. Stopping recording.")
                    break

        except KeyboardInterrupt:
            print("Listening manually stopped.")

    print("Finished listening. Transcribing audio...")

    # Convert recorded audio to WAV for Whisper
    transcribed_text = ""
    for idx, audio_chunk in enumerate(audio_data):
        wav_filename = f"audio_chunk_{idx}.wav"

        with open(wav_filename, "wb") as f:
            f.write(audio_chunk.get_wav_data())

        try:
            # Transcribe using Whisper
            result = whisper_model.transcribe(wav_filename)
            transcribed_text += " " + result["text"]
        except Exception as e:
            print(f"Error in transcription of {wav_filename}: {str(e)}")

    if transcribed_text.strip():
        print("\nFull Transcription:\n", transcribed_text)

        # Summarize only after transcription completes
        print("\nSummarizing text...")
        summary = summarize_text(transcribed_text)
        print("\nSummary:\n", summary)
    else:
        print("No speech detected, nothing to summarize.")

# Run the process
listen_transcribe_summarize()
