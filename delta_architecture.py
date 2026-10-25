python
import colorama
from colorama import Fore, Style
from typing import List, Tuple

colorama.init(autoreset=True)

class RelationalNucleus:
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        return f"R0({self.value})"

class DependentComponent:
    def __init__(self, value: str, position: str = "suffix", color: str = Fore.WHITE, relational_marker: str = "") -> None:
        self.value = value  
        self.position = position  
        self.color = color        
        self.relational_marker = relational_marker 
    def __str__(self):
        return f"c[{self.value}]({self.position})"

class MicroConfiguration:
    def __init__(self, r0: RelationalNucleus, components: List[DependentComponent]):
        self.r0 = r0
        self.components = components
    def get_surface_form(self) -> str:
        prefixes = "".join([c.value for c in self.components if c.position == "prefix"])
        infixes = "".join([c.value for c in self.components if c.position == "infix"])
        suffixes = "".join([c.value for c in self.components if c.position == "suffix"])
        return f"{prefixes}{self.r0.value}{infixes}{suffixes}"
    def get_chromatic_form(self) -> str:
        prefixes = "".join([f"{c.color}{c.value}" for c in self.components if c.position == "prefix"])
        infixes = "".join([f"{c.color}{c.value}" for c in self.components if c.position == "infix"])
        suffixes = "".join([f"{c.color}{c.value}" for c in self.components if c.position == "suffix"])
        return f"{prefixes}{Fore.WHITE}{self.r0.value}{infixes}{suffixes}{Style.RESET_ALL}"

class DeltaArchitecture:
    @staticmethod
    def diagnostic_r0(c1_r0: RelationalNucleus, target_r0_value: str) -> bool:
        return c1_r0.value == target_r0_value

    @staticmethod
    def directional_regime(c1: MicroConfiguration, c2: MicroConfiguration) -> None:
        print(f"{Fore.CYAN}=== 1. REGIM DIRECȚIONAL \Delta(->) ==={Style.RESET_ALL}")
        print(f"Relație de corespondență orientată: {c1.get_chromatic_form()} ---> {c2.get_chromatic_form()}\n")

    @staticmethod
    def additive_regime(c1: MicroConfiguration, new_c: DependentComponent) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 2. REGIM ADITIV \Delta(+) ==={Style.RESET_ALL}")
        updated_components = c1.components + [new_c]
        c2 = MicroConfiguration(c1.r0, updated_components)
        print(f"Formă inițială 1C: {c1.get_chromatic_form()}")
        print(f"Rezultat stabilizat 2C: {c2.get_chromatic_form()}\n")
        return c2

    @staticmethod
    def semantic_redistribution_regime(c_dep: DependentComponent, c_base: MicroConfiguration, semantic_effect: str) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 3. REDISTRIBUIRE SEMANTICĂ \Delta(><) ==={Style.RESET_ALL}")
        updated_components = [c_dep] + c_base.components
        c2 = MicroConfiguration(c_base.r0, updated_components)
        print(f"Bază lexicală C1: {c_base.get_chromatic_form()}")
        print(f"Configurație rezultată B: {c2.get_chromatic_form()}\n")
        return c2

    @staticmethod
    def substitutional_regime(c1: MicroConfiguration, eliminate_val: str, introduce_c: DependentComponent) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 4. REGIM SUBSTITUȚIONAL \Delta(-/+) ==={Style.RESET_ALL}")
        updated_components = [c for c in c1.components if c.value != eliminate_val] + [introduce_c]
        c2 = MicroConfiguration(c1.r0, updated_components)
        print(f"Formă inițială 1C: {c1.get_chromatic_form()}")
        print(f"Rezultat stabilizat 2C: {c2.get_chromatic_form()}\n")
        return c2

    @staticmethod
    def relational_coupling_regime(c_rel: DependentComponent, c_base: MicroConfiguration) -> str:
        print(f"{Fore.CYAN}=== 5. CUPLARE RELAȚIONALĂ \Delta(>/<) ==={Style.RESET_ALL}")
        result_syntagm = f"{c_rel.color}{c_rel.value}{Style.RESET_ALL} / {c_base.get_chromatic_form()}"
        print(f"Sintagmă unificată relațional: {result_syntagm}\n")
        return result_syntagm

    @staticmethod
    def reductive_regime(c1: MicroConfiguration, eliminate_val: str) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 6. REGIM REDUCTIV \Delta(-) ==={Style.RESET_ALL}")
        updated_components = [c for c in c1.components if c.value != eliminate_val]
        c2 = MicroConfiguration(c1.r0, updated_components)
        print(f"Formă inițială 1C: {c1.get_chromatic_form()}")
        print(f"Rezultat redus 2C: {c2.get_chromatic_form()}\n")
        return c2

    @staticmethod
    def positional_reorganization_regime(c1: MicroConfiguration) -> MicroConfiguration:
        print(f"{Fore.CYAN}=== 7. REORGANIZARE POZIȚIONALĂ \Delta(~) ==={Style.RESET_ALL}")
        reorganized_components = list(reversed(c1.components))
        c2 = MicroConfiguration(c1.r0, reorganized_components)
        print(f"Configurație liniară 1C: {c1.get_chromatic_form()}")
        print(f"Configurație reorganizată 2C: {c2.get_chromatic_form()}\n")
        return c2

    @staticmethod
    def cumulative_paradigmatic_regime(r0: RelationalNucleus, paradigms: List[Tuple[str, str]]) -> None:
        print(f"{Fore.CYAN}=== 8. FLEXIBILITATE PARADIGMATICĂ CUMULATIVĂ \Delta(\pm) ==={Style.RESET_ALL}")
        for index, (ending, grammatical_person) in enumerate(paradigms, 1):
            comp = DependentComponent(ending, position="suffix", color=Fore.YELLOW)
            config = MicroConfiguration(r0, [comp])
            print(f"  Forma A{index} [{grammatical_person}]: {config.get_chromatic_form()}")

