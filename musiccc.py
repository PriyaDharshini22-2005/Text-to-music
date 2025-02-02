import streamlit as st
from music21 import stream, note, chord

# Function to map the text to music notes
def text_to_music(text):
    # Mapping each letter of the alphabet to a musical note
    note_mapping = {
        'a': 'C4', 'b': 'D4', 'c': 'E4', 'd': 'F4', 'e': 'G4', 'f': 'A4', 'g': 'B4',
        'h': 'C5', 'i': 'D5', 'j': 'E5', 'k': 'F5', 'l': 'G5', 'm': 'A5', 'n': 'B5',
        'o': 'C6', 'p': 'D6', 'q': 'E6', 'r': 'F6', 's': 'G6', 't': 'A6', 'u': 'B6',
        'v': 'C7', 'w': 'D7', 'x': 'E7', 'y': 'F7', 'z': 'G7', ' ': 'R'  # R for rest (pause)
    }

    music_stream = stream.Stream()

    for char in text.lower():  # Process each character
        if char in note_mapping:
            note_name = note_mapping[char]
            if note_name == 'R':
                music_stream.append(note.Rest())
            else:
                music_stream.append(note.Note(note_name, quarterLength=1))
    
    return music_stream

# Function to play the generated music
def play_music(music_stream):
    music_stream.show('midi')  # Opens MIDI player to play the music

# Function to save music as a MIDI file
def save_music_as_audio(music_stream, output_path):
    music_stream.write('midi', fp=output_path)

# Streamlit interface for user input
st.title("Text to Music Chatbot")

# Chatbot prompt
user_input = st.text_input("Enter some text to convert it into music:")

if user_input:
    # Generate music from the entered text
    extracted_text = user_input
    st.write(f"Entered Text: {extracted_text}")
    
    # Generate music based on the input text
    music_stream = text_to_music(extracted_text)
    st.write("Generated Music Based on Entered Text:")
    
    # Play the generated music
    if st.button("Play Music"):
        play_music(music_stream)
    
    # Save as a MIDI file
    midi_path = "generated_music.mid"
    save_music_as_audio(music_stream, midi_path)
    st.download_button("Download MIDI File", midi_path)
