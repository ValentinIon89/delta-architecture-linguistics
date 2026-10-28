"""Functional regression tests for the existing didactic Delta architecture script.

These tests verify documented program behavior, not scientific validation of the
linguistic model or an automatic R0 diagnostic.
"""
import contextlib
import io
import unittest

from delta_architecture import (
    DeltaArchitecture,
    DependentComponent,
    MicroConfiguration,
    RelationalNucleus,
)


class DeltaArchitectureTests(unittest.TestCase):
    def setUp(self):
        self.r0 = RelationalNucleus("lexeme-test")

    def call_silently(self, method, *args):
        with contextlib.redirect_stdout(io.StringIO()):
            return method(*args)

    def test_r0_identity_is_label_comparison_only(self):
        self.assertTrue(DeltaArchitecture.r0_candidate_matches(self.r0, RelationalNucleus("lexeme-test")))
        self.assertFalse(DeltaArchitecture.r0_candidate_matches(self.r0, RelationalNucleus("other")))

    def test_directional_example_surface(self):
        initial = MicroConfiguration(self.r0, "zi")
        resulting = MicroConfiguration(self.r0, "zi", [DependentComponent("le")])
        self.assertEqual(initial.get_surface_form(), "zi")
        self.assertEqual(resulting.get_surface_form(), "zile")
        self.assertIsNone(self.call_silently(DeltaArchitecture.directional_regime, initial, resulting))

    def test_additive_regime(self):
        initial = MicroConfiguration(self.r0, "merg")
        result = self.call_silently(DeltaArchitecture.additive_regime, initial, DependentComponent("eam"))
        self.assertEqual(result.get_surface_form(), "mergeam")
        self.assertEqual(initial.get_surface_form(), "merg")

    def test_semantic_redistribution_renders_manually_specified_form(self):
        initial = MicroConfiguration(self.r0, "trust")
        result = self.call_silently(
            DeltaArchitecture.semantic_redistribution_regime,
            DependentComponent("dis", "prefix"), initial, "negative orientation",
        )
        self.assertEqual(result.get_surface_form(), "distrust")

    def test_substitutional_regime(self):
        initial = MicroConfiguration(self.r0, "cas", [DependentComponent("ă")])
        result = self.call_silently(
            DeltaArchitecture.substitutional_regime, initial, "ă", DependentComponent("e")
        )
        self.assertEqual(initial.get_surface_form(), "casă")
        self.assertEqual(result.get_surface_form(), "case")
        self.assertEqual(result.r0, initial.r0)

    def test_relational_coupling(self):
        base = MicroConfiguration(self.r0, "άντρας")
        result = self.call_silently(
            DeltaArchitecture.relational_coupling_regime,
            DependentComponent("ο", "relational"), base,
        )
        self.assertEqual(result, "ο άντρας")

    def test_reductive_regime(self):
        initial = MicroConfiguration(self.r0, "γελάδα", [DependentComponent("α", "prefix")])
        result = self.call_silently(DeltaArchitecture.reductive_regime, initial, "α")
        self.assertEqual(initial.get_surface_form(), "αγελάδα")
        self.assertEqual(result.get_surface_form(), "γελάδα")

    def test_positional_reorganization(self):
        result = self.call_silently(
            DeltaArchitecture.positional_reorganization_regime, ("l", "a"), 0, 1, "constructed"
        )
        self.assertEqual(result, ("a", "l"))
        result2 = self.call_silently(
            DeltaArchitecture.positional_reorganization_regime, ("a", "s", "k"), 1, 2, "attested"
        )
        self.assertEqual("".join(result2), "aks")

    def test_cumulative_greek_paradigm(self):
        paradigm = [
            ("ω", "1sg"), ("εις", "2sg"), ("ει", "3sg"),
            ("ουμε", "1pl"), ("ετε", "2pl"), ("ουν", "3pl"),
        ]
        result = self.call_silently(DeltaArchitecture.cumulative_paradigmatic_regime, "γράφ", paradigm)
        self.assertEqual(result, ["γράφω", "γράφεις", "γράφει", "γράφουμε", "γράφετε", "γράφουν"])

    def test_infix_and_component_validation(self):
        with self.assertRaises(ValueError):
            DependentComponent("x", "infix")
        with self.assertRaises(ValueError):
            MicroConfiguration(self.r0, "abc", [DependentComponent("x", "infix", offset=4)])
        form = MicroConfiguration(self.r0, "abc", [DependentComponent("x", "infix", offset=1)])
        self.assertEqual(form.get_surface_form(), "axbc")

    def test_reject_invalid_substitution(self):
        initial = MicroConfiguration(self.r0, "cas", [DependentComponent("ă", "suffix")])
        with self.assertRaises(ValueError):
            self.call_silently(
                DeltaArchitecture.substitutional_regime,
                initial, "ă", DependentComponent("e", "prefix"),
            )

    def test_reject_invalid_relational_or_paradigmatic_inputs(self):
        with self.assertRaises(ValueError):
            self.call_silently(
                DeltaArchitecture.additive_regime,
                MicroConfiguration(self.r0, "cas"), DependentComponent("o", "relational"),
            )
        with self.assertRaises(ValueError):
            self.call_silently(
                DeltaArchitecture.cumulative_paradigmatic_regime,
                "γράφ", [("ω", "1sg"), ("εις", "2sg")],
            )


if __name__ == "__main__":
    unittest.main()
