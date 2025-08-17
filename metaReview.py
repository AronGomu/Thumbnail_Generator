import os
import platform

format = "Legacy"
text = "Ce Match Up n'existe pas"
deck1 = "Mono Black Aggro" 
deck2 = "Jund Nic Fit"

youtuberName = "BeExcellent"
videoLink = "https://www.youtube.com/watch?v=54sD5qL9h84"
channelLink = "https://www.youtube.com/@BeExcellent80s"

Title = f"{text} - {deck1} vs {deck2} - {format} League Review"





Description = f"""
BIG UP à {youtuberName} pour permettre le libre partage de cette vidéo !

Lien de la vidéo : {videoLink}
Lien de la chaîne : {channelLink}

_________________

Réseaux Sociaux :
Chaîne perso de Nathan : https://www.youtube.com/@arongomu4294
Facebook : https://www.facebook.com/mtgones
Twitter/X : https://x.com/MtgOnes
Discord : https://discord.gg/2uXnFwnV
"""



file_path = "LeagueReviewMetaData.txt"

# Write to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(Title + "\n\n")
    f.write(Description)

# Open the file after writing
system_name = platform.system()
if system_name == "Windows":
    os.startfile(file_path)  # Works only on Windows
elif system_name == "Darwin":  # macOS
    os.system(f"open '{file_path}'")
else:  # Linux and others
    os.system(f"xdg-open '{file_path}'")