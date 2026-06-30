# 🧬 DNA Translator

*A Python program that simulates key molecular biology processes.*

![Python](https://img.shields.io/badge/Python-3.14+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Project](https://img.shields.io/badge/Project-Educational-purple)

DNA Translator is an educational bioinformatics toolkit that performs DNA validation, sequence analysis, transcription, and translation.

```text
DNA → mRNA → Protein
```

## Features

- DNA sequence validation
- Sequence statistics
  - Length
  - Base counts
  - GC/AT content
- DNA → mRNA transcription
- Start codon detection (`AUG`)
- Stop codon termination (`UGA`, `UAA`, `UAG`)
- Codon-based amino acid translation
- Reading frame analysis
- Coding region display

## 📦 Installation

```bash
git clone https://github.com/isaacrodriguez7100/dna-translator.git
cd dna-translator
python src/dna_translator.py
```

## Requirements

```text
Python 3.14+
No external dependencies
```

## ⚙️ How It Works

1. The user inputs a DNA sequence.
2. The program validates that only A, T, C, and G are included.
3. The sequence statistics are calculated.
4. DNA is transcribed into mRNA.
5. The mRNA sequence is searched for a start codon.
6. Codons are translated into amino acids.
7. Translation stops at the first stop codon.
8. The final protein sequence is displayed.

# Examples

The program currently supports two primary modes of operation.

---

## Example 1 — DNA Sequence Statistics

Analyze the composition of a DNA sequence.

### Input

```text
Input DNA sequence:
gatcgtagtacgtacgtgacactgactgtactgactg

Option:
1
```

### Output

- DNA sequence formatted into codons
- Sequence length
- Individual base counts
- Base percentages
- GC content
- AT content

![Screenshot 2026-06-26 at 4.39.53 PM.png](../../Desktop/Screenshots/Screenshot%202026-06-26%20at%204.39.53%E2%80%AFPM.png)

---

## Example 2 — DNA Translation

Translate a DNA sequence into its corresponding protein.

### Input

```text
Input DNA sequence:
gatcgtagtacgtacgtgacactgactgtactgactg

Option:
2
```

### Output

- DNA → mRNA transcription
- Start codon detection (`AUG`)
- Protein coding region visualization
- Translation into amino acids
- Protein count

![Screenshot 2026-06-26 at 4.39.16 PM.png](../../Desktop/Screenshots/Screenshot%202026-06-26%20at%204.39.16%E2%80%AFPM.png)

## 🗺️ Roadmap

### Completed

- [x] DNA validation
- [x] Sequence statistics
- [x] Transcription
- [x] Translation
- [x] Start codon detection
- [x] Stop codon termination

### Planned

- [ ] FASTA file input support
- [ ] `.txt` file input support
- [ ] Reverse complement
- [ ] Open Reading Frame detection
- [ ] Mutation simulator
- [ ] Biopython integration
- [ ] Export results to file

## 🎯 Why I Built This

I built this project to combine my interests in programming and molecular biology while preparing for future coursework and research in computational biology.

As an incoming Biotechnology student at the University of Houston, my long-term goal is to develop software that helps researchers analyze biological data and better understand genetic information.

## 📄 License

This project is licensed under the MIT License.