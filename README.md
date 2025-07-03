#  zipcrack

**zipcrack** is a lightweight Python CLI tool that brute-forces password-protected ZIP files where the password is a numeric string of fixed length (default: 9 digits).

This tool is ideal for CTFs, forensic analysis, or recovering your own lost ZIP passwords when you know the format.

---

##  Features

- Brute-force ZIP file passwords with all-digit combinations.
- Supports configurable digit length (e.g., 4, 6, 9).
- Uses a progress bar with `tqdm`.
- One-command CLI execution.

---

##  Installation

You can install directly from GitHub using:

```bash
pip install git+https://github.com/MahizhnanC/zipcrack.git
```


---

##  Usage

```bash
zipcrack --file /path/to/protected.zip --digits 9
```

### Arguments:

| Flag         | Description                                       | Default |
|--------------|---------------------------------------------------|---------|
| `--file`, `-f` | Path to the ZIP file to crack                    | required |
| `--digits`, `-d` | Number of digits in the password (numeric only) | 9 |

---

###  Example

```bash
zipcrack -f ~/Downloads/challenge.zip -d 9
```

---

##  Tip

Try common passwords like `123456789`, `987654321`, `000000000`, etc., manually before brute-forcing all 1 billion combinations.

---

##  Disclaimer

This tool is for **educational and ethical use only**. Do not use it to attack ZIP files without permission.

---

##  License

MIT License
