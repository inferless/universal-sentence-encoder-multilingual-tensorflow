import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text

class InferlessPythonModel:
    def initialize(self):
        self.module = hub.load('https://kaggle.com/models/google/universal-sentence-encoder/frameworks/TensorFlow1/variations/universal-sentence-encoder/versions/1')

    def infer(self, inputs):
        questions = inputs['questions']
        responses = inputs['responses']
        response_contexts = inputs['response_contexts']

        question_embeddings = self.module.signatures['question_encoder'](tf.constant(questions))
        response_embeddings = self.module.signatures['response_encoder'](input=tf.constant(responses), context=tf.constant(response_contexts))

        return {"values" : str(np.inner(question_embeddings['outputs'], response_embeddings['outputs']))}

    def finalize(self):
        self.module = None

