# Text Justifier

Whilst reading my Kindle on a plane, I wondered how the text justification was done. I decided to implement my guess at a definition.

## Usage

- Place desired input text in `input.txt`
- Edit settings in `settings.py` as needed
- Run `python3 text_justifier.py`
- View output in `output.txt`

## Justification Definition

In an attempt to do this without existing work, I have no idea what the actual definition of justified text is. But the following rules were adhered to:

- Each line (except the last) will have the following
  - A character in the leftmost column
  - A character in the rightmost (`LINE_WIDTH`) column
  - Spaces distributed as evenly as possible to fill the width to the `LINE_WIDTH` setting
    - Current implementation starts from the rightmost column and drops one space after each existing space until it reaches the leftmost column, at which point it wraps around and repeats
- The last line will have its text left as is
- Each word in the output will be separated by the `SPACE` parameter in `settings.py`
- Newlines and tabs will be stripped upon reading the input
