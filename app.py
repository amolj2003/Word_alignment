from flask import Flask, render_template, request
import simalign
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        source_sentence = request.form['sentence1']
        target_sentence = request.form['sentence2']
        
        model = simalign.SentenceAligner()
        result = model.get_word_aligns(source_sentence, target_sentence)
        print(result['itermax'])

        aligned_words = []

        for source_index, target_index in result['itermax']:
            source_word = source_sentence.split()[source_index]
            target_word = target_sentence.split()[target_index]
            aligned_words.append((source_word, target_word))
        word=result['itermax']
        print(aligned_words)
        arr1=[]
        arr2=[]
        s=[]
    for i in range(len(word)):
        arr1.append(word[i][0])
        arr2.append(word[i][1])


    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            print(s.append(arr1[i]))
    probability=((len(arr1)-len(s))/len(arr1))*100
    return render_template('index.html', words=aligned_words,probability=probability)

if __name__ == '__main__':
    app.run(debug=True)


