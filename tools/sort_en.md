# Analyzing the Python Script through the Lens of Unix Philosophy

This article examines a Python script designed to move all PDF files from a source directory to a target directory while removing duplicates. We'll analyze this script in the context of the Unix Philosophy, which emphasizes simplicity, modularity, and reusability.

# Unix Philosophy Principles

The Unix Philosophy can be summarized by several key principles:

Make each program do one thing well.
Expect the output of every program to become the input to another.
Design and build software to be tried early, ideally within weeks.
Use tools in preference to unskilled help to lighten a programming task.
Write programs to work together.
Write programs to handle text streams, because that is a universal interface.
Let's delve into how this script adheres to these principles.

# Script Overview

[sort.py](sort.py)

# Analysis of Unix Philosophy Adherence

### 1. Make Each Program Do One Thing Well

The script is focused on a single task: moving PDF files and eliminating duplicates. Each function within the script has a clear, specific purpose, such as checking for duplicate files (`isNotDuplicated`), verifying PDF extensions (`isPDF`), and handling command-line arguments (`get_cli_args`).

### 2. Expect the Output of Every Program to Become the Input to Another

While this script is self-contained and doesn't directly feed its output into another program, it is designed in a way that its functions could be easily integrated into larger workflows. For instance, `getFiles` can be reused to filter files in other scripts, and `movePDF` can be adapted to handle different file types or destinations.

### 3. Design and Build Software to be Tried Early

The script includes a `--unittest` option to run doctests, which means the code can be tested immediately after changes are made. This encourages iterative development and immediate feedback, aligning with the Unix philosophy of building and testing software quickly.

### 4. Use Tools in Preference to Unskilled Help

The script leverages several powerful Python libraries (`argparse`, `shutil`, `pathlib`, and `re`) to accomplish its tasks efficiently. This use of robust libraries simplifies the code and reduces the likelihood of errors, embodying the Unix philosophy of utilizing effective tools.

### 5. Write Programs to Work Together

The modular design of the script, with clear function definitions and a main entry point, facilitates integration with other scripts or systems. Functions like `getFiles` and `movePDF` can be independently tested and reused, promoting interoperability.

### 6. Write Programs to Handle Text Streams

While the script primarily deals with file paths and operations, it follows the principle of handling text streams by processing command-line arguments and validating paths. The use of `argparse` ensures the script can interact seamlessly with user input provided as text.

## Conclusion

This Python script exemplifies several key aspects of the Unix Philosophy. Its focus on a single task, modular structure, use of powerful tools, and ability to be tested and integrated into larger workflows all reflect the principles that have guided Unix development for decades. By adhering to these principles, the script not only accomplishes its goal effectively but also maintains simplicity, clarity, and flexibility.
