from epub2txt import epub2txt
from gtts import gTTS

if __name__ == '__main__':

    # get all paragraphs in the book
    book = epub2txt('book_path')
    # turn the text into speech
    tts = gTTS(book, lang='zh-TW')
    # save the audio file
    tts.save('output.mp3')
