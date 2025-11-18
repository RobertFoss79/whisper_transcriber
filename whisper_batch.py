import whisper
import time
import os
import glob

# --- CONFIGURATION ---
# The folder where you drop your MP3s
SOURCE_FOLDER = r"C:\Users\Rober\Desktop\todo"

# The folder where the text files will be saved
OUTPUT_FOLDER = r"C:\Users\Rober\Desktop\Transcribed Lessons"

MODEL_SIZE = "large" 
OUTPUT_FILE_SUFFIX = '_output.txt'
# ---------------------

def transcribe_batch():
    # 1. Check/Create Output Directory
    if not os.path.exists(OUTPUT_FOLDER):
        print(f"Creating output directory: {OUTPUT_FOLDER}")
        os.makedirs(OUTPUT_FOLDER)

    # 2. Load the model ONCE before the loop starts
    print(f"Loading {MODEL_SIZE} model... (This happens only once)")
    try:
        # Keeping device="cuda" based on your previous snippet. 
        # If you have specific GPU errors, change "cuda" to "cpu".
        model = whisper.load_model(MODEL_SIZE, device="cuda")
    except Exception as e:
        print(f"Error loading model on CUDA: {e}")
        print("Falling back to CPU (this will be slower)...")
        model = whisper.load_model(MODEL_SIZE, device="cpu")

    # 3. Find all .mp3 files in the source folder
    # using glob to find files ending in .mp3 inside the folder
    search_path = os.path.join(SOURCE_FOLDER, "*.mp3")
    files = glob.glob(search_path)
    
    total_files = len(files)
    print(f"\nFound {total_files} files in {SOURCE_FOLDER}\n")

    if total_files == 0:
        print("No MP3 files found. Please check the folder path.")
        return

    # 4. Loop through each file
    for index, audio_file_path in enumerate(files):
        file_name = os.path.basename(audio_file_path)
        
        print(f"--- Processing {index + 1}/{total_files}: {file_name} ---")
        
        # Define the output filename
        base_name = os.path.splitext(file_name)[0]
        output_filename = base_name + OUTPUT_FILE_SUFFIX
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        # Skip if already exists? (Optional: currently overwrites to be safe)
        # if os.path.exists(output_path):
        #     print(f"Skipping {file_name}, output already exists.")
        #     continue

        start_time = time.time()

        try:
            # Transcribe
            # fp16=False helps avoid warnings/errors on some CPUs or specific GPUs
            result = model.transcribe(audio_file_path, fp16=False, verbose=True)

            # Save the output to the specific destination folder
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])

            elapsed_time = (time.time() - start_time) / 60
            print(f"Finished {file_name}. Saved to: {output_filename}")
            print(f"Time taken: {elapsed_time:.2f} minutes\n")

        except Exception as e:
            print(f"FAILED to transcribe {file_name}")
            print(f"Error: {e}\n")

    print("--- Batch Transcription Complete ---")

if __name__ == "__main__":
    transcribe_batch()