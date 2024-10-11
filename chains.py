import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def get_resume_data(self, resume_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### Find Extracted Resume Text Below:
            {resume_data}
            ### INSTRUCTION:
            The scraped text is from the candidate's resume file.
            Your job is to extract the important data related to candidate in JSON format containing the following keys: 
            `name`, `email`, `contact number`, `job title`, `education`, `experience`, `skills`, `address`.
            add anyother important info. if available.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"resume_data": resume_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
