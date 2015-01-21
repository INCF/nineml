# from cloner import (ExpandPortDefinition, ExpandAliasDefinition, RenameSymbol,
#                     ClonerVisitor, ClonerVisitorPrefixNamespace)
from queryer import ComponentClassQueryer
from visitors import ComponentClassVisitor, ComponentClassActionVisitor
from .xml import (
    ComponentClassXMLLoader, ComponentClassXMLReader, ComponentClassXMLWriter)
from .interface_inferer import InterfaceInferer