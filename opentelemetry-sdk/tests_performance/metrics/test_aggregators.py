# Copyright 2020, OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from opentelemetry.sdk.metrics.export import aggregate

@pytest.mark.benchmark(
    group="counter-aggregator",
    min_time=0.5,
    max_time=1.0,
    min_rounds=5,
    disable_gc=True,
    warmup=True,
    warmup_iterations=10**5,
)
class TestCounterAggregator:
    def test_float(self, benchmark):
        counter = aggregate.CounterAggregator()
        benchmark(counter.update, 3.123)

    def test_int(self, benchmark):
        counter = aggregate.CounterAggregator()
        benchmark(counter.update, 3)

@pytest.mark.benchmark(
    group="mmsc-aggregator",
    min_time=0.5,
    max_time=1.0,
    min_rounds=5,
    disable_gc=True,
    warmup=True,
    warmup_iterations=10**5,
)
class TestMMSCAggregator:
    def test_float(self, benchmark):
        mmsc = aggregate.MinMaxSumCountAggregator()
        benchmark(mmsc.update, 3.123)

    def test_int(self, benchmark):
        mmsc = aggregate.MinMaxSumCountAggregator()
        benchmark(mmsc.update, 3)

@pytest.mark.benchmark(
    group="observer-aggregator",
    min_time=0.5,
    max_time=1.0,
    min_rounds=5,
    disable_gc=True,
    warmup=True,
    warmup_iterations=10**5,
)
class TestObserverAggregator:
    def test_float(self, benchmark):
        observer = aggregate.ObserverAggregator()
        benchmark(observer.update, 3.123)

    def test_int(self, benchmark):
        observer = aggregate.ObserverAggregator()
        benchmark(observer.update, 3)