# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
FastForestBinaryClassifier
"""

__all__ = ["FastForestBinaryClassifier"]


from ...entrypoints.trainers_fastforestbinaryclassifier import \
    trainers_fastforestbinaryclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class FastForestBinaryClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Machine Learning Fast Forest

    .. remarks::
        Decision trees are non-parametric models that perform a sequence of
        simple tests on inputs. This decision procedure maps them to outputs
        found in the training dataset whose inputs were similar to the
        instance
        being processed. A decision is made at each node of the binary tree
        data
        structure based on a measure of similarity that maps each instance
        recursively through the branches of the tree until the appropriate
        leaf
        node is reached and the output decision returned.

        Decision trees have several advantages:

        * They are efficient in both computation and memory usage during
          training and prediction.
        * They can represent non-linear decision boundaries.
        * They perform integrated feature selection and classification.
        * They are resilient in the presence of noisy features.

        Fast forest classifier is a random forest and quantile regression
        forest
        implementation using the tree learner in
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`. The model consists of an
        ensemble of decision trees.


        **Reference**

            `Wikipedia: Random forest
            <https://en.wikipedia.org/wiki/Random_forest>`_

            `Quantile regression forest
            <http://jmlr.org/papers/volume7/meinshausen06a/meinshausen06a.pdf>`_

            `From Stumps to Trees to Forests
            <https://blogs.technet.microsoft.com/machinelearning/2014/09/10/from-
            stumps-to-trees-to-forests/>`_


    :param number_of_trees: Specifies the total number of decision trees to
        create in the ensemble. By creating more decision trees, you can
        potentially get better coverage, but the training time increases.

    :param number_of_leaves: The maximum number of leaves (terminal nodes) that
        can be created in any tree. Higher values potentially increase the size
        of the tree and get better precision, but risk overfitting and
        requiring longer training times.

    :param minimum_example_count_per_leaf: Minimum number of training instances
        required to form a leaf. That is, the minimal number of documents
        allowed in a leaf of regression tree, out of the sub-sampled data. A
        'split' means that features in each level of the tree (node) are
        randomly divided.

    :param normalize: If ``Auto``, the choice to normalize depends on the
        preference declared by the algorithm. This is the default choice. If
        ``No``, no normalization is performed. If ``Yes``, normalization always
        performed. If ``Warn``, if normalization is needed by the algorithm, a
        warning message is displayed but normalization is not performed. If
        normalization is performed, a ``MaxMin`` normalizer is used. This
        normalizer preserves sparsity by mapping zero to zero.

    :param caching: Whether trainer should cache input training data.

    :param maximum_output_magnitude_per_tree: Upper bound on absolute value of
        single tree output.

    :param number_of_quantile_samples: Number of labels to be sampled from each
        leaf to make the distribution.

    :param parallel_trainer: Allows to choose Parallel FastTree Learning
        Algorithm.

    :param number_of_threads: The number of threads to use.

    :param random_state: The seed of the random number generator.

    :param feature_selection_seed: The seed of the active feature selection.

    :param entropy_coefficient: The entropy (regularization) coefficient
        between 0 and 1.

    :param histogram_pool_size: The number of histograms in the pool (between 2
        and numLeaves).

    :param disk_transpose: Whether to utilize the disk or the data's native
        transposition facilities (where applicable) when performing the
        transpose.

    :param feature_flocks: Whether to collectivize features during dataset
        preparation to speed up training.

    :param categorical_split: Whether to do split based on multiple categorical
        feature values.

    :param maximum_categorical_group_count_per_node: Maximum categorical split
        groups to consider when splitting on a categorical feature. Split
        groups are a collection of split points. This is used to reduce
        overfitting when there many categorical features.

    :param maximum_categorical_split_point_count: Maximum categorical split
        points to consider when splitting on a categorical feature.

    :param minimum_example_fraction_for_categorical_split: Minimum categorical
        example percentage in a bin to consider for a split.

    :param minimum_examples_for_categorical_split: Minimum categorical example
        count in a bin to consider for a split.

    :param bias: Bias for calculating gradient for each feature bin for a
        categorical feature.

    :param bundling: Bundle low population bins. Bundle.None(0): no bundling,
        Bundle.AggregateLowPopulation(1): Bundle low population,
        Bundle.Adjacent(2): Neighbor low population bundle.

    :param maximum_bin_count_per_feature: Maximum number of distinct values
        (bins) per feature.

    :param sparsify_threshold: Sparsity level needed to use sparse feature
        representation.

    :param first_use_penalty: The feature first use penalty coefficient. This
        is a form of regularization that incurs a penalty for using a new
        feature when creating the tree. Increase this value to create trees
        that don't use many features.

    :param feature_reuse_penalty: The feature re-use penalty (regularization)
        coefficient.

    :param gain_conf_level: Tree fitting gain confidence requirement (should be
        in the range [0,1) ).

    :param softmax_temperature: The temperature of the randomized softmax
        distribution for choosing the feature.

    :param execution_time: Print execution time breakdown to stdout.

    :param feature_fraction: The fraction of features (chosen randomly) to use
        on each iteration.

    :param bagging_size: Number of trees in each bag (0 for disabling bagging).

    :param bagging_example_fraction: Percentage of training examples used in
        each bag.

    :param feature_fraction_per_split: The fraction of features (chosen
        randomly) to use on each split.

    :param smoothing: Smoothing paramter for tree regularization.

    :param allow_empty_trees: When a root split is impossible, allow training
        to proceed.

    :param feature_compression_level: The level of feature compression to use.

    :param compress_ensemble: Compress the tree Ensemble.

    :param test_frequency: Calculate metric values for train/valid/test every k
        rounds.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FastTreesBinaryClassifier
        <nimbusml.ensemble.FastTreesBinaryClassifier>`,
        :py:class:`FastForestRegressor
        <nimbusml.ensemble.FastForestRegressor>`

    .. index:: models, classification, regression

    Example:
       .. literalinclude:: /../nimbusml/examples/FastForestBinaryClassifier.py
              :language: python
    """

    @trace
    def __init__(
            self,
            number_of_trees=100,
            number_of_leaves=20,
            minimum_example_count_per_leaf=10,
            normalize='Auto',
            caching='Auto',
            maximum_output_magnitude_per_tree=100.0,
            number_of_quantile_samples=100,
            parallel_trainer=None,
            number_of_threads=None,
            random_state=123,
            feature_selection_seed=123,
            entropy_coefficient=0.0,
            histogram_pool_size=-1,
            disk_transpose=None,
            feature_flocks=True,
            categorical_split=False,
            maximum_categorical_group_count_per_node=64,
            maximum_categorical_split_point_count=64,
            minimum_example_fraction_for_categorical_split=0.001,
            minimum_examples_for_categorical_split=100,
            bias=0.0,
            bundling='None',
            maximum_bin_count_per_feature=255,
            sparsify_threshold=0.7,
            first_use_penalty=0.0,
            feature_reuse_penalty=0.0,
            gain_conf_level=0.0,
            softmax_temperature=0.0,
            execution_time=False,
            feature_fraction=0.7,
            bagging_size=1,
            bagging_example_fraction=0.7,
            feature_fraction_per_split=0.7,
            smoothing=0.0,
            allow_empty_trees=True,
            feature_compression_level=1,
            compress_ensemble=False,
            test_frequency=2147483647,
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.number_of_trees = number_of_trees
        self.number_of_leaves = number_of_leaves
        self.minimum_example_count_per_leaf = minimum_example_count_per_leaf
        self.normalize = normalize
        self.caching = caching
        self.maximum_output_magnitude_per_tree = maximum_output_magnitude_per_tree
        self.number_of_quantile_samples = number_of_quantile_samples
        self.parallel_trainer = parallel_trainer
        self.number_of_threads = number_of_threads
        self.random_state = random_state
        self.feature_selection_seed = feature_selection_seed
        self.entropy_coefficient = entropy_coefficient
        self.histogram_pool_size = histogram_pool_size
        self.disk_transpose = disk_transpose
        self.feature_flocks = feature_flocks
        self.categorical_split = categorical_split
        self.maximum_categorical_group_count_per_node = maximum_categorical_group_count_per_node
        self.maximum_categorical_split_point_count = maximum_categorical_split_point_count
        self.minimum_example_fraction_for_categorical_split = minimum_example_fraction_for_categorical_split
        self.minimum_examples_for_categorical_split = minimum_examples_for_categorical_split
        self.bias = bias
        self.bundling = bundling
        self.maximum_bin_count_per_feature = maximum_bin_count_per_feature
        self.sparsify_threshold = sparsify_threshold
        self.first_use_penalty = first_use_penalty
        self.feature_reuse_penalty = feature_reuse_penalty
        self.gain_conf_level = gain_conf_level
        self.softmax_temperature = softmax_temperature
        self.execution_time = execution_time
        self.feature_fraction = feature_fraction
        self.bagging_size = bagging_size
        self.bagging_example_fraction = bagging_example_fraction
        self.feature_fraction_per_split = feature_fraction_per_split
        self.smoothing = smoothing
        self.allow_empty_trees = allow_empty_trees
        self.feature_compression_level = feature_compression_level
        self.compress_ensemble = compress_ensemble
        self.test_frequency = test_frequency

    @property
    def _entrypoint(self):
        return trainers_fastforestbinaryclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column_name=self._getattr_role('feature_column_name', all_args),
            label_column_name=self._getattr_role('label_column_name', all_args),
            example_weight_column_name=self._getattr_role('example_weight_column_name', all_args),
            row_group_column_name=self._getattr_role('row_group_column_name', all_args),
            number_of_trees=self.number_of_trees,
            number_of_leaves=self.number_of_leaves,
            minimum_example_count_per_leaf=self.minimum_example_count_per_leaf,
            normalize_features=self.normalize,
            caching=self.caching,
            maximum_output_magnitude_per_tree=self.maximum_output_magnitude_per_tree,
            number_of_quantile_samples=self.number_of_quantile_samples,
            parallel_trainer=self.parallel_trainer,
            number_of_threads=self.number_of_threads,
            seed=self.random_state,
            feature_selection_seed=self.feature_selection_seed,
            entropy_coefficient=self.entropy_coefficient,
            histogram_pool_size=self.histogram_pool_size,
            disk_transpose=self.disk_transpose,
            feature_flocks=self.feature_flocks,
            categorical_split=self.categorical_split,
            maximum_categorical_group_count_per_node=self.maximum_categorical_group_count_per_node,
            maximum_categorical_split_point_count=self.maximum_categorical_split_point_count,
            minimum_example_fraction_for_categorical_split=self.minimum_example_fraction_for_categorical_split,
            minimum_examples_for_categorical_split=self.minimum_examples_for_categorical_split,
            bias=self.bias,
            bundling=self.bundling,
            maximum_bin_count_per_feature=self.maximum_bin_count_per_feature,
            sparsify_threshold=self.sparsify_threshold,
            feature_first_use_penalty=self.first_use_penalty,
            feature_reuse_penalty=self.feature_reuse_penalty,
            gain_confidence_level=self.gain_conf_level,
            softmax_temperature=self.softmax_temperature,
            execution_time=self.execution_time,
            feature_fraction=self.feature_fraction,
            bagging_size=self.bagging_size,
            bagging_example_fraction=self.bagging_example_fraction,
            feature_fraction_per_split=self.feature_fraction_per_split,
            smoothing=self.smoothing,
            allow_empty_trees=self.allow_empty_trees,
            feature_compression_level=self.feature_compression_level,
            compress_ensemble=self.compress_ensemble,
            test_frequency=self.test_frequency)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)