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

from opentelemetry import metrics as metrics_api
from opentelemetry.sdk import metrics, resources
from opentelemetry.sdk.metrics import export

class TestCounter:
    def test_direct_int(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        counter = metrics.Counter("name", "desc", "unit", int, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)

        benchmark(counter.add, 3, label_set)

    def test_direct_float(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        counter = metrics.Counter("name", "desc", "unit", float, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)

        benchmark(counter.add, 3.12, label_set)

    def test_bound_int(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        counter = metrics.Counter("name", "desc", "unit", int, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)
        bound_counter = counter.bind(label_set)

        benchmark(bound_counter.add, 3)

    def test_bound_float(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        counter = metrics.Counter("name", "desc", "unit", float, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)
        bound_counter = counter.bind(label_set)

        benchmark(bound_counter.add, 3.12)

class TestMeasure:
    def test_direct_int(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        measure = metrics.Measure("name", "desc", "unit", int, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)

        benchmark(measure.record, 3, label_set)

    def test_direct_float(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        measure = metrics.Measure("name", "desc", "unit", float, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)

        benchmark(measure.record, 3.12, label_set)

    def test_bound_int(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        measure = metrics.Measure("name", "desc", "unit", int, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)
        bound_counter = measure.bind(label_set)

        benchmark(bound_counter.record, 3)

    def test_bound_float(self, benchmark):
        meter = metrics.MeterProvider().get_meter(__name__)
        measure = metrics.Measure("name", "desc", "unit", float, meter, ("key",))
        kvp = {"key": "value"}
        label_set = meter.get_label_set(kvp)
        bound_counter = measure.bind(label_set)

        benchmark(bound_counter.record, 3.12)
