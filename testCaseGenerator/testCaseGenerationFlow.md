The cobol snippets in the dataset are incomplete

example

```
TIME-RTN.                                                        
      *    ***<<   時間処理    >>***                            
           DISPLAY 'ENTER TIME: '.                                     
           ACCEPT  WK-INPUT-TIME.                                     
           UNSTRING WK-INPUT-TIME DELIMITED BY ':'                    
           INTO WK-HH, WK-MM, WK-SS.                                  
      *    ***<<   時間の編集    >>***                              
           IF  WK-HH < 10                                             
               MOVE '0' TO WK-HH-FORMATTED                            
               MOVE WK-HH TO WK-HH-FORMATTED(2:2).                    
           ELSE                                                       
               MOVE WK-HH TO WK-HH-FORMATTED.                         
           END-IF.                                                    
           IF  WK-MM < 10                                             
               MOVE '0' TO WK-MM-FORMATTED                            
               MOVE WK-MM TO WK-MM-FORMATTED(2:2).                    
           ELSE                                                       
               MOVE WK-MM TO WK-MM-FORMATTED.                         
           END-IF.                                                    
           IF  WK-SS < 10                                             
               MOVE '0' TO WK-SS-FORMATTED                            
               MOVE WK-SS TO WK-SS-FORMATTED(2:2).                    
           ELSE                                                       
               MOVE WK-SS TO WK-SS-FORMATTED.                         
           END-IF.                                                    
           STRING WK-HH-FORMATTED, WK-MM-FORMATTED, WK-SS-FORMATTED    
           DELIMITED BY ':' INTO WK-TIME-FORMATTED.                   
       
TIME-RTN-X.

```