# VirtualTA
Virtual Teaching Assistant which is a RAG Model that answers on Course Content and Discourse.

# *Main Functionality* API that can automatically answer student questions on their behalf based on:
-Course content with content for TDS Jan 2025 as on 15 Apr 2025.
-TDS Discourse posts with content from 1 Jan 2025 - 14 Apr 2025.

# Explaining all Functionalities
  - *get_content.py* - Gets Markdown Files out of the Discourse Forum across a Date Range. Also, It fetches all the image data present in the post.
    - Parameters : Date Range [Start Data & End Date] & Forum Cookie String

  - *embed_all_files.py* - Creates Chunks and Embeddings of the Markdown content

  - *get_answers.py* - has a Fast API POST End Point ('/api/'). Gets Parameters like Question, Image & Link,Extracts Data if the content type is Image and Then Searches the Embeddings for the closest result.
