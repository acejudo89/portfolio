'set constants to the number of columns you will be consulting in your loop
Const openpricecolumn = 3
Const datecolum = 2
Const closepricecolumn = 6
Const vol_column = 7
Const ticker = 1
Const ticker_result = 9
Const difference_result = 10
Const difference_var = 11
Const Totalstockresult = 12
Const greatest = 14
Const topticker = 15
Const TopValue = 16


Sub stocks()
    'set variables for value storage for total volume, open price, close price,
    'difference from open price and closing price and procentage variacion price
    Dim ws As Worksheet
    For Each ws In Worksheets
    
    Dim totalvol As Double, openprice As Double, closeprice As Double, pricedif As Double, pricevar As Double
        totalvol = 0
   'Set two indexes, i index will help searching data and j index will help to buid the summary table
    Dim RowCount As Long, i As Long, j As Long
    RowCount = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    i = 2
    j = 1
    
    'Set name headers for the summary table
    ws.Cells(j, ticker_result) = "Ticker"
    ws.Cells(j, difference_result) = "Yearly Change"
    ws.Cells(j, difference_var) = "Percent Change"
    ws.Cells(j, Totalstockresult) = "Total Stock Volume"
    
    j = 2
    
    'save your inicial open price for the first tikcer
    
    openprice = ws.Cells(i, openpricecolumn).Value
    
    'created a while loop to register all table values create the summary table explaining
    'the yearly behavior for every ticker
    
        Do While i <= RowCount
                
        'the true condition will compare every row whit the next one for the ticker column, and cumulate the volumen stock
        'Then it will increase the i index to the next row
        
           If ws.Cells(i + 1, ticker).Value = ws.Cells(i, ticker).Value Then
                totalvol = totalvol + ws.Cells(i, vol_column).Value
                i = i + 1
            'The false condition wil summarize the last volume value, get the difference open and close prices and print summary
            
            Else
                totalvol = totalvol + ws.Cells(i, vol_column).Value
                closeprice = ws.Cells(i, closepricecolumn).Value
                ws.Cells(j, ticker_result) = ws.Cells(i, ticker).Value
                ws.Cells(j, difference_result) = closeprice - openprice
               If closeprice - openprice <= 0 Then
                    ws.Cells(j, difference_result).Interior.ColorIndex = 3
                Else
                   ws.Cells(j, difference_result).Interior.ColorIndex = 4
               End If
               ws.Cells(j, difference_var) = (closeprice - openprice) / openprice
               ws.Cells(j, difference_var).Style = "percent"
               ws.Cells(j, Totalstockresult) = totalvol
                
                openprice = ws.Cells(i + 1, openpricecolumn).Value
                totalvol = 0
                i = i + 1
                j = j + 1
                
            End If
         
        Loop
        
'Reset both index, i index will help searching data and j index will help to buid the geatest values table
       
   
   'set haders for the resume table
    
    ws.Range("N2").Value = " Greatest % Increase"
    ws.Range("N3").Value = " Greatest % Decrease"
    ws.Range("N4").Value = " Greatest Total Volume"
    
     'use max, min and match function to find asked values
    increase_number = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("K2:K" & RowCount)), ws.Range("K2:K" & RowCount), 0) + 1
    decrease_number = WorksheetFunction.Match(WorksheetFunction.Min(ws.Range("K2:K" & RowCount)), ws.Range("K2:K" & RowCount), 0) + 1
    increase_volume = WorksheetFunction.Match(WorksheetFunction.Max(ws.Range("L2:L" & RowCount)), ws.Range("L2:L" & RowCount), 0) + 1
    ws.Range("O2") = ws.Cells(increase_number + 1, ticker_result)
    ws.Range("O3") = ws.Cells(decrease_number + 1, ticker_result)
    ws.Range("O4") = ws.Cells(increase_volume + 1, ticker_result)
    ws.Range("p2") = WorksheetFunction.Max(ws.Range("K:K"))
    ws.Range("p3") = WorksheetFunction.Min(ws.Range("K:K"))
    ws.Range("p4") = WorksheetFunction.Max(ws.Range("L:L"))
    ws.Range("p2").Style = "percent"
    ws.Range("p3").Style = "percent"
      
        
 Next ws
 
    
End Sub

