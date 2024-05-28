import pytest
from AnonymousSurvey import AnonymousSurvey


@pytest.fixture
def language_survey():
    "A survey that will be available to all test functions."
    question = "What language did you first learned to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    "Test a single response is stored properly."
    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):
    "Test that 3 individual responses are stored properly."
    languages = ["English", "Ukrainian", "Polish"]
    for language in languages:
        language_survey.store_response(language)
    for language in languages:
        assert language in language_survey.responses
