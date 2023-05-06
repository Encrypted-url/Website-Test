from flask import Flask, render_template, request

app = Flask(__name__)

# A list of file names for the png images to display.
file_names = ['1.png', '2.png', '3.png']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # If the user clicked a button
        # Get the index of the current file
        current_file_index = file_names.index(request.form['current_file']) 

        if 'previous' in request.form: # If they clicked the 'previous' button
            # Decrement the index to change the file
            current_file_index = (current_file_index - 1) % len(file_names)
        elif 'next' in request.form: # If they clicked the 'next' button
            # Increment the index to change the file
            current_file_index = (current_file_index + 1) % len(file_names)

    else:
        # Set the current file to the first in the list
        current_file_index = 0

    # Get the current file name
    current_file = file_names[current_file_index]

    return render_template('index.html',
                            file=current_file,
                            current_file=current_file)

app.run(host='0.0.0.0', port=81)