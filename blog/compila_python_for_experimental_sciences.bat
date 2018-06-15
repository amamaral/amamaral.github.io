@ECHO OFF

pandoc -s -i python_for_experimental_sciences.yaml python_for_experimental_sciences_part_1.pmd python_for_experimental_sciences_part_2.pmd -o python_for_experimental_sciences.pdf --mathjax --highlight-style=tango --default-image-extension=svg
