#GOALS
# 1. DNA --> mRNA transcription
# 2. Read codons and convert to amino acids
# 3. Sequence statistics: length, amount of individual bases, GC content, AT content
while True:
    DNA_string = input("Input DNA sequence: ").upper().strip().replace(" ","")
    if not DNA_string or not all(letter in "ATCG" for letter in DNA_string):
        print("DNA sequence is invalid. \nOnly A, T, C, and G are allowed")
        continue
    else:
        option_view = input("Enter 1 to view your DNA Statistics \nEnter 2 to translate your DNA sequence \n: ")
        if option_view == "1":
            DNA = []
            for a in range(0, len(DNA_string), 3):
                DNA.append(DNA_string[a:a + 3])
            organized_DNA = " ".join(DNA)  # reformatted version of the DNA sequence used to print at end

            # Sequence Statistics
            length_DNA = len(DNA_string)  # length of sequence
            # amount of bases
            amt_A = DNA_string.count("A")
            amt_T = DNA_string.count("T")
            amt_C = DNA_string.count("C")
            amt_G = DNA_string.count("G")
            # percent of bases
            percent_A = amt_A / length_DNA * 100
            percent_T = amt_T / length_DNA * 100
            percent_C = amt_C / length_DNA * 100
            percent_G = amt_G / length_DNA * 100
            # percent of base pairs
            percent_AT = percent_A + percent_T
            percent_GC = percent_G + percent_C

            DNA_SEQ_STATS = {
                "Amount of bases:": length_DNA,
                "Amount of base A:": amt_A,
                "Amount of base T:": amt_T,
                "Amount of base C:": amt_C,
                "Amount of base G:": amt_G,
                "Base A content:": percent_A,
                "Base T content:": percent_T,
                "Base C content:": percent_C,
                "Base G content:": percent_G,
                "Content of pair AT:": percent_AT,
                "Content of pair GC:": percent_GC,
            }
            print(f"Your DNA Sequence:\n{organized_DNA}")
            for stat, value in DNA_SEQ_STATS.items():
                print(f"{stat}{value: .2f}")

            break
        elif option_view == "2":
            CODON_LIBRARY = {
                "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
                "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
                "CAU": "His", "CAC": "His",
                "CAA": "Gln", "CAG": "Gln",
                "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
                "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
                "AUG": "Met",
                "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
                "AAU": "Asn", "AAC": "Asn",
                "AAA": "Lys", "AAG": "Lys",
                "AGU": "Ser", "AGC": "Ser",
                "AGA": "Arg", "AGG": "Arg",
                "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
                "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
                "GAU": "Asp", "GAC": "Asp",
                "GAA": "Glu", "GAG": "Glu",
                "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
                "UUU": "Phe", "UUC": "Phe",
                "UUA": "Leu", "UUG": "Leu",
                "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
                "UAU": "Tyr", "UAC": "Tyr",
                "UAA": "STOP", "UAG": "STOP",
                "UGU": "Cys", "UGC": "Cys",
                "UGA": "STOP",
                "UGG": "Trp"
            }
            # DNA transcription
            mRNA_transcription = DNA_string.replace("A", "u").replace(
                "T", "a").replace("C", "g").replace("G", "c")
            mRNA = mRNA_transcription.upper()
            start_frame = mRNA.find("AUG")  # find start of coding region

            # failsafe
            if start_frame == -1:
                print("Could not find a start codon")
                continue
            else:
                # codon grouping
                codons = []
                for i in range(start_frame, len(mRNA), 3):
                    codons.append(mRNA[i:i + 3])
                protein_coding_region = " ".join(codons)

                amino_acid = []
                for codon in codons:
                    codon = CODON_LIBRARY.get(codon.upper(), "Incomplete codon")
                    if codon == "STOP":  # stops at the end of codding region
                        break

                    amino_acid.append(codon)
                amount_protein = len(amino_acid)
                #formatting
                protein_sequence = " ".join(amino_acid)
                num_char_in_protein_coding_region = len(protein_coding_region) + 2
                format_present_protein_sequence = (" " * start_frame) + ("^" * num_char_in_protein_coding_region)

                print(f"Your mRNA sequence is: {mRNA[0:start_frame]} {protein_coding_region}")
                print(f"Protein coding region: {format_present_protein_sequence}")
                print(f"Your proteins are: {protein_sequence}")
                print(f"Amount of Proteins: {amount_protein}")

            break
        else:
            print("Please enter a valid option")
            continue