if __name__ == "__main__":
    print(f"{Fore.GREEN}INIȚIALIZARE EXECUȚIE MATRICE OPERATORIALĂ DELTA\n{Style.RESET_ALL}")
    r0_zi = RelationalNucleus("zi")
    r0_merg = RelationalNucleus("merg")
    r0_trust = RelationalNucleus("trust")
    r0_cas = RelationalNucleus("cas")
    r0_andras = RelationalNucleus("άντρας")
    r0_gelada = RelationalNucleus("γελάδα")
    r0_la = RelationalNucleus("la")
    r0_graf = RelationalNucleus("γράφ")

    c1_zi = MicroConfiguration(r0_zi, [])
    c2_zile = MicroConfiguration(r0_zi, [DependentComponent("le", "suffix", Fore.BLUE)])
    DeltaArchitecture.directional_regime(c1_zi, c2_zile)

    c1_merg = MicroConfiguration(r0_merg, [])
    suffix_eam = DependentComponent("eam", "suffix", Fore.GREEN)
    DeltaArchitecture.additive_regime(c1_merg, suffix_eam)

    c1_trust = MicroConfiguration(r0_trust, [])
    prefix_dis = DependentComponent("dis", "prefix", Fore.MAGENTA)
    DeltaArchitecture.semantic_redistribution_regime(prefix_dis, c1_trust, "Antonymy / Negation")

    c1_casa = MicroConfiguration(r0_cas, [DependentComponent("ă", "suffix", Fore.RED)])
    suffix_e = DependentComponent("e", "suffix", Fore.GREEN)
    DeltaArchitecture.substitutional_regime(c1_casa, "ă", suffix_e)

    c1_andras = MicroConfiguration(r0_andras, [])
    article_o = DependentComponent("ο", "prefix", Fore.CYAN, relational_marker="'")
    DeltaArchitecture.relational_coupling_regime(article_o, c1_andras)

    c1_gelada = MicroConfiguration(r0_gelada, [DependentComponent("α", "prefix", Fore.RED)])
    DeltaArchitecture.reconstructive_regime = DeltaArchitecture.reductive_regime(c1_gelada, "α")

    c1_la = MicroConfiguration(r0_la, [DependentComponent("l", "prefix", Fore.YELLOW), DependentComponent("a", "infix", Fore.YELLOW)])
    c1_la.r0.value = "" 
    DeltaArchitecture.positional_reorganization_regime(c1_la)

    greek_paradigm = [("ω", "Pers. 1 SG"), ("εις", "Pers. 2 SG"), ("ει", "Pers. 3 SG"), ("ουμε", "Pers. 1 PL"), ("ετε", "Pers. 2 PL"), ("ουν", "Pers. 3 PL")]
    DeltaArchitecture.cumulative_paradigmatic_regime(r0_graf, greek_paradigm)