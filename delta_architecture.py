"""Didactic rendering of selected examples from the Δ architecture.

This is a small, manually specified demonstration. R₀ is kept as an abstract
relational identifier, separate from the surface base used to render forms.
The script does not implement the full ordered R₀ diagnostic or automatically
classify linguistic data.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

try:
    import colorama
    from colorama import Fore, Style

    colorama.init(autoreset=True)
except ImportError:  # The script remains usable without optional terminal colors.
    class Fore:
        WHITE = CYAN = GREEN = MAGENTA = RED = BLUE = YELLOW = ""

    class Style:
        RESET_ALL = ""


@dataclass(frozen=True)
class RelationalNucleus:
    """An abstract R₀ identifier, not a phonological root or surface string."""

    identity: str

    def __str__(self) -> str:
        return f"R₀[{self.identity}]"


@dataclass
class DependentComponent:
    value: str
    position: str = "suffix"
    color: str = Fore.WHITE
    # Required for an infix: number of base characters before the insertion.
    offset: Optional[int] = None

    def __post_init__(self) -> None:
        if self.position not in {"prefix", "infix", "suffix", "relational"}:
            raise ValueError("Position must be prefix, infix, suffix, or relational.")
        if self.position == "infix" and self.offset is None:
            raise ValueError("An infix component requires an explicit offset.")
        if self.position != "infix" and self.offset is not None:
            raise ValueError("An offset is only valid for an infix component.")


@dataclass
class MicroConfiguration:
    """R₀ and the rendered base are separate; components are manually supplied."""

    r0: RelationalNucleus
    base: str
    components: List[DependentComponent] = field(default_factory=list)

    def __post_init__(self) -> None:
        if any(c.position == "relational" for c in self.components):
            raise ValueError("Relational elements are coupled separately, not embedded as affixes.")
        for component in self.components:
            if component.position == "infix" and not 0 <= component.offset <= len(self.base):
                raise ValueError("An infix offset must fall within the rendered base.")

    def get_surface_form(self) -> str:
        prefixes = "".join(c.value for c in self.components if c.position == "prefix")
        suffixes = "".join(c.value for c in self.components if c.position == "suffix")
        infixes = {}
        for component in self.components:
            if component.position == "infix":
                infixes.setdefault(component.offset, []).append(component.value)
        rendered_base = "".join(
            ("".join(infixes.get(i, [])) + char)
            for i, char in enumerate(self.base)
        ) + "".join(infixes.get(len(self.base), []))
        return f"{prefixes}{rendered_base}{suffixes}"

    def get_chromatic_form(self) -> str:
        prefixes = "".join(
            f"{c.color}{c.value}{Style.RESET_ALL}"
            for c in self.components if c.position == "prefix"
        )
        suffixes = "".join(
            f"{c.color}{c.value}{Style.RESET_ALL}"
            for c in self.components if c.position == "suffix"
        )
        infixes = {}
        for component in self.components:
            if component.position == "infix":
                infixes.setdefault(component.offset, []).append(
                    f"{component.color}{component.value}{Style.RESET_ALL}"
                )
        rendered_base = "".join(
            "".join(infixes.get(i, [])) + f"{Fore.WHITE}{char}{Style.RESET_ALL}"
            for i, char in enumerate(self.base)
        ) + "".join(infixes.get(len(self.base), []))
        return f"{prefixes}{rendered_base}{suffixes}"


class DeltaArchitecture:
    @staticmethod
    def r0_candidate_matches(initial: RelationalNucleus, resulting: RelationalNucleus) -> bool:
        """Compare supplied R₀ labels only; this is not the full R₀ diagnostic."""
        return initial.identity == resulting.identity

    @staticmethod
    def directional_regime(initial: MicroConfiguration, resulting: MicroConfiguration) -> None:
        print(f"{Fore.CYAN}=== 1. Δ(→): corespondență direcțională ==={Style.RESET_ALL}")
        print(f"Corespondență orientată: {initial.get_chromatic_form()} → {resulting.get_chromatic_form()}")
        print("Δ(→) înregistrează corespondența; orice intervenție internă se clasifică separat, dacă este analizată.\n")

    @staticmethod
    def additive_regime(initial: MicroConfiguration, new_component: DependentComponent) -> MicroConfiguration:
        if new_component.position == "relational":
            raise ValueError("A relational component is not integrated by Δ(+).")
        print(f"{Fore.CYAN}=== 2. Δ(+): integrare ==={Style.RESET_ALL}")
        resulting = MicroConfiguration(initial.r0, initial.base, initial.components + [new_component])
        print(f"Configurație inițială: {initial.get_chromatic_form()}")
        print(f"Material integrat: {new_component.value}")
        print(f"Configurație rezultată: {resulting.get_chromatic_form()}\n")
        return resulting

    @staticmethod
    def semantic_redistribution_regime(
        dependent_component: DependentComponent,
        base: MicroConfiguration,
        semantic_effect: str,
    ) -> MicroConfiguration:
        if dependent_component.position == "relational":
            raise ValueError("Relational coupling is represented by Δ(>/<), not Δ(><).")
        print(f"{Fore.CYAN}=== 3. Δ(><): reorientare semantică/gramaticală ==={Style.RESET_ALL}")
        resulting = MicroConfiguration(base.r0, base.base, base.components + [dependent_component])
        print(f"Bază: {base.get_chromatic_form()}")
        print(f"Formă ilustrată: {resulting.get_chromatic_form()}")
        print(f"Reorientare indicată manual: {semantic_effect}")
        print("Programul doar redă forma; efectul semantic nu este calculat. Integrarea materialului se clasifică separat prin Δ(+) când este analizată.\n")
        return resulting

    @staticmethod
    def substitutional_regime(
        initial: MicroConfiguration,
        eliminate_value: str,
        introduced_component: DependentComponent,
    ) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 4. Δ(−/+): înlocuire corelată ==={Style.RESET_ALL}")
        matches = [i for i, c in enumerate(initial.components) if c.value == eliminate_value]
        if len(matches) != 1:
            raise ValueError("Exemplul trebuie să conțină exact o componentă de eliminat.")
        index = matches[0]
        eliminated = initial.components[index]
        if (eliminated.position, eliminated.offset) != (introduced_component.position, introduced_component.offset):
            raise ValueError("Componenta introdusă trebuie să ocupe aceeași poziție structurală.")
        updated = list(initial.components)
        updated[index] = introduced_component
        resulting = MicroConfiguration(initial.r0, initial.base, updated)
        print(f"Configurație inițială: {initial.get_chromatic_form()}")
        print(f"Înlocuire în aceeași poziție: {eliminate_value} → {introduced_component.value}")
        print(f"Configurație rezultată: {resulting.get_chromatic_form()}\n")
        return resulting

    @staticmethod
    def relational_coupling_regime(relation_element: DependentComponent, base: MicroConfiguration) -> str:
        if relation_element.position != "relational":
            raise ValueError("The coupled element must be marked as relational.")
        print(f"{Fore.CYAN}=== 5. Δ(>/<): cuplare relațională ==={Style.RESET_ALL}")
        surface = f"{relation_element.value} {base.get_surface_form()}"
        print(f"Relație stabilizată: {relation_element.value} / {base.get_surface_form()}")
        print(f"Configurație: {surface}\n")
        return surface

    @staticmethod
    def reductive_regime(initial: MicroConfiguration, eliminate_value: str) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 6. Δ(−): eliminare ==={Style.RESET_ALL}")
        matches = [i for i, c in enumerate(initial.components) if c.value == eliminate_value]
        if len(matches) != 1:
            raise ValueError("Exemplul trebuie să conțină exact o componentă de eliminat.")
        index = matches[0]
        updated = list(initial.components)
        eliminated = updated.pop(index)
        resulting = MicroConfiguration(initial.r0, initial.base, updated)
        print(f"Configurație inițială: {initial.get_chromatic_form()}")
        print(f"Material eliminat: {eliminated.value}")
        print(f"Configurație rezultată: {resulting.get_chromatic_form()}\n")
        return resulting

    @staticmethod
    def positional_reorganization_regime(
        components: Tuple[str, ...], first_index: int, second_index: int, example_note: str
    ) -> Tuple[str, ...]:
        if first_index == second_index or not (0 <= first_index < len(components)) or not (0 <= second_index < len(components)):
            raise ValueError("Indicați două poziții distincte existente în configurație.")
        reordered = list(components)
        reordered[first_index], reordered[second_index] = reordered[second_index], reordered[first_index]
        result = tuple(reordered)
        print(f"{Fore.CYAN}=== 7. Δ(~): reorganizare pozițională ==={Style.RESET_ALL}")
        print(f"Ilustrație: {''.join(components)} ~ {''.join(result)}")
        print(f"Notă: {example_note}\n")
        return result

    @staticmethod
    def cumulative_paradigmatic_regime(stem: str, paradigm: List[Tuple[str, str]]) -> List[str]:
        if len(paradigm) < 3:
            raise ValueError("Δ(±) cere un domeniu paradigmatic de cel puțin trei forme.")
        forms = [stem + ending for ending, _ in paradigm]
        print(f"{Fore.CYAN}=== 8. Δ(±): domeniu paradigmatic cumulativ (k={len(forms)}) ==={Style.RESET_ALL}")
        for index, ((ending, grammatical_value), form) in enumerate(zip(paradigm, forms), 1):
            print(f"  A{index} [{grammatical_value}]: {stem}{Fore.YELLOW}{ending}{Style.RESET_ALL} = {form}")
        print("Δ(±) clasifică domeniul stabilizat ca întreg.")
        print("Relațiile locale analizate între forme sunt Δ(−/+) când există înlocuire în aceeași poziție:")
        for index in range(len(forms) - 1):
            ending_a = paradigm[index][0]
            ending_b = paradigm[index + 1][0]
            print(f"  A{index + 1} (−{ending_a} + {ending_b}) = A{index + 2}")
        print()
        return forms


if __name__ == "__main__":
    print(f"{Fore.GREEN}DEMONSTRAȚIE DIDACTICĂ A UNOR REPREZENTĂRI Δ{Style.RESET_ALL}\n")

    zi_r0 = RelationalNucleus("lexeme-zi")
    zi = MicroConfiguration(zi_r0, "zi")
    zile = MicroConfiguration(zi_r0, "zi", [DependentComponent("le", "suffix", Fore.BLUE)])
    DeltaArchitecture.directional_regime(zi, zile)

    merg = MicroConfiguration(RelationalNucleus("lexeme-merg"), "merg")
    DeltaArchitecture.additive_regime(merg, DependentComponent("eam", "suffix", Fore.GREEN))

    trust = MicroConfiguration(RelationalNucleus("lexeme-trust"), "trust")
    DeltaArchitecture.semantic_redistribution_regime(
        DependentComponent("dis", "prefix", Fore.MAGENTA), trust, "reorientare negativă"
    )
    urs = MicroConfiguration(RelationalNucleus("lexeme-urs"), "urs")
    DeltaArchitecture.semantic_redistribution_regime(
        DependentComponent("oaică", "suffix", Fore.MAGENTA), urs, "valoare lexicală/gramaticală feminină"
    )

    casa = MicroConfiguration(RelationalNucleus("lexeme-cas"), "cas", [DependentComponent("ă", "suffix", Fore.RED)])
    DeltaArchitecture.substitutional_regime(casa, "ă", DependentComponent("e", "suffix", Fore.GREEN))

    andras = MicroConfiguration(RelationalNucleus("lexeme-antras"), "άντρας")
    DeltaArchitecture.relational_coupling_regime(DependentComponent("ο", "relational", Fore.CYAN), andras)

    agelada = MicroConfiguration(RelationalNucleus("lexeme-gelada"), "γελάδα", [DependentComponent("α", "prefix", Fore.RED)])
    DeltaArchitecture.reductive_regime(agelada, "α")

    DeltaArchitecture.positional_reorganization_regime(
        ("l", "a"), 0, 1, "la ~ al este o ilustrație construită; nu dovedește continuitatea empirică a lui R₀."
    )
    DeltaArchitecture.positional_reorganization_regime(
        ("a", "s", "k"), 1, 2, "ask ~ aks este alternanța engleză atestată menționată în apendice."
    )

    greek_present = [
        ("ω", "persoana I singular"),
        ("εις", "persoana II singular"),
        ("ει", "persoana III singular"),
        ("ουμε", "persoana I plural"),
        ("ετε", "persoana II plural"),
        ("ουν", "persoana III plural"),
    ]
    DeltaArchitecture.cumulative_paradigmatic_regime("γράφ", greek_present)
