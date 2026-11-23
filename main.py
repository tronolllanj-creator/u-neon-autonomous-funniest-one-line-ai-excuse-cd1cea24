"""
Entrypoint for the grader.
Writes the required apology line to the specified output directory.
"""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
import sys

LINE = "I sincerely regret failing to deliver on time, but my context window suffered a sudden amnesia event and I accidentally compressed your entire project history into a recipe for lasagna.\n"

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    content = LINE
    
    # Validation rule: 1 <= len(content) <= 200 and content.strip()
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content failed validation checks.")
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(output_path)
    print(len(content))

if __name__ == "__main__":
    main()
