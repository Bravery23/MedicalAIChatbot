from __future__ import annotations
from typing import Any, Dict, List, Optional, Text

import regex
from underthesea import word_tokenize

import rasa.shared.utils.io
import rasa.utils.io
from rasa.engine.graph import ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.shared.constants import DOCS_URL_COMPONENTS
from rasa.shared.nlu.training_data.message import Message


@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER, is_trainable=False
)
class VietnameseTokenizer(Tokenizer):
    """Tokenizer for Vietnamese language using underthesea library."""

    @staticmethod
    def not_supported_languages() -> Optional[List[Text]]:
        """The languages that are not supported by this tokenizer."""
        return None  # VietnameseTokenizer is specifically for Vietnamese

    @staticmethod
    def get_default_config() -> Dict[Text, Any]:
        """Returns the component's default config."""
        return {
            # Flag to check whether to split intents
            "intent_tokenization_flag": False,
            # Symbol on which intent should be split
            "intent_split_symbol": "_",
            # Regular expression to detect tokens (not used in VietnameseTokenizer)
            "token_pattern": None,
            # Symbol on which prefix should be split
            "prefix_separator_symbol": None,
        }

    def __init__(self, config: Dict[Text, Any]) -> None:
        """Initialize the tokenizer."""
        super().__init__(config)
        self.emoji_pattern = rasa.utils.io.get_emoji_regex()

        if "case_sensitive" in self._config:
            rasa.shared.utils.io.raise_warning(
                "The option 'case_sensitive' was moved from the tokenizers to the "
                "featurizers.",
                docs=DOCS_URL_COMPONENTS,
            )

    @classmethod
    def create(
            cls,
            config: Dict[Text, Any],
            model_storage: ModelStorage,
            resource: Resource,
            execution_context: ExecutionContext,
    ) -> VietnameseTokenizer:
        """Creates a new component."""
        return cls(config)

    def remove_emoji(self, text: Text) -> Text:
        """Remove emoji if the full text matches the emoji regex."""
        match = self.emoji_pattern.fullmatch(text)
        if match is not None:
            return ""
        return text

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        text = message.get(attribute) or ""

        # Remove emoji from full text (if bạn muốn)
        # text = self.emoji_pattern.sub("", text)

        # Tokenize giữ nguyên chữ gốc
        words = word_tokenize(text)

        # Remove emoji token riêng (nếu cần)
        words = [self.remove_emoji(w) for w in words if w.strip()]
        if not words:
            words = [text]

        tokens = self._convert_words_to_tokens(words, text)

        return self._apply_token_pattern(tokens)

    def _convert_words_to_tokens(self, words: List[Text], text: Text) -> List[Token]:
        """Convert a list of words to a list of Token objects with correct offsets."""
        tokens = []
        current_offset = 0

        for word in words:
            # Find the start position of the word in the original text
            match = regex.search(regex.escape(word), text[current_offset:])
            if match:
                start = current_offset + match.start()
                end = current_offset + match.end()
                tokens.append(Token(word, start, end))
                current_offset = end
            else:
                # If the word is not found, approximate the position
                tokens.append(Token(word, current_offset, current_offset + len(word)))
                current_offset += len(word) + 1  # Assume a space

        return tokens
