from pdfminer.high_level import extract_text
from chains import Chain


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
 
if __name__ == '__main__':
    chain = Chain()
    resume_text = extract_text_from_pdf(r"sample-data/resume.pdf")

    response = chain.get_resume_data(resume_text)
    print(response)