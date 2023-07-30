import nbformat as nbf

# Function to create code cell
def create_code_cell(code):
    return nbf.v4.new_code_cell(source=code)

# Function to create markdown cell
def create_markdown_cell(text):
    return nbf.v4.new_markdown_cell(source=text)

# Notebook structure
notebook_content = [
    create_markdown_cell("## Game of Thrones Dialogue Analysis\n\nThis notebook contains the analysis of dialogue in the Game of Thrones sample conversation."),
    create_code_cell('''
def get_unique_speakers(filename):
    unique_speakers = set()
    with open(filename, 'r') as file:
        for line in file:
            if line.strip().endswith(":"):
                speaker = line.strip()[:-1]
                unique_speakers.add(speaker)
    return unique_speakers

def create_speaker_files(filename):
    speakers = {}
    with open(filename, 'r') as file:
        current_speaker = None
        for line in file:
            if line.strip().endswith(":"):
                current_speaker = line.strip()[:-1]
                speakers[current_speaker] = set()
            else:
                if current_speaker:
                    words = line.strip().split()
                    for word in words:
                        cleaned_word = word.strip(".,!?\":;")
                        if cleaned_word:
                            speakers[current_speaker].add(cleaned_word.lower())

    for speaker, words in speakers.items():
        with open(f"{speaker}.txt", 'w') as outfile:
            for word in words:
                outfile.write(word + '\\n')

# Task 1: Find out the number of unique dialogue speakers
input_file = "conv.txt"
unique_speakers = get_unique_speakers(input_file)
num_unique_speakers = len(unique_speakers)
print(f"Number of unique dialogue speakers: {num_unique_speakers}")

# Task 2: Create a new text file for each speaker containing their unique words
create_speaker_files(input_file)
print("Text files for each speaker created successfully.")
    ''')
]

# Create the notebook
notebook = nbf.v4.new_notebook(cells=notebook_content)

# Save the notebook to a file
file_path = "game_of_thrones.ipynb"
with open(file_path, "w", encoding="utf-8") as f:
    nbf.write(notebook, f)

print(f"Notebook '{file_path}' created successfully.")