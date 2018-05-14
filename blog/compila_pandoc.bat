@ECHO OFF

FOR %%i IN (*.pmd) DO (
pandoc -s -i %%i -o %%~ni.html --mathjax --highlight-style=tango --default-image-extension=svg
)
