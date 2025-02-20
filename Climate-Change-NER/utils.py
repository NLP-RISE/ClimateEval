from pprint import pprint

import numpy as np
import sklearn.metrics


def entity_f1(predictions, references):
    """
    Computes precision, recall, and F1-score for NER task.

    :param predictions: List of dictionaries with entity types as keys and lists of entities as values.
    :param references: List of dictionaries with gold-standard entity labels.
    :return: (precision, recall, f1-score) tuple per instance.
    """

    precision_scores = []
    recall_scores = []
    f1_scores = []
    print("Prediction:")
    pprint(predictions)
    print("Gold:")

    pprint(references)

    for pred, ref in zip(predictions, references):
        pred_entities = set((etype, ent) for etype, ents in pred.items() for ent in ents)
        ref_entities = set((etype, ent) for etype, ents in ref.items() for ent in ents)

        true_positives = len(pred_entities & ref_entities)
        false_positives = len(pred_entities - ref_entities)
        false_negatives = len(ref_entities - pred_entities)

        precision = true_positives / (true_positives + false_positives + 1e-9)
        recall = true_positives / (true_positives + false_negatives + 1e-9)
        f1 = 2 * (precision * recall) / (precision + recall + 1e-9)

        precision_scores.append(precision)
        recall_scores.append(recall)
        f1_scores.append(f1)

    return list(zip(precision_scores, recall_scores, f1_scores))


def agg_entity_f1(items):
    """
    Aggregates F1-score across dataset instances.

    :param items: List of tuples containing precision, recall, and F1-score for each instance.
    :return: Mean F1-score across instances.
    """

    precision, recall, f1_scores = zip(*items)
    precision, recall, f1_scores = np.asarray(precision), np.asarray(recall), np.asarray(f1_scores)

    return {
        "precision": np.mean(precision),
        "recall": np.mean(recall),
        "f1": np.mean(f1_scores)
    }
