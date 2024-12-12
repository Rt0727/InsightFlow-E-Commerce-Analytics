def calculate_summary(sales_data):
    total_revenue = sum(item["revenue"] for item in sales_data)
    total_quantity = sum(item["quantity_sold"] for item in sales_data)
    
    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity
    }