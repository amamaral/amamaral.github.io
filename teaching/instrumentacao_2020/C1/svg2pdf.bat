@ECHO OFF
FOR %%i IN (*.svg) DO (
ECHO Inkscape svg2pdf conversion of %%i...
inkscape -f=%%i --export-pdf=%%~ni.pdf --export-dpi=600
)
