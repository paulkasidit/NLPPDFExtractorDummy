What does this program do?
------------------

Quick summarization:
------------------

This program extracts text from a PDF file (located in the "input" directory), takes text out of the PDF file, cleans the text, and once again put the completed text file into a directory titled and puts the completed results into the "output" directory . 

Simple breakdown on how this all works:
------------------

- PDF file is put into the "input folder" to be processed. 
- The program loops to check in current working directory if the "output" directory exists, if not it creates it. 
- With the OS module, an empty text file called "output.txt" is created, ready for writing. 
- The uncleaned extracted text is written into "output.txt". 
- Now we move onto text cleaning with the Natural Language Toolkit (nltk). Some text cleaning processes include tokenizing, removing special characters, removing stopwords (words such as "an", "and", etc).
- We clear the original content (the uncleaned text), and write the new and cleaned text into it instead.
- We save and close the file. (This is the latest step so far). 


Requirements (Modules and APIs and how they were used in the parantheses.)
------------------

- OS (Used for creating a new file and directory, and writing into the newly created file.)
- Slate (Extracting text from PDF)
- Json (This will be used later for creating a JSON and populating it with extracted data.)
- String (This is used to convert to PDF file into a string object, this is required for further steps.)
- nltk (Natural Language Tool Kit) (Used for cleaning text)
- PorterStemmer (Stems text, it may be removed)
- re 

What worked and what did not?
------------------

Converting Text:
- WORKS: Slate is better than PyPDF2 because the latter was not able to extract texts from PDF. 

Cleaning Text: 
- FAIL: The stemming of the texts made the words difficult to read, and may not be effective in later stages. (e.g. "Thailand" became "Thlnd". etc. )

Engineering:
- FAIL: The engineering (or structure) of this program is still poor. Please do let me know of any suggestions you could make in order to improve runtime. Maybe put everything into a function? 

Unfulfilled Tasks
------------------
- Recognize entities from text and assign them to the correct entities. 
- Creating a JSON file. 

# NLPPDFExtractorDummy
# NLPPDFExtractorDummy # NLPPDFExtractorDummy
# NLPPDFExtractorDummy # NLPPDFExtractorDummy
