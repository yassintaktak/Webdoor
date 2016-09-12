def table(rows, columns):
    try:
        table_len = len(rows)
        table_columns = []
        table_rows = []
        min_size = 0
        row_padding = "+"
        row_margin = "|"
        column_margin = "|"
        current_column = 0
        for row in rows:
            table_rows.append(row)
        for column in columns:
            table_columns.append(column)
        for table in table_rows:
            if(len(table) > min_size):
                min_size = len(table)
        for column in table_columns:
            if(len(column) > min_size):
                min_size = len(column)
        for _ in range(0, table_len):
            for _ in range(0, min_size):
                row_padding += "-"
            row_padding += "+"
        for row in table_rows:
            if(len(row)%2 != 0):
                row = row+" "
            spaces_count = ((min_size-len(row))/2)
            for _ in range(0, spaces_count):
                row_margin += " "
            row_margin += row
            for _ in range(0, spaces_count):
                row_margin += " "
            row_margin += "|"
        print row_padding
        print row_margin
        print row_padding
        for column in table_columns:
            if(len(column)%2 != 0):
                column = column+" "
            spaces_count = (min_size-len(column))/2
            for _ in range(0, spaces_count):
                column_margin += " "
            column_margin += column
            for _ in range(0, spaces_count):
                column_margin += " "
            column_margin += "|"
            current_column += 1
            if(current_column == table_len):
                print column_margin
                print row_padding
                column_margin = "|"
                current_column = 0

    except Exception as e:
        print "Fail at options.table() : "+str(e)
