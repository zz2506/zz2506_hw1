
# coding: utf-8

# In[ ]:


from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def random_quotes():
	with open('inspiration.txt', 'r', encoding='utf-8') as fp:
		data = fp.read().split('\n')
	return(random.choice(data))

if __name__ == '__main__':
    app.run()

