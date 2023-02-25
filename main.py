import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from gtts import gTTS


def all2speech(epub_path: str, mp3_path: str, lang='zh-TW'):
    from epub2txt import epub2txt

    # get all paragraphs in the book
    text = epub2txt(epub_path)
    # turn the text into speech
    t2s = gTTS(text, lang=lang)
    # save the audio file
    t2s.save(mp3_path)


def sections2speech(epub_path: str, mp3_path: str, section_nums: list, lang='zh-TW'):
    # Read in the EPUB file
    book = epub.read_epub(epub_path)
    # Extract the paragraphs from specified sections in the book
    paragraphs = []
    for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
        if i in section_nums:
            content = item.get_content().decode('utf-8')
            soup = BeautifulSoup(content, 'html.parser')
            # get all texts under <body> tag, the tags vary in books.
            paragraphs += [p.text for p in soup.find_all('body')]
    text = ''.join(paragraphs)
    t2s = gTTS(text, lang=lang)
    t2s.save(mp3_path)


if __name__ == '__main__':

    b_path = 'book.epub'
    audio_path = 'book_section_19-23.mp3'
    sections = [i for i in range(19, 24)]
    sections2speech(b_path, audio_path, sections)
