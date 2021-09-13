"""Basic definitions for the distributions module."""

import tensorflow as tf


class Distribution(tf.keras.layers.Layer):
    """Distribution base class."""

    def log_prob(self, x):
        """Calculate log probability under the distribution.
        Args:
            x: Tensor, shape (batch_size, ...)
        Returns:
            log_prob: Tensor, shape (batch_size,)
        """
        raise NotImplementedError()

    def sample(self, num_samples):
        """Generates samples from the distribution.
        Args:
            num_samples: int, number of samples to generate.
        Returns:
            samples: Tensor, shape (num_samples, ...)
        """
        raise NotImplementedError()

    def sample_with_log_prob(self, num_samples):
        """Generates samples from the distribution together with their log probability.
        Args:
            num_samples: int, number of samples to generate.
        Returns:
            samples: Tensor, shape (num_samples, ...)
            log_prob: Tensor, shape (num_samples,)
        """
        samples = self.sample(num_samples)
        log_prob = self.log_prob(samples)
        return samples, log_prob

    def call(self, *args):
        '''
        Not implemented for Distributions
        '''
        raise RuntimeError("Forward method cannot be called for a Distribution.")