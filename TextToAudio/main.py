import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('Chapter_1.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'Chapter_1.mp3')
speaker.runAndWait()

speaker.stop()