# XeLaTeX is required because main.tex uses fontspec and Unicode text.
# Force XeLaTeX even when latexmk receives '-pdf' from an external builder.
$pdflatex = 'xelatex -interaction=nonstopmode -file-line-error %O %S';
$pdf_mode = 1;
