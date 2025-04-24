import os
from transformers import pipeline

# Initialize summarization pipeline
summariser = pipeline("summarisation")

# Initialize optional translators
translator_de = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
translator_tr = pipeline("translation_en_to_tr", model="Helsinki-NLP/opus-mt-en-tr")

def generate_mash(data: dict, language: str = 'EN') -> str:
    """Generates a Markdown one-pager using local transformer models."""
    # Generate overview
    overview_input = (
        f"Generate a concise project overview for the following repository:\n"
        f"Name: {data['name']}\nDescription: {data['description']}"
    )
    build_input = (
        f"Based on this README, extract the build and run instructions in bullet points:\n"
        f"{data['readme']}"
    )
    issues_input = (
        f"List the following known issues in bullet points:\n"
        f"{data['known_issues']}"
    )

    overview = summariser(overview_input, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    build_run = summariser(build_input, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    issues = summariser(issues_input, max_length=100, min_length=20, do_sample=False)[0]['summary_text']

    # Construct Markdown
    md = (
        f"# {data['name']} - One-Pager\n\n"
        f"## Project Overview\n{overview}\n\n"
        f"## Build & Run Instructions\n{build_run}\n\n"
        f"**License:** {data['license']}\n\n"
        f"## Known Issues\n{issues}\n"
    )

    # Translate if needed
    if language.upper() == 'DE':
        md = translator_de(md, max_length=1000)[0]['translation_text']
    elif language.upper() == 'TR':
        md = translator_tr(md, max_length=1000)[0]['translation_text']

    return md