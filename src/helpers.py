def create_route_column(df):
    df = df.copy()
    df["ROUTE"] = df["ORIGIN"] + "-" + df["DEST"]
    return df