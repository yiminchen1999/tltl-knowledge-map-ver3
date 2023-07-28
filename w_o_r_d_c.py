import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Directory paths
input_dir = 'assets/Year2023text/original'

# Read the text data from files in the directory
data = []
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, 'r') as file:
            text = file.read()
            data.append(text)

# Combine the text data into a single string
combined_text = ' '.join(data)

# Generate the word cloud
wordcloud = WordCloud().generate(combined_text)

# Plot the word cloud
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')

# Function to handle mouse hover event
def on_hover(event):
    if event.inaxes == ax:
        for i, word in enumerate(wordcloud.words_):
            if wordcloud.words_[word] >= event.zdata:
                # Display the word as a tooltip
                tooltip = plt.annotate(word, xy=(event.xdata, event.ydata), xytext=(10, 10),
                                       textcoords='offset points', ha='left', va='top',
                                       bbox=dict(boxstyle='round', facecolor='white', edgecolor='grey'))
                tooltip.set_visible(True)
                fig.canvas.draw_idle()
                break

# Function to handle mouse leave event
def on_leave(event):
    if event.inaxes == ax:
        tooltip.set_visible(False)
        fig.canvas.draw_idle()

# Connect the mouse hover and leave events to the figure
fig.canvas.mpl_connect('motion_notify_event', on_hover)
fig.canvas.mpl_connect('axes_leave_event', on_leave)

# Show the interactive word cloud
plt.show()



# Generate the word cloud
wordcloud = WordCloud().generate(combined_text)

# Plot the word cloud
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')

# Add interactivity using mplcursors
cursor = mplcursors.cursor(ax, hover=True)

# Define the tooltip content
@cursor.connect("add")
def on_add(sel):
    word = sel.target.get_text()
    sel.annotation.set_text(word)
    sel.annotation.set_position((0, 20))
    sel.annotation.set_fontsize(10)
    sel.annotation.arrow_patch.set(arrowstyle="simple")

# Show the interactive word cloud
plt.show()


