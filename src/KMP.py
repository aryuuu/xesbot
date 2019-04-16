# Variabel Global
idx_solution = []

# Algoritma KMP
def KMP(text, pattern):
  global idx_solution

  lenght_text = len(text)
  lenght_pattern = len(pattern)

  # Array untuk menyimpan longest preffix dan sufffix
  lps = [0]*lenght_pattern
  
  # Inisialisasi index i untuk text dan j untuk path
  i = 0
  j = 0

  # Cari longest Preffix dan suffix dahulu
  findLPS(pattern, lenght_pattern, lps)

  while (i < lenght_text):
    if (text[i] == pattern[j]):
      i += 1
      j += 1

    if (j == lenght_pattern):
      return (i-j)
      j = lps[j-1]
    # Ketika terjadi ketidakcocokan setelah ada beberapa yang cocok
    elif (i < lenght_text and text[i] != pattern[j]):
      if (j != 0):
        j = lps[j-1]
      else:
        i += 1

  return -1

# Fungsi untuk mencari longest preffix dan suffix
def findLPS(pattern, lenght, lps):
  # inisialisasi
  lps[0]
  i = 1
  j = 0 

  while (i < lenght):
    if (pattern[i] == pattern[j]):
      j += 1
      lps[i] = j
      i += 1
    else:
      if (j != 0):
        j = lps[j-1]
      else:
        lps[i] = 0
        i += 1
