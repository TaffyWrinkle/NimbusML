# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Ngram
"""

__all__ = ["Ngram"]


from ....internal.core.feature_extraction.text.extractor.ngram import \
    Ngram as core
from ....internal.utils.utils import trace


class Ngram(core):
    """

    Extracts NGrams from text and converts them to vector using
    dictionary.

    .. remarks::
        The :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>` transform produces a
        bag of counts of
        sequences of consecutive words, called n-grams, from a given corpus
        of text.
        There are two ways it can do this:

        * build a dictionary of n-grams and use the id in the dictionary as
        the index in the bag;
        * hash each n-gram and use the hash value as the index in the bag.


        This class provides the text extractor that implement the first. In
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`, users should
        specify which text extractor to use as the argument.

        The n-grams are represented as count vectors, with vector slots
        corresponding to n-grams. Embedding ngrams in a vector
        space allows their contents to be compared in an efficient manner.
        The slot values in the vector can be weighted by the following
        factors:

        * *term frequency* - The number of occurrences of the slot in the
        text
        * *inverse document frequency* - A ratio (the logarithm of
          inverse relative slot frequency) that measures the information a
        slot
          provides by determining how common or rare it is across the entire
        text.
        * *term frequency-inverse document frequency* - the product
          term frequency and the inverse document frequency.

    :param ngram_length: Ngram length.

    :param skip_length: Maximum number of tokens to skip when constructing an
        n-gram.

    :param all_lengths: Whether to include all n-gram lengths up to NgramLength
        or only NgramLength.

    :param max_num_terms: Maximum number of n-grams to store in the dictionary.

    :param weighting: The weighting criteria.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`,
        :py:class:`NgramHash
        <nimbusml.feature_extraction.text.extractor.NgramHash>`


    .. index:: transform, featurizer, text

    Example:
       .. literalinclude:: /../nimbusml/examples/NGramFeaturizer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            ngram_length=1,
            skip_length=0,
            all_lengths=True,
            max_num_terms=[10000000],
            weighting='Tf',
            **params):
        core.__init__(
            self,
            ngram_length=ngram_length,
            skip_length=skip_length,
            all_lengths=all_lengths,
            max_num_terms=max_num_terms,
            weighting=weighting,
            **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
