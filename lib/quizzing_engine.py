from pydantic import BaseModel, Field
from typing import List

# 1. Schema for a Single Flashcard
class Flashcard(BaseModel):
    """A Pydantic model for a single flashcard."""
    front: str = Field(description="The term or question for the front of the card.")
    back: str = Field(description="The definition or answer for the back of the card.")

# 2. Schema for the Flashcard Set
class FlashcardSet(BaseModel):
    """A list of flashcards generated from the content."""
    flashcards: List[Flashcard]
    
# 3. Schema for a Single Quiz Question
class QuizQuestion(BaseModel):
    """A Pydantic model for a single multiple-choice quiz question."""
    question: str = Field(description="The text of the quiz question.")
    options: List[str] = Field(description="A list of 4 possible answer choices.")
    correct_answer: str = Field(description="The correct answer choice from the options list.")
    explanation: str = Field(description="A brief explanation of why the answer is correct.")

# 4. Schema for the Quiz (List of questions)
class Quiz(BaseModel):
    """A list of quiz questions generated from the content."""
    quiz_title: str = Field(description="A title for the quiz, e.g., 'Quiz on Newtonian Physics'.")
    questions: List[QuizQuestion]