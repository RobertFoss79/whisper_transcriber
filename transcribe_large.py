import whisper
import time
import sys
import os

# --- CONFIGURATION ---
MODEL_SIZE = "large" 
OUTPUT_FILE_SUFFIX = '_output.txt'
# ---------------------

def transcribe_audio():
    # 1. Check for command line argument (argv)
    if len(sys.argv) < 2:
        print("Error: Please provide the audio file path as an argument.")
        print("Usage: python3 transcribe_large.py <audio_file_name.mp3>")
        sys.exit(1)

    # The audio file name is the second argument (sys.argv[1])
    audio_file_name = sys.argv[1]
    
    # Create the output file name based on the input file name
    base_name = os.path.splitext(audio_file_name)[0]
    output_file = base_name + OUTPUT_FILE_SUFFIX

    print(f"Loading {MODEL_SIZE} model...")
    start_time = time.time()

    try:
        # Load the model and force it to run on the CPU (to avoid the RTX 5070 Ti compatibility error)
        model = whisper.load_model("large", device="cuda") 
        
        print(f"Starting transcription for: {audio_file_name}...")

        # Run transcription, disabling FP16 to prevent the warning and ensure stable CPU processing
        result = model.transcribe(audio_file_name, fp16=False, verbose=True) 

        # Save the output
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        end_time = time.time()
        elapsed_time = (end_time - start_time) / 60

        print(f"\n--- Transcription Complete ---")
        print(f"Output saved to: {output_file}")
        print(f"Time elapsed: {elapsed_time:.2f} minutes")

    except FileNotFoundError:
        print(f"\nError: Audio file '{audio_file_name}' not found. Make sure it is in the current directory.")
        sys.exit(1)
    except Exception as e:
        print(f"\n--- Critical Error ---")
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    transcribe_audio()