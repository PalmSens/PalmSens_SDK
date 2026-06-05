# Generated from MethodScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MethodScriptParser import MethodScriptParser
else:
    from MethodScriptParser import MethodScriptParser

# This class defines a complete generic visitor for a parse tree produced by MethodScriptParser.

class MethodScriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MethodScriptParser#sourceFile.
    def visitSourceFile(self, ctx:MethodScriptParser.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#statement.
    def visitStatement(self, ctx:MethodScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#commentLine.
    def visitCommentLine(self, ctx:MethodScriptParser.CommentLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MethodScriptParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:MethodScriptParser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#stringDeclaration.
    def visitStringDeclaration(self, ctx:MethodScriptParser.StringDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#ifStatement.
    def visitIfStatement(self, ctx:MethodScriptParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#elseifClause.
    def visitElseifClause(self, ctx:MethodScriptParser.ElseifClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#elseClause.
    def visitElseClause(self, ctx:MethodScriptParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#loopStatement.
    def visitLoopStatement(self, ctx:MethodScriptParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:MethodScriptParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#tag.
    def visitTag(self, ctx:MethodScriptParser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:MethodScriptParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#operator.
    def visitOperator(self, ctx:MethodScriptParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#operand.
    def visitOperand(self, ctx:MethodScriptParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#arrayAccess.
    def visitArrayAccess(self, ctx:MethodScriptParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#commandCall.
    def visitCommandCall(self, ctx:MethodScriptParser.CommandCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#simpleCommand.
    def visitSimpleCommand(self, ctx:MethodScriptParser.SimpleCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#measurementLoop.
    def visitMeasurementLoop(self, ctx:MethodScriptParser.MeasurementLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#optionalArgumentBlock.
    def visitOptionalArgumentBlock(self, ctx:MethodScriptParser.OptionalArgumentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#measurementCommand.
    def visitMeasurementCommand(self, ctx:MethodScriptParser.MeasurementCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#commandName.
    def visitCommandName(self, ctx:MethodScriptParser.CommandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#argument.
    def visitArgument(self, ctx:MethodScriptParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#literal.
    def visitLiteral(self, ctx:MethodScriptParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#fstringLiteral.
    def visitFstringLiteral(self, ctx:MethodScriptParser.FstringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#fstringContent.
    def visitFstringContent(self, ctx:MethodScriptParser.FstringContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MethodScriptParser#fstringInterpolation.
    def visitFstringInterpolation(self, ctx:MethodScriptParser.FstringInterpolationContext):
        return self.visitChildren(ctx)



del MethodScriptParser