def generate_business_recommendations(df, date_col, product_col, sales_col):
    
    insights = []

    # Trend
    if df[sales_col].iloc[-1] > df[sales_col].iloc[0]:
        insights.append("📈 Sales are increasing. Consider expanding inventory.")
    else:
        insights.append("📉 Sales are decreasing. Focus on promotions or discounts.")

    # Peak day
    df['day'] = df[date_col].dt.day_name()
    peak_day = df.groupby('day')[sales_col].sum().idxmax()
    insights.append(f"🔥 Peak sales occur on {peak_day}. Increase stock before this day.")

    # Best & worst products
    best_product = df.groupby(product_col)[sales_col].sum().idxmax()
    worst_product = df.groupby(product_col)[sales_col].sum().idxmin()

    insights.append(f"🏆 '{best_product}' is your best-selling product. Promote it more.")
    insights.append(f"⚠️ '{worst_product}' is underperforming. Consider discounts or replacement.")

    # Average sales
    avg_sales = df[sales_col].mean()
    insights.append(f"📊 Average sales: {round(avg_sales,2)}")

    return insights