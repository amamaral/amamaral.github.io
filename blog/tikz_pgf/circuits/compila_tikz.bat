::pandoc -s --template=template_png.pgs blink.tikz -o blink.tex
::pdflatex -shell-escape blink.tex
::pandoc -s --template=template_svg.pgs blink.tikz -o blink.tex
::pdflatex -shell-escape blink.tex

@ECHO OFF

FOR %%I IN (*.tikz) DO (
@ECHO Compilando %%~nI

@pandoc -s --template=..\template_png.pgs %%~nI.tikz -o %%~nI.tex
@pdflatex -shell-escape %%~nI.tex
::pandoc -s --template=..\template_svg.pgs %%~nI.tikz -o %%~nI.tex
::pdflatex -shell-escape %%~nI.tex

del %%~nI.tex %%~nI.log %%~nI.aux %%~nI.pdf
)
