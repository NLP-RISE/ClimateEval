import json
from pprint import pprint
import json_repair
import numpy as np
import sklearn.metrics
from aiohttp.client_reqrep import json_re


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

    for pred, ref in zip(predictions, references):
        try:
            ref = json_repair.loads(ref)
            pred = json_repair.loads(pred)
            if isinstance(pred, list):
                pred = pred[0]

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
        except Exception as e:
            print("---- Exception", e)
            print(pred)
            precision_scores.append(0)
            recall_scores.append(0)
            f1_scores.append(0)
    return list(zip(precision_scores, recall_scores, f1_scores))


def agg_entity_f1(items):
    """
    Aggregates F1-score across dataset instances.

    :param items: List of lists containing tuples of (precision, recall, f1-score) for each instance.
    :return: Dictionary with mean Precision, Recall, and F1-score across instances.
    """
    # Flatten list of lists into a single list of tuples
    flat_items = [entry for sublist in items for entry in sublist]

    if not flat_items:  # Handle case where all predictions are empty
        print("nooo")
        return {"precision": 0.0, "recall": 0.0, "f1": 0.0}

    # Unpack correctly after flattening
    precision, recall, f1_scores = zip(*flat_items)

    return {
        "precision": np.mean(precision),
        "recall": np.mean(recall),
        "f1": np.mean(f1_scores)
    }