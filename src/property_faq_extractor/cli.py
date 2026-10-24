# Entry place for any request coming into the system. CLI, API Gateway, EventBridge, or anything else comes from here and returns a result in here only

import argparse
from pathlib import Path

from .reader import readDocument
from .generate import generateFAQ

def main():
    p = argparse.ArgumentParser(
            prog="property-faq-extractor",
            description="Generate a list of FAQ based on the documents containing house rules, contracts, guidelines and instructions.",
        )
    p.add_argument("files", nargs="+", type=Path, help="One or more files: PDF, Word, image or text")
    p.add_argument("--output", type=Path, help="JSON file as output. Without it the result will only be shown in the screen")

    args = p.parse_args()

    for f in args.files:
        if not f.exists():
            p.error(f'File not found: {f}')

    documents = [readDocument(d) for d in p.files]
    faq = generateFAQ(documents)
    



if __name__ == "__main__":
    main()