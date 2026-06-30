# Generated from MethodScriptParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MethodScriptParser import MethodScriptParser
else:
    from MethodScriptParser import MethodScriptParser

# This class defines a complete listener for a parse tree produced by MethodScriptParser.
class MethodScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by MethodScriptParser#sourceFile.
    def enterSourceFile(self, ctx:MethodScriptParser.SourceFileContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#sourceFile.
    def exitSourceFile(self, ctx:MethodScriptParser.SourceFileContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#statement.
    def enterStatement(self, ctx:MethodScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#statement.
    def exitStatement(self, ctx:MethodScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#commentLine.
    def enterCommentLine(self, ctx:MethodScriptParser.CommentLineContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#commentLine.
    def exitCommentLine(self, ctx:MethodScriptParser.CommentLineContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:MethodScriptParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:MethodScriptParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#arrayDeclaration.
    def enterArrayDeclaration(self, ctx:MethodScriptParser.ArrayDeclarationContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#arrayDeclaration.
    def exitArrayDeclaration(self, ctx:MethodScriptParser.ArrayDeclarationContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#stringDeclaration.
    def enterStringDeclaration(self, ctx:MethodScriptParser.StringDeclarationContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#stringDeclaration.
    def exitStringDeclaration(self, ctx:MethodScriptParser.StringDeclarationContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#ifStatement.
    def enterIfStatement(self, ctx:MethodScriptParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#ifStatement.
    def exitIfStatement(self, ctx:MethodScriptParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#elseifClause.
    def enterElseifClause(self, ctx:MethodScriptParser.ElseifClauseContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#elseifClause.
    def exitElseifClause(self, ctx:MethodScriptParser.ElseifClauseContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#elseClause.
    def enterElseClause(self, ctx:MethodScriptParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#elseClause.
    def exitElseClause(self, ctx:MethodScriptParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#loopStatement.
    def enterLoopStatement(self, ctx:MethodScriptParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#loopStatement.
    def exitLoopStatement(self, ctx:MethodScriptParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#breakStatement.
    def enterBreakStatement(self, ctx:MethodScriptParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#breakStatement.
    def exitBreakStatement(self, ctx:MethodScriptParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#tag.
    def enterTag(self, ctx:MethodScriptParser.TagContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#tag.
    def exitTag(self, ctx:MethodScriptParser.TagContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:MethodScriptParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:MethodScriptParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#operator.
    def enterOperator(self, ctx:MethodScriptParser.OperatorContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#operator.
    def exitOperator(self, ctx:MethodScriptParser.OperatorContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#operand.
    def enterOperand(self, ctx:MethodScriptParser.OperandContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#operand.
    def exitOperand(self, ctx:MethodScriptParser.OperandContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#arrayAccess.
    def enterArrayAccess(self, ctx:MethodScriptParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#arrayAccess.
    def exitArrayAccess(self, ctx:MethodScriptParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#commandCall.
    def enterCommandCall(self, ctx:MethodScriptParser.CommandCallContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#commandCall.
    def exitCommandCall(self, ctx:MethodScriptParser.CommandCallContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#simpleCommand.
    def enterSimpleCommand(self, ctx:MethodScriptParser.SimpleCommandContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#simpleCommand.
    def exitSimpleCommand(self, ctx:MethodScriptParser.SimpleCommandContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#measurementLoop.
    def enterMeasurementLoop(self, ctx:MethodScriptParser.MeasurementLoopContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#measurementLoop.
    def exitMeasurementLoop(self, ctx:MethodScriptParser.MeasurementLoopContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#optionalArgumentBlock.
    def enterOptionalArgumentBlock(self, ctx:MethodScriptParser.OptionalArgumentBlockContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#optionalArgumentBlock.
    def exitOptionalArgumentBlock(self, ctx:MethodScriptParser.OptionalArgumentBlockContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#measurementCommand.
    def enterMeasurementCommand(self, ctx:MethodScriptParser.MeasurementCommandContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#measurementCommand.
    def exitMeasurementCommand(self, ctx:MethodScriptParser.MeasurementCommandContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#commandName.
    def enterCommandName(self, ctx:MethodScriptParser.CommandNameContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#commandName.
    def exitCommandName(self, ctx:MethodScriptParser.CommandNameContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#argument.
    def enterArgument(self, ctx:MethodScriptParser.ArgumentContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#argument.
    def exitArgument(self, ctx:MethodScriptParser.ArgumentContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#literal.
    def enterLiteral(self, ctx:MethodScriptParser.LiteralContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#literal.
    def exitLiteral(self, ctx:MethodScriptParser.LiteralContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#fstringLiteral.
    def enterFstringLiteral(self, ctx:MethodScriptParser.FstringLiteralContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#fstringLiteral.
    def exitFstringLiteral(self, ctx:MethodScriptParser.FstringLiteralContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#fstringContent.
    def enterFstringContent(self, ctx:MethodScriptParser.FstringContentContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#fstringContent.
    def exitFstringContent(self, ctx:MethodScriptParser.FstringContentContext):
        pass


    # Enter a parse tree produced by MethodScriptParser#fstringInterpolation.
    def enterFstringInterpolation(self, ctx:MethodScriptParser.FstringInterpolationContext):
        pass

    # Exit a parse tree produced by MethodScriptParser#fstringInterpolation.
    def exitFstringInterpolation(self, ctx:MethodScriptParser.FstringInterpolationContext):
        pass



del MethodScriptParser