#!/usr/bin/env python3
"""Finite specification examples, not an INDEX-ALIGN-CERT implementation.

Run with Python 3.10+ and the standard library only. The default JSON receipt is
written beside this script. These checks exercise a small explicit mathematical
model and preserve counterexamples to the superseded statements. They do not
test an LLM, establish checker soundness, prove graph completeness, enforce an
execution boundary, or demonstrate the framework's empirical efficacy.
"""

from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
import unittest


def concentration(
    masses: tuple[int, ...] | None,
    windows: tuple[tuple[int, int], ...] | None,
    alpha: Fraction,
) -> Fraction | None:
    """Return the restricted subspan mass ratio, or None for UNKNOWN.

    A chunk consists of equally spaced discrete units. A window [start, end)
    is contiguous and its length is end-start. Missing measure/windows, zero
    total mass, and no eligible nonempty window leave the observable unknown.
    Invalid supplied mathematical objects are errors, never a semantic PASS.
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be strictly between zero and one")
    if masses is None or windows is None:
        return None
    if any(mass < 0 for mass in masses):
        raise ValueError("a mass measure must be nonnegative")
    length = len(masses)
    if any(not (0 <= start < end <= length) for start, end in windows):
        raise ValueError("windows must be nonempty contiguous chunk subspans")
    total = sum(masses)
    eligible = [(start, end) for start, end in windows
                if end - start <= alpha * length]
    if total == 0 or not eligible:
        return None
    return max(Fraction(sum(masses[start:end]), total)
               for start, end in eligible)


def concentration_verdict(masses, windows, alpha, threshold):
    """A small model of the declared cap, with no inferred default threshold."""
    if threshold is None:
        return "NO_VERDICT"
    value = concentration(masses, windows, alpha)
    if value is None:
        return "UNKNOWN"
    return "PASS" if value <= threshold else "FAIL"


def kleene_and(verdicts: tuple[str, ...]) -> str:
    if any(value not in {"T", "F", "U"} for value in verdicts):
        raise ValueError("only T/F/U are semantic monitor values")
    if "F" in verdicts:
        return "F"
    if "U" in verdicts:
        return "U"
    return "T"


def release_bit(verdict: str) -> int:
    """Control projection only; zero is not an assertion of semantic falsity."""
    return int(verdict == "PASS")


def minimal_failed_nodes(nodes, edges, failed):
    """Compute Min(failed) in the supplied finite DAG, including transitive order.

    This function assumes the graph supplied by the caller is the relevant
    graph. It does not certify missing-edge absence or actual system causality.
    """
    nodes, failed = set(nodes), set(failed)
    if not failed <= nodes:
        raise ValueError("every failure must identify a declared node")
    successors = {node: set() for node in nodes}
    indegree = dict.fromkeys(nodes, 0)
    for before, after in edges:
        if before not in nodes or after not in nodes:
            raise ValueError("an edge endpoint is undeclared")
        if after not in successors[before]:
            successors[before].add(after)
            indegree[after] += 1
    ready = deque(sorted(node for node in nodes if indegree[node] == 0))
    failed_ancestor = dict.fromkeys(nodes, False)
    frontier = set()
    visited = 0
    while ready:
        node = ready.popleft()
        visited += 1
        if node in failed and not failed_ancestor[node]:
            frontier.add(node)
        for child in sorted(successors[node]):
            failed_ancestor[child] |= failed_ancestor[node] or node in failed
            indegree[child] -= 1
            if indegree[child] == 0:
                ready.append(child)
    if visited != len(nodes):
        raise ValueError("causal order must be acyclic")
    return frontier


def partition_depth(induction_level: int, maximum_depth: int) -> int:
    if not 0 <= induction_level <= maximum_depth:
        raise ValueError("induction level is outside the declared ladder")
    return maximum_depth - induction_level


def first_observed_failure(verdicts, declared_order):
    """Locate an observed F under a declared permutation of partition depths."""
    if sorted(declared_order) != list(range(len(verdicts))):
        raise ValueError("the order must enumerate every partition depth once")
    if any(value not in {"T", "F", "U"} for value in verdicts):
        raise ValueError("only T/F/U are semantic monitor values")
    for position, depth in enumerate(declared_order):
        if verdicts[depth] == "F":
            return {"order_position": position, "partition_depth": depth,
                    "induction_level": len(verdicts) - 1 - depth}
    return None


def reconciliation_cost_bound(round_cap, call_bounds, enforced_deadline=None):
    """Abstract repair-work bound, not an implementation of cancellation/timeouts.

    None denotes a call with no known finite bound. A finite round cap alone
    cannot bound such a call. A supplied deadline is an ASSUMED effective bound
    on each entire call, including cancellation; no running process is tested.
    This excludes initial/final readiness assessments, which must also terminate.
    Per-repair control overhead must be included in the supplied call bounds.
    """
    if round_cap < 0 or any(b is not None and b < 0 for b in call_bounds):
        raise ValueError("work bounds must be nonnegative")
    if enforced_deadline is not None and enforced_deadline < 0:
        raise ValueError("a deadline bound must be nonnegative")
    if round_cap == 0:
        return 0
    if enforced_deadline is None and any(b is None for b in call_bounds):
        return None
    bounds = [b if enforced_deadline is None else
              enforced_deadline if b is None else min(b, enforced_deadline)
              for b in call_bounds]
    return round_cap * sum(bounds)


def reconcile_finite_example(required_repairs, repair_cap):
    """Toy repair counter with terminating checks; no trace or effect execution."""
    for value in (required_repairs, repair_cap):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("repair counts must be nonnegative integers")
    remaining = required_repairs
    for attempted in range(repair_cap + 1):
        if remaining == 0:
            return "READY", attempted
        if attempted == repair_cap:
            break
        remaining -= 1
    return "NO_VERDICT", repair_cap


CHUNK_WINDOWS = tuple((start, end) for start in range(4)
                      for end in range(start + 1, 5))
HALF = Fraction(1, 2)


class SpecificationExamples(unittest.TestCase):
    def test_restricted_concentration_distinguishes_two_distributions(self):
        self.assertEqual(concentration((1, 1, 1, 1), CHUNK_WINDOWS, HALF), HALF)
        self.assertEqual(concentration((4, 0, 0, 0), CHUNK_WINDOWS, HALF), 1)

    def test_superseded_full_chunk_formula_is_constant(self):
        for masses in ((1, 1, 1, 1), (4, 0, 0, 0), (0, 2, 1, 0)):
            old_value = max(Fraction(sum(masses[start:end]), sum(masses))
                            for start, end in CHUNK_WINDOWS)
            self.assertEqual(old_value, 1)

    def test_window_size_boundary_excludes_full_chunk(self):
        self.assertEqual(concentration((1, 1, 1, 1), ((0, 4), (0, 2)), HALF), HALF)

    def test_absent_measure_is_unknown(self):
        self.assertEqual(concentration_verdict(None, CHUNK_WINDOWS, HALF, 1),
                         "UNKNOWN")

    def test_absent_window_contract_is_unknown(self):
        self.assertEqual(concentration_verdict((1, 1, 1, 1), None, HALF, 1),
                         "UNKNOWN")

    def test_empty_or_ineligible_windows_are_unknown(self):
        for windows, alpha in (((), HALF), (CHUNK_WINDOWS, Fraction(1, 8))):
            self.assertIsNone(concentration((1, 1, 1, 1), windows, alpha))

    def test_zero_mass_denominator_is_unknown(self):
        self.assertIsNone(concentration((0, 0, 0, 0), CHUNK_WINDOWS, HALF))

    def test_missing_threshold_is_no_verdict(self):
        self.assertEqual(concentration_verdict((1, 1, 1, 1), CHUNK_WINDOWS,
                                             HALF, None), "NO_VERDICT")

    def test_declared_threshold_separates_examples(self):
        self.assertEqual(concentration_verdict((1, 1, 1, 1), CHUNK_WINDOWS,
                                             HALF, Fraction(3, 4)), "PASS")
        self.assertEqual(concentration_verdict((4, 0, 0, 0), CHUNK_WINDOWS,
                                             HALF, Fraction(3, 4)), "FAIL")

    def test_invalid_observable_inputs_do_not_become_passes(self):
        for alpha in (Fraction(0), Fraction(1)):
            with self.assertRaises(ValueError):
                concentration((1, 1, 1, 1), CHUNK_WINDOWS, alpha)
        with self.assertRaises(ValueError):
            concentration((-1, 2, 1, 1), CHUNK_WINDOWS, HALF)
        with self.assertRaises(ValueError):
            concentration((1, 1, 1, 1), ((0, 5),), HALF)

    def test_zero_threshold_scalar_matches_conjunction(self):
        for arity in range(1, 7):
            weight_sets = (tuple(range(1, arity + 1)),
                           tuple(Fraction(1, i + 1) for i in range(arity)))
            for weights in weight_sets:
                for bits in product((0, 1), repeat=arity):
                    deficit = sum(w * (1 - bit) for w, bit in zip(weights, bits))
                    self.assertEqual(deficit == 0, all(bits))

    def test_strong_kleene_preserves_sound_finite_inputs(self):
        for arity in range(1, 5):
            for semantics in product((0, 1), repeat=arity):
                admissible = [("T", "U") if value else ("F", "U")
                              for value in semantics]
                for verdicts in product(*admissible):
                    aggregate = kleene_and(verdicts)
                    if aggregate == "T":
                        self.assertTrue(all(semantics))
                    if aggregate == "F":
                        self.assertFalse(all(semantics))

    def test_failed_sufficient_child_does_not_establish_false_parent(self):
        # R is a sufficient implication, not an equivalence. This finite model
        # satisfies (p AND r) => (p OR r) for every assignment.
        for p, r in product((False, True), repeat=2):
            self.assertTrue(not (p and r) or (p or r))
        p, r = False, True
        self.assertEqual(kleene_and(("F", "T")), "F")
        self.assertTrue(p or r, "a child failure must not be copied to this parent")

    def test_unknown_does_not_license_release_or_imply_false(self):
        self.assertEqual(kleene_and(("T", "U")), "U")
        self.assertEqual(kleene_and(("F", "U")), "F")
        for value in ("FAIL", "UNKNOWN", "NO_VERDICT", "SKIPPED"):
            self.assertEqual(release_bit(value), 0)
        self.assertEqual(release_bit("PASS"), 1)

    def test_frontier_excludes_nonminimal_incomparable_descendant(self):
        self.assertEqual(minimal_failed_nodes({"a", "b", "c"},
                                             {("a", "c")}, {"a", "b", "c"}),
                         {"a", "b"})

    def test_frontier_uses_transitive_order_through_nonfailed_nodes(self):
        self.assertEqual(minimal_failed_nodes({"a", "b", "c", "x"},
                                             {("a", "x"), ("x", "c")},
                                             {"a", "b", "c"}), {"a", "b"})

    def test_frontier_rejects_cycles_and_undeclared_nodes(self):
        with self.assertRaises(ValueError):
            minimal_failed_nodes({"a", "b"}, {("a", "b"), ("b", "a")}, {"a"})
        with self.assertRaises(ValueError):
            minimal_failed_nodes({"a"}, {("a", "missing")}, {"a"})

    def test_partition_and_induction_indices_run_in_opposite_directions(self):
        partitions = ((frozenset(range(4)),),
                      (frozenset((0, 1)), frozenset((2, 3))),
                      tuple(frozenset((i,)) for i in range(4)))
        maximum_depth = len(partitions) - 1
        self.assertEqual([partition_depth(j, maximum_depth) for j in range(3)],
                         [2, 1, 0])
        for level in range(1, 3):
            parents = partitions[partition_depth(level, maximum_depth)]
            children = partitions[partition_depth(level - 1, maximum_depth)]
            for child in children:
                self.assertEqual(sum(child <= parent for parent in parents), 1)
            for parent in parents:
                self.assertEqual(frozenset().union(*(c for c in children if c <= parent)),
                                 parent)

    def test_first_failure_depends_on_declared_order_and_records_partition(self):
        # Entries are indexed by partition depth k; an unknown is not a failure.
        verdicts = ("U", "F", "T", "F")
        coarse_first = (0, 1, 2, 3)
        finest_first = (3, 2, 1, 0)
        self.assertEqual(first_observed_failure(verdicts, coarse_first),
                         {"order_position": 1, "partition_depth": 1,
                          "induction_level": 2})
        self.assertEqual(first_observed_failure(verdicts, finest_first),
                         {"order_position": 0, "partition_depth": 3,
                          "induction_level": 0})
        self.assertIsNone(first_observed_failure(("T", "U"), (1, 0)))
        with self.assertRaises(ValueError):
            first_observed_failure(verdicts, (0, 1, 1, 3))

    def test_individually_valid_field_reads_do_not_establish_joint_snapshot(self):
        # Finite history counterexample, NOT a concurrency implementation test.
        # The only committed joint states are before and after one atomic update.
        joint_states = (("policy-v1", "registry-v1"),
                        ("policy-v2", "registry-v2"))
        reads = ((0, 0, "policy-v1"), (1, 1, "registry-v2"))
        # Each read can linearize at its indicated state: first before the
        # update, second after it. Their individually valid results never coexist.
        for state_index, field_index, returned_value in reads:
            self.assertEqual(returned_value, joint_states[state_index][field_index])
        observed_pair = tuple(returned_value for _, _, returned_value in reads)
        self.assertEqual(observed_pair, ("policy-v1", "registry-v2"))
        self.assertNotIn(observed_pair, joint_states)

    def test_round_cap_alone_cannot_bound_an_unbounded_call(self):
        self.assertIsNone(reconciliation_cost_bound(3, (None, 2)))

    def test_initially_clean_state_needs_no_repair_budget(self):
        self.assertEqual(reconcile_finite_example(0, 0), ("READY", 0))

    def test_final_allowed_repair_is_assessed_before_exhaustion(self):
        self.assertEqual(reconcile_finite_example(2, 2), ("READY", 2))
        self.assertEqual(reconcile_finite_example(2, 1), ("NO_VERDICT", 1))
        for invalid in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                reconcile_finite_example(2, invalid)

    def test_finite_calls_or_assumed_enforced_deadlines_supply_a_bound(self):
        self.assertEqual(reconciliation_cost_bound(3, (4, 2)), 18)
        self.assertEqual(reconciliation_cost_bound(3, (None, 2), enforced_deadline=5), 21)
        self.assertEqual(reconciliation_cost_bound(0, (None, 2)), 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("specification-checks.json"))
    args = parser.parse_args()
    loader = unittest.TestLoader()
    test_names = loader.getTestCaseNames(SpecificationExamples)
    result = unittest.TextTestRunner(verbosity=2).run(
        loader.loadTestsFromTestCase(SpecificationExamples))
    failed_names = {test._testMethodName for test, _ in result.failures + result.errors}
    receipt = {
        "kind": "finite-specification-examples",
        "scope": "Deterministic finite examples and counterexamples only; not INDEX-ALIGN-CERT implementation or LLM efficacy tests.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": sys.version.split()[0],
        "passed": result.wasSuccessful(),
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "checks": [{"name": name, "passed": name not in failed_names}
                   for name in test_names],
        "examples": {
            "concentration_alpha": "1/2",
            "uniform_mass": [1, 1, 1, 1],
            "concentrated_mass": [4, 0, 0, 0],
            "repaired_concentration": {"uniform": "1/2", "concentrated": "1"},
            "superseded_concentration": {"uniform": "1", "concentrated": "1"},
            "scalar_conjunction_cases": 252,
            "strong_kleene_sound_input_cases": 340,
            "failed_sufficient_child_counterexample": {
                "children": [False, True],
                "parent_disjunction": True,
                "sufficient_implication_holds_on_all_four_assignments": True,
            },
            "minimal_frontier": ["a", "b"],
            "partition_depths_for_induction_levels_0_1_2": [2, 1, 0],
            "first_failure_partition_depth": {"coarse_first": 1, "finest_first": 3},
            "field_read_snapshot_counterexample": {
                "joint_states": [["policy-v1", "registry-v1"],
                                 ["policy-v2", "registry-v2"]],
                "individually_valid_mixed_pair": ["policy-v1", "registry-v2"],
                "mixed_pair_was_jointly_present": False,
            },
            "round_cap_only_with_unbounded_call": "NO_FINITE_BOUND",
            "finite_repair_examples": {
                "initially_clean_at_zero_budget": list(reconcile_finite_example(0, 0)),
                "success_on_final_allowed_repair": list(reconcile_finite_example(2, 2)),
                "insufficient_repair_budget": list(reconcile_finite_example(2, 1)),
            },
        },
        "limitations": [
            "Sound primitive checkers, complete obligation/dependency inventories and valid real-system refinement witnesses are not established.",
            "Finite truth-table checks supplement, but do not replace, general proofs.",
            "The mixed-field snapshot history is a counterexample; it does not test a concurrent store or an actual linearizability implementation.",
            "The deadline example assumes effective interruption including cleanup; it does not execute or validate a timeout mechanism.",
            "No model calls, live actions, framework mutation trials, performance claims or empirical cost savings are tested.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(f"Receipt: {args.output}")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
