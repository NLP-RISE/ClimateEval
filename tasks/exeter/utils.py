from collections import Counter

import numpy as np
from sklearn.metrics import f1_score
import logging


def f1(predictions, references):  # This is a passthrough function

    _prediction = predictions[0]
    _reference = references[0]
    print(f"_prediction: {_prediction}")
    print(f"_reference: {_reference}")
    string_label = ['0', '1', '2', '3', '4', '5']
    reference = string_label.index(_reference)
    prediction = (
        string_label.index(_prediction)
        if _prediction in string_label
        else not bool(reference)
    )

    return (prediction, reference)

def multi_f1(predictions, references):  # This is a passthrough function
    return (predictions[0], references[0])

def agg_f1(items):

    references, predictions = zip(*items)
    logging.info(f"predictions: {predictions}")
    logging.info(f"Counter(predictions): {Counter(list(predictions))}")

    logging.info(f"references: {references}")
    logging.info(f"Counter(references): {Counter(list(references))}")

    references, predictions = np.asarray(references), np.asarray(predictions)

    return f1_score(references, predictions, average='macro')


