from textx import metamodel_from_str


class SplProjectGenerator:
    def __init__(self, project_description: str):
        self.project_description = project_description

    def generate(self):
        project_metamodel = metamodel_from_str(SPL_PROJECT_GRAMMAR)
        return project_metamodel.model_from_str(self.project_description)


SPL_PROJECT_GRAMMAR = """
/*
  SPL project DSL grammar.
*/

SplProject:
    'project' name=ID
    variants+=Variant
;

Variant:
    'variant' '{'
        'flavor' flavor=ID
        'subsystem' subsystem=ID
        'components' components+=Component
    '}' 
;

Component:
    name=ID
;


// Special rule for comments. Comments start with //
Comment:
    /\/\/.*$/
;
"""
