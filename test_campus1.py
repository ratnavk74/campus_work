from campus1 import calculate_usage_score, classify_utilization


def test_calculate_usage_score():
    assert calculate_usage_score(10, 6) == 60


def test_classify_over_utilized():
    assert classify_utilization(95) == "Over-Utilized Resource"


def test_classify_optimally_utilized():
    assert classify_utilization(60) == "Optimally Utilized Resource"


def test_classify_under_utilized():
    assert classify_utilization(40) == "Under-Utilized Resource"
