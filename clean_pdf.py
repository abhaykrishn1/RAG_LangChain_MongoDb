# load the pdf using langchain
# print 1 page 
from langchain_community.document_loaders import PyPDFLoader

# Specify the path to your PDF file
file_path = "./data_sample/mongodb.pdf"

# Initialize the loader
loader = PyPDFLoader( file_path )

# Load and split the pages
pages = loader.load_and_split()

# Print content of the first page (index 0)
print(pages[0].page_content)
print(pages[1].page_content)


