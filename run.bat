@echo off

IF /i "%1%"=="convert" goto convert
IF /i "%1%"=="copy" goto copy

echo "Please use following CMD arguments (convert|copy)."
goto commonexit

:convert
python ebook_converter.py
goto commonexit

:copy
python ebook_copier.py
goto commonexit

:commonexit