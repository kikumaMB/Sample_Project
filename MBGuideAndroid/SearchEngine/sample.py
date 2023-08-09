def extract_word_between_n_and_space(text, n):
    # Find the first space after index n
    space_after_n = text.find(" ", n)

    if space_after_n != -1:
        # Extract the word between n and space
        word = text[n:space_after_n]
        return word
    else:
        # If there is no space after index n, return None or raise an error
        return None

# Example usage:
text = "Edition of BAIx 447.8 E-CELL 2021-05 IP_BAIx ECE_ROW MA-ECE_ROW HU-ECE_ROW NTG6.0 Mid, 1, de_DE.zip--PA200605--Z:\WebfsDownload\2021\May_done\Input_Content_Download_90_one_lang\PA200605\PA200605_BAiX_EQV_Mid"
n = 5  # Index from which to start extracting the word

result = extract_word_between_n_and_space(text, n)
print(result)  # Output: "is"
