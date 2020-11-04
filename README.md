# Course Handouts
This directory contains the source code for compiling course handouts. The documents in
this directory **are not** the assignment handouts.

Each subdirectory within this folder has, at a minimum, a file titled
`latexmkrc`.  This is the settings file for latexmk, which will handle
juggling the various latex engines preferred by the course staff.  A basic
`latexmkrc` file (e.g., for `pdflatex`) might have the following contents
([`latexmk` documentation](https://mirror.las.iastate.edu/tex-archive/support/latexmk/latexmk.pdf)):
```
@default_files = ("main.tex");   # Set the root tex file for the output document
$pdf_mode = 1;                   # tex -> PDF
$auto_rc_use = 1;                # Do not read further latexmkrc files
$warnings_as_errors = 1;         # Elevates warnings to errors.  Enforces cleaner code.
$pdflatex = "pdflatex -halt-on-error -interaction=batchmode %O %S";
                                 # Forces latexmk to stop and quit if it encounters an error
$jobname = "output_name";        # This is the name of the output PDF file
$silent = 1                      # For quieter output on the terminal.
```
Feel free to customize this as you desire, including adding more files,
directories, and media.  There is only one requirements:

**IT MUST BE POSSIBLE TO COMPILE EACH DOCUMENT USING ONLY THE FOLLOWING COMMAND:**
```
$ latexmk
```
A properly setup `latexmkrc` file can handle any special compilation options you
may require.  Put those options in the `latexmkrc` file so that other course
staff can compile your document with the command above.

Other commands that might be helpful include:
- `$ latexmk -pvc`:  (preview continuously) This will run `latexmk`
continuously, allowing you to immediately view changes to your output document
as you save source files.
- `$ latexmk -c`:  This will remove all auxiliary files other than the final
output PDF.
- `$ latexmk -C`:  This will remove all output files (including the final output
PDF).