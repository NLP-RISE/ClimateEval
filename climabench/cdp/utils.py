import datasets
import numpy as np
import sklearn.metrics

labels = ["Adaptation", "Buildings", "Climate Hazards", "Emissions", "Energy", "Food", "Governance and Data Management", "Opportunities", "Strategy", "Transport", "Waste", "Water"]
columns_to_drop = ["id", "Year Reported to CDP", "Organization", "Parent Section", "Section",
                   "Question Name", "Row Name", "Comments", "Response Answer"]

def label_to_id(example):
    """Maps the Category/Label to an index based on the labels list."""
    example["label_index"] = labels.index(example["Label"])
    return example


def prepare_topic_dataset(dataset: datasets.Dataset) -> datasets.Dataset:

    dataset = dataset.remove_columns(columns_to_drop)
    dataset = dataset.map(label_to_id)  # Add label index column
    return dataset

def f1(predictions, references):  # This is a passthrough function

    _prediction = predictions[0]
    _reference = references[0]
    print(f"_prediction: {_prediction}")
    print(f"_reference: {_reference}")
    string_label = ['no', 'yes']
    reference = string_label.index(_reference)
    prediction = (
        string_label.index(_prediction)
        if _prediction in string_label
        else not bool(reference)
    )

    return (prediction, reference)

def agg_f1(items):

    references, predictions = zip(*items)
    references, predictions = np.asarray(references), np.asarray(predictions)

    return sklearn.metrics.f1_score(references, predictions, average='macro')