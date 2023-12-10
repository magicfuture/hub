import evaluate
from langchain.evaluation import load_evaluator
from langchain.evaluation import JsonValidityEvaluator


def frugalscore():
    frugalscore = evaluate.load("frugalscore", "moussaKam/frugalscore_medium_bert-base_mover-score")
    results = frugalscore.compute(predictions=['hello world'], references=['hugging face'])
    return results


def accuracy(references, predictions):
    accuracy_metric = evaluate.load("accuracy")
    results = accuracy_metric.compute(references=references, predictions=predictions)
    return results

def test_json(prediction):
    evaluator = load_evaluator("json_validity")
    result = evaluator.evaluate_strings(prediction=prediction)
    return result
