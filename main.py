import ast
import astpretty

sPath = "./file.txt"
with open(sPath) as f:
	sInput = f.read()


node = ast.parse(sInput)
# astpretty.pprint(node)


class CNodeVisitor(ast.NodeVisitor):
	def __init__(self):
		super(CNodeVisitor, self).__init__()
		self.m_str = {}
	
	def visit_Str(self, node):
		self.m_str[node.lineno] = node.s


oVisitor = CNodeVisitor()
oVisitor.visit(node)
print(oVisitor.m_str)
