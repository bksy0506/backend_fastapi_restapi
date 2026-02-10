# --- Korean Font Configuration ---
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def korean_font_config():
    if platform.system() == 'Darwin': # Mac
        rc('font', family='AppleGothic')
    elif platform.system() == 'Windows': # Windows
        # If Malgun Gothic is not available, try 'Gulim' or 'Batang'
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else: # Linux (e.g., Ubuntu, Debian)
        # You might need to install 'fonts-nanum' package
        # sudo apt-get install fonts-nanum
        # Then, rebuild font cache: sudo fc-cache -fv
        rc('font', family='NanumGothic')

    plt.rcParams['axes.unicode_minus'] = False # To correctly display minus signs
# ----------------------------------


if __name__ == "__main__":
    pass