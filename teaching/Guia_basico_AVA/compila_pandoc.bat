SET filename=apresentacao


:: Add --self-contained to see slides without internet connection...
pandoc -s -i -t revealjs %filename%.pmd -o %filename%.html --mathjax --highlight-style=tango --default-image-extension=svg
:: Optional beamer output
::pandoc -s -i -t beamer %filename%.pmd -o %filename%.pdf --highlight-style=tango --default-image-extension=pdf

IF /I "%ERRORLEVEL%" NEQ "0" (
    pause
)
