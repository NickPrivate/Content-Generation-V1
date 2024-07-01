import threading
from scripts.scriptgen import generate_script

def print_stream(generator):
    for word in generator:
        print(word, end='', flush=True)

def main():
    word_count = input("Enter word count: ")
    prompt = input("Enter prmopt: ")
    our_prompt = f"{prompt} in {word_count} words"
    response_generator = generate_script(our_prompt)
    
    stream_thread = threading.Thread(target=print_stream, args=(response_generator,))
    stream_thread.start()
    

    stream_thread.join()
    print("\nStream completed.")

if __name__ == "__main__":
    main()
