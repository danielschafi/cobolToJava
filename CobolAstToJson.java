import io.proleap.cobol.CobolLexer;
import io.proleap.cobol.CobolParser;
import io.proleap.cobol.CobolParser.StartRuleContext;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CobolAstToJson {
    
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java CobolAstToJson <cobol-file-path>");
            System.exit(1);
        }
        
        String filePath = args[0];
        
        try {
            // Read the COBOL file
            String cobolCode = new String(Files.readAllBytes(Paths.get(filePath)));
            
            // Create lexer and parser
            ANTLRInputStream input = new ANTLRInputStream(cobolCode);
            CobolLexer lexer = new CobolLexer(input);
            CommonTokenStream tokens = new CommonTokenStream(lexer);
            CobolParser parser = new CobolParser(tokens);
            
            // Parse starting from the root rule
            StartRuleContext tree = parser.startRule();
            
            // Convert AST to JSON
            Map<String, Object> astJson = parseTreeToJson(tree);
            
            // Output JSON
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            System.out.println(gson.toJson(astJson));
            
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            System.exit(1);
        } catch (Exception e) {
            System.err.println("Error parsing COBOL file: " + e.getMessage());
            System.exit(1);
        }
    }
    
    private static Map<String, Object> parseTreeToJson(ParseTree tree) {
        Map<String, Object> node = new HashMap<>();
        
        if (tree instanceof TerminalNode) {
            // Terminal node (leaf)
            TerminalNode terminal = (TerminalNode) tree;
            node.put("type", "terminal");
            node.put("text", terminal.getText());
            node.put("symbol", terminal.getSymbol().getType());
        } else {
            // Rule node (internal node)
            RuleContext ruleContext = (RuleContext) tree;
            String ruleName = CobolParser.ruleNames[ruleContext.getRuleIndex()];
            
            node.put("type", "rule");
            node.put("rule", ruleName);
            node.put("text", tree.getText());
            
            // Add children
            List<Map<String, Object>> children = new ArrayList<>();
            for (int i = 0; i < tree.getChildCount(); i++) {
                children.add(parseTreeToJson(tree.getChild(i)));
            }
            if (!children.isEmpty()) {
                node.put("children", children);
            }
        }
        
        return node;
    }
}