# Text to Music Chatbot

This project converts input text into music by mapping each letter of the alphabet to a specific musical note. It uses the **music21** library for generating the musical notes and **Streamlit** for the user interface. The generated music can be played directly in the browser or downloaded as a MIDI file.

## Features

- **Text to Music Conversion**: Each letter of the alphabet corresponds to a specific musical note.
- **Music Playback**: The generated music can be played directly within the app.
- **MIDI File Download**: You can download the generated music as a MIDI file.

## Technologies Used

- **Python**: Programming language used for the development of the project.
- **Streamlit**: A Python library for creating interactive web applications.
- **music21**: A Python library used for music analysis and creation.
  
## Setup Instructions

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:
    ```bash
    pip install streamlit music21
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. The app will open in your web browser. Enter some text, and it will convert it to music!

## How It Works

1. **Text Input**: The user enters some text into the input box.
2. **Mapping**: Each letter of the alphabet is mapped to a musical note (e.g., 'a' → 'C4', 'b' → 'D4', etc.).
3. **Music Generation**: The corresponding notes are generated and added to a musical stream.
4. **Playback**: The user can listen to the generated music by clicking the "Play Music" button.
5. **MIDI File Download**: Users can download the generated music as a MIDI file.

## Example

For example, if you input the word `hello`, the corresponding musical notes will be generated and played. You can also download the music as a `.mid` file.

## Below are the snapshots of the output

<img width="956" alt="image" src="https://github.com/user-attachments/assets/419caaa3-241c-429a-a8c5-009c23135c39" />

<img width="959" alt="image" src="https://github.com/user-attachments/assets/1c8acda7-253f-4ce7-b5cd-1d8838409cc8" />



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact priyadharshinikameswaran@gmail.com



