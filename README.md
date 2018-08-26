# TechcidoForYelp.com


Resource 'corpora/wordnet' not found

# Solution
So, supposing my python application is in a directory called "myapp/"
Step 1: Create the directory


cd myapp/


mkdir nltk_data


Step 2: Download Corpus to New Directory


python -m nltk.downloader


This'll pop up the nltk downloader. Set your Download Directory to whatever_the_absolute_path_to_myapp_is/nltk_data/


Step3: Let nltk Know Where to Look

ntlk looks for data,resources,etc. in the locations specified in the nltk.data.path variable. All you need to do is add nltk.data.path.append('./nltk_data/') to the python file actually using nltk, and it will look for corpora, tokenizers, and such in there in addition to the default paths.
