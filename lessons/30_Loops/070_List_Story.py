"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story
"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

#story = [words[0],[2],[7],[9],[7],[1],[11],[12],[13],[10],[7],[3]]
story = []
story.append(words[0])
story.append(words[2])
story.append(words[7])
story.append(words[9])
story.append(words[7])
story.append(words[13])
story.append(words[14])
story.append(words[7])
story.append(words[1])
story.append(words[15])
story.append(words[10])
story.append(words[7])
story.append(words[4])
story.append(words[10])
story.append(words[17])
story.append(words[18])

# Display the story to the user
print(' '.join(story))