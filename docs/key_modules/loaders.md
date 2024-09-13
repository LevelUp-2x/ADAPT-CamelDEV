Skip to main content

__Back to top

__ `Ctrl`+`K`

[ ![](https://raw.githubusercontent.com/camel-
ai/camel/master/misc/primary_logo.png) CAMEL 0.1.9 ](../index.html)

Get Started

  * [Installation and Setup](../get_started/setup.html)

Agents

  * [Creating Your First Agent](../agents/single_agent.html)
  * [Creating Your First Agent Society](../agents/role_playing.html)
  * [Embodied Agents](../agents/embodied_agents.html)
  * [Critic Agents and Tree Search](../agents/critic_agents_and_tree_search.html)

Key Modules

  * Loaders
  * [Storages](storages.html)
  * [Embeddings](embeddings.html)
  * [Retrievers](retrievers.html)

Tutorial and Cookbooks

  * [🐫 Agents with RAG](../tutorials_and_cookbooks/agents_with_rag.html)

API References

  * [camel](../modules.html) __
    * [Camel Package](../camel.html) __
      * [camel.agents package](../camel.agents.html)
      * [camel.prompts package](../camel.prompts.html)

__

  * [ __ .md ](../_sources/key_modules/loaders.md "Download source file")
  * __ .pdf

__

# Loaders

##  Contents

  * 1\. Concept
  * 2\. Types
    * 2.1. Base IO
    * 2.2. Unstructured IO
  * 3\. Get Started
    * 3.1. Using `Base IO`
    * 3.2. Using `Unstructured IO`

# Loaders#

## 1\. Concept#

CAMEL introduced two IO modules, `Base IO` and `Unstructured IO` which are
designed for handling various file types and unstructured data processing.

## 2\. Types#

### 2.1. Base IO#

Base IO module is focused on fundamental input/output operations related to
files. It includes functionalities for representing, reading, and processing
different file formats.

### 2.2. Unstructured IO#

Unstructured IO module deals with the handling, parsing, and processing of
unstructured data. It provides tools for parsing files or URLs, cleaning data,
extracting specific information, staging elements for different platforms, and
chunking elements. The core of this module lies in its advanced ETL
capabilities to manipulate unstructured data to make it usable for various
applications like Retrieval-Augmented Generation(RAG).

## 3\. Get Started#

### 3.1. Using `Base IO`#

This module is designed to read files of various formats, extract their
contents, and represent them as `File` objects, each tailored to handle a
specific file type.

    
    
    from io import BytesIO
    from camel.loaders import read_file
    
    # Read a pdf file from disk
    with open("test.pdf", "rb") as file:
        file_content = BytesIO(file.read())
        file_content.name = "test.pdf"
    
    # Use the read_file function to create an object based on the file extension
    file_obj = read_file(file_content)
    
    # Once you have the File object, you can access its content
    print(file_obj.docs[0]["page_content"])
    

### 3.2. Using `Unstructured IO`#

To get started with the `Unstructured IO` module, you first need to import the
module and initialize an instance of it. Once initialized, you can utilize
this module to handle a variety of functionalities such as parsing, cleaning,
extracting data, and integrating with cloud services like AWS S3 and Azure.
Here’s a basic guide to help you begin:

Utilize `parse_file_or_url` to load and parse unstructured data from a file or
URL

    
    
    # Set example url
    example_url = (
        "https://www.cnn.com/2023/01/30/sport/empire-state-building-green-"
        "philadelphia-eagles-spt-intl/index.html")
    elements = uio.parse_file_or_url(example_url)
    print(("\n\n".join([str(el) for el in elements])))
    
    
    
    >>> The Empire State Building was lit in green and white to celebrate the Philadelphia Eagles’ victory in the NFC Championship game on Sunday – a decision that’s sparked a bit of a backlash in the Big Apple.
    
    >>>  The Eagles advanced to the Super Bowl for the first time since 2018 after defeating the San Francisco 49ers 31-7, and the Empire State Building later tweeted how it was marking the occasion.
    
    >>>  Fly @Eagles Fly! We’re going Green and White in honor of the Eagles NFC Championship Victory. pic.twitter.com/RNiwbCIkt7— Empire State Building (@EmpireStateBldg)
    
    >>>  January 29, 2023...
    

Utilize `clean_text_data` to do various text cleaning operations

    
    
    # Set example dirty text
    example_dirty_text = ("\x93Some dirty text â€™ with extra spaces and – dashes.")
    
    # Set clean options   
    options = [
        ('replace_unicode_quotes', {}),
        ('clean_dashes', {}),
        ('clean_non_ascii_chars', {}),
        ('clean_extra_whitespace', {}),
    ]
    
    cleaned_text = uio.clean_text_data(text=example_dirty_text,clean_options=options)
    print(cleaned_text)
    
    
    
    >>> Some dirty text with extra spaces and dashes.
    

Utilize `extract_data_from_text` to do text extraction operation

    
    
    # Set example email to extract
    example_email_text = ("Contact me at example@email.com.")
    
    extracted_text = uio.extract_data_from_text(text=example_email_text,
    extract_type="extract_email_address")
    
    print(extracted_text)
    
    
    
    >>> ['example@email.com']
    

Utilize `chunk_elements` to chunk the content

    
    
    chunks = uio.chunk_elements(elements=elements,chunk_type="chunk_by_title")
    
    for chunk in chunks:
        print(chunk)
        print("\n" + "-" * 80)
    
    
    
    >>> The Empire State Building was lit in green and white to celebrate the Philadelphia Eagles’ victory in the NFC Championship game on Sunday – a decision that’s sparked a bit of a backlash in the Big Apple.
    
    >>>  The Eagles advanced to the Super Bowl for the first time since 2018 after defeating the San Francisco 49ers 31-7, and the Empire State Building later tweeted how it was marking the occasion.
    
    >>>  --------------------------------------------------------------------------------
    >>>  Fly @Eagles Fly! We’re going Green and White in honor of the Eagles NFC Championship Victory. pic.twitter.com/RNiwbCIkt7— Empire State Building (@EmpireStateBldg)
    
    >>>  --------------------------------------------------------------------------------
    >>>  January 29, 2023
    

Utilize `stage_elements` to do element staging

    
    
    staged_element = uio.stage_elements(elements=elements,stage_type="stage_for_baseplate")
    
    print(staged_element)
    
    
    
    >>> {'rows': [{'data': {'type': 'UncategorizedText', 'element_id': 'e78902d05b0cb1e4c38fc7a79db450d5', 'text': 'CNN\n        \xa0—'}, 'metadata': {'filetype': 'text/html', 'languages': ['eng'], 'page_number': 1, 'url': 'https://www.cnn.com/2023/01/30/sport/empire-state-building-green-philadelphia-eagles-spt-intl/index.html', 'emphasized_text_contents': ['CNN'], 'emphasized_text_tags': ['span']}}, ...
    

This is a basic guide to get you started with the `Unstructured IO` module.
For more advanced usage, refer to the specific method documentation and the
[Unstructured IO Documentation](https://unstructured-
io.github.io/unstructured/).

[ __ previous Critic Agents and Tree Search
](../agents/critic_agents_and_tree_search.html "previous page") [ next
Storages __](storages.html "next page")

__Contents

  * 1\. Concept
  * 2\. Types
    * 2.1. Base IO
    * 2.2. Unstructured IO
  * 3\. Get Started
    * 3.1. Using `Base IO`
    * 3.2. Using `Unstructured IO`

By CAMEL-AI.org

© Copyright 2023, CAMEL-AI.org.  

