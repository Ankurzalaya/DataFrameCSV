import pandas as pd
import webbrowser


def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table")
    # print(table_id)
    # print(table_html)
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html


if __name__ == "__main__":
    # read the dataframe dataset
    df = pd.read_csv("/home/developer/Downloads/annual.csv")
    # take only first 1000, otherwise it'll generate a large html file
    df = df.iloc[:1001]
    # generate the HTML from the dataframe
    html = generate_html(df)
    # print(html)
    # write the HTML content to an HTML file
    open("home.html", "w").write(html)
    # open the new HTML file with the default browser
    webbrowser.open("home.html")
