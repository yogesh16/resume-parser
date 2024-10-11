# Resume Parser
Resume Parser for hiring company or HR department using groq, langchain. Simply provide Resume PDF file, it will extract candidate data, and provide you candidate data in JSON format. Which can be saved to Database or create a micro service API, where you can upload candidate's Resume PDF, and it will return candidate data in JSON format. 

# Setup
1. create `.env` file
```commandline
    cp example.env .env
```

2. It uses [groq](https://groq.com/), So first need to create `API_KEY` from here: https://console.groq.com/keys. Update `GROQ_API_KEY` value inside `.env` file.

3. Create a virtual environment called `venv`
```commandline
    python -m venv venv
```
Activate virtual enviroment
```commandline
   source ./venv/bin/activate
```

4. Install the dependencies using:
```commandline
    pip install -r requirements.txt
```

5. Run app
```commandline
    python main.py
```

## Sample Output
For provided sample resume pdf `sample-data/resume.pdf` JSON output
```commandline
   [{'name': 'John W. Smith', 'email': 'jwsmith@colostate.edu', 'address': '2002 Front Range Way, Fort Collins, CO 80525', 'job_title': 'Counseling Supervisor', 'education': [{'degree': 'BS', 'field': 'Early Childhood Development', 'university': 'University of Arkansas at Little Rock', 'year': 1999, 'gpa': 3.8}, {'degree': 'BA', 'field': 'Elementary Education', 'university': 'University of Arkansas at Little Rock', 'year': 1998, 'gpa': 3.5}], 'experience': [{'job_title': 'Counseling Supervisor', 'company': 'The Wesley Center', 'location': 'Little Rock, Arkansas', 'year': '1999-2002'}, {'job_title': 'Client Specialist', 'company': 'Rainbow Special Care Center', 'location': 'Little Rock, Arkansas', 'year': '1997-1999'}, {'job_title': 'Teacher’s Assistant', 'company': 'Cowell Elementary', 'location': 'Conway, Arkansas', 'year': '1996-1997'}], 'skills': ['Early Childhood Development', 'Special Needs Care', 'Client Management', 'Volunteer Management', 'Database Management', 'Communication'], 'awards': ['Dean’s List', 'Chancellor’s List']}]
```

## References

[Resume Parse Using Python](https://github.com/sanketsarwade/Resume-Parser-using-Python)

[Cold Email Generator](https://github.com/codebasics/project-genai-cold-email-generator).