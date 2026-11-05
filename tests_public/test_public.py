"""Публичные проверки формата. Проходят — значит грейдер сможет прочитать ваши файлы.
Баллы за правильность ответов и качество модели считаются скрытыми проверками."""
import json

import pandas as pd
import pytest

ANSWER_KEYS = ["n_rows", "median_price", "top_district", "corr_area_price", "share_first_floor", "mean_price_per_m2"]


@pytest.mark.points(0.5)
def test_answers_json(repo_dir):
    p = repo_dir / "outputs" / "answers.json"
    assert p.exists(), "ноутбук должен создать outputs/answers.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    missing = [k for k in ANSWER_KEYS if k not in data]
    assert not missing, f"в answers.json нет ключей: {missing}"
    empty = [k for k in ANSWER_KEYS if data[k] is None]
    assert not empty, f"не заполнены: {empty}"
    assert isinstance(data["top_district"], str), "top_district — строка с названием района"
    for k in ANSWER_KEYS:
        if k != "top_district":
            assert isinstance(data[k], (int, float)), f"{k} должно быть числом"


@pytest.mark.points(0.5)
def test_predictions_csv(repo_dir):
    p = repo_dir / "outputs" / "predictions.csv"
    assert p.exists(), "ноутбук должен создать outputs/predictions.csv"
    df = pd.read_csv(p)
    assert list(df.columns) == ["id", "price"], f"ожидались колонки id, price; получено {list(df.columns)}"
    assert len(df) > 0, "файл пустой"
    assert not df["price"].isna().any(), "в price есть пропуски"
    assert not df["id"].duplicated().any(), "повторяющиеся id"
