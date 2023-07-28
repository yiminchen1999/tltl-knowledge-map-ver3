import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Directory paths
input_dir = 'assets/Year2023text/original'
output_dir = 'assets/wordcloud_plots_bookshape'



if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Custom WordCloud parameters
wordcloud_params = {
    'width': 800,
    'height': 400,
    'background_color': 'white',
    'colormap': 'viridis',
    'prefer_horizontal': 0.8,
    'mask': plt.imread('book_shape.png')
}

for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Read the text file
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r') as file:
            text = file.read()

        wordcloud = WordCloud(**wordcloud_params).generate(text)

        # Plot the word cloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        # Save the word cloud plot
        output_path = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.png')
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()

#
print(f"saved in the '{output_dir}' directory.")