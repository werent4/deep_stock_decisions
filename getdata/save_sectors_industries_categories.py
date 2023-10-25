import pandas as pd

industries = {
    "Retail": 1,
    "Oil & Gas": 2,
    "Home Furnishings": 3,
    "Transportation Services": 4,
    "Food Chains": 5,
    "Computer Software": 6,
    "Books": 7,
    "Military/Government/Technical": 8,
    "Agricultural Chemicals": 9,
    "Electric Utilities": 10,
    "Banks": 11,
    "Other Metals and Minerals": 12,
    "Shoe Manufacturing": 13,
    "Consumer Specialties": 14,
    "Services-Misc. Amusement & Recreation": 15,
    "Medical Specialties": 16,
    "Natural Gas Distribution": 17,
    "Hotels/Resorts": 18,
    "Auto & Home Supply Stores": 19,
    "Packaged Foods": 20,
    "Paper": 21,
    "Consumer Electronics/Appliances": 22,
    "Environmental Services": 23,
    "Electrical Products": 24,
    "Real Estate Investment Trusts": 25,
    "Water Supply": 26,
    "Rental/Leasing Companies": 27,
    "Investment Bankers/Brokers/Service": 28,
    "Integrated Oil Companies": 29,
    "Textiles": 30,
    "Automotive Aftermarket": 31,
    "Electronics Distribution": 32,
    "Hospital/Nursing Management": 33,
    "Package Goods/Cosmetics": 34,
    "Forest Products": 35,
    "Marine Transportation": 36,
    "Meat/Poultry/Fish": 37,
    "General Building Contractors": 38,
    "Ophthalmic Goods": 39,
    "Farming/Seeds/Milling": 40,
    "Professional and Commercial Equipment": 41,
    "Medicinal Chemicals and Botanical Products": 42,
    "Advertising": 43,
    "Movies/Entertainment": 44,
    "Specialty Insurers": 45,
    "Engineering & Construction": 46,
    "Trusts Except Educational Religious and Charitable": 47,
    "Savings Institutions": 48,
    "Electronic Components": 49,
    "Broadcasting": 50,
    "Metal Fabrications": 51,
    "Tools/Hardware": 52,
    "Water Sewer Pipeline Comm & Power Line Construction": 53,
    "Major Chemicals": 54,
    "Beverages": 55,
    "Biotechnology": 56,
    "Radio And Television Broadcasting And Communications Equipment": 57,
    "Precision Instruments": 58,
    "Investment Managers": 59,
    "Misc Health and Biotechnology Services": 60,
    "Durable Goods": 61,
    "Homebuilding": 62,
    "Mining & Quarrying of Nonmetallic Minerals": 63,
    "Property-Casualty Insurers": 64,
    "Educational Services": 65,
    "Specialty Chemicals": 66,
    "Catalog/Specialty Distribution": 67,
    "Coal Mining": 68,
    "Miscellaneous Manufacturing Industries": 69,
    "Finance: Consumer Services": 70,
    "Commercial Banks": 71,
    "Newspapers/Magazines": 72,
    "Medical/Dental Instruments": 73,
    "Semiconductors": 74,
    "Plastic Products": 75,
    "Pollution Control Equipment": 76,
    "Aluminum": 77,
    "Clothing/Shoe/Accessory Stores": 78,
    "Metal Mining": 79,
    "Life Insurance": 80,
    "Restaurants": 81,
    "Computer Software: Prepackaged Software": 82,
    "Motor Vehicles": 83,
    "Auto Parts": 84,
    "Consumer Electronics/Video Chains": 85,
    "Biotechnology: Pharmaceutical Preparations": 86,
    "Industrial Specialties": 87,
    "Containers/Packaging": 88,
    "Telecommunications Equipment": 89,
    "Multi-Sector Companies": 90,
    "Medical/Nursing Services": 91,
    "Office Equipment/Supplies/Services": 92,
    "Pharmaceuticals and Biotechnology": 93,
    "Wholesale Distributors": 94,
    "Building Operators": 95,
    "Publishing": 96,
    "Construction/Ag Equipment/Trucks": 97,
    "Biotechnology: Biological Products": 98,
    "Accident & Health Insurance": 99,
    "Finance/Investors Services": 100,
    "Building Products": 101,
    "Other Consumer Services": 102,
    "Diversified Electronic Products": 103,
    "Apparel": 104,
    "Food Distributors": 105,
    "Building Materials": 106,
    "Industrial Machinery/Components": 107,
    "Finance Companies": 108,
    "Specialty Foods": 109,
    "Biotechnology: In Vitro & In Vivo Diagnostic Substances": 110,
    "Diversified Commercial Services": 111,
    "Oil/Gas Transmission": 112,
    "Medical Electronics": 113,
    "Ordnance And Accessories": 114,
    "Precious Metals": 115,
    "Aerospace": 116,
    "Professional Services": 117,
    "Biotechnology: Electromedical & Electrotherapeutic Apparatus": 118,
    "Department/Specialty Retail Stores": 119,
    "Computer Communications Equipment": 120,
    "Other Pharmaceuticals": 121,
    "Assisted Living Services": 122,
    "Recreational Games/Products/Toys": 123,
    "Air Freight/Delivery Services": 124,
    "Cable & Other Pay Television Services": 125,
    "Computer Peripheral Equipment": 126,
    "Paints/Coatings": 127,
    "Oilfield Services/Equipment": 128,
    "Blank Checks": 129,
    "Managed Health Care": 130,
    "Business Services": 131,
    "Tobacco": 132,
    "Auto Manufacturing": 133,
    "EDP Services": 134,
    "Railroads": 135,
    "Power Generation": 136,
    "Steel/Iron Ore": 137,
    "Retail: Building Materials": 138,
    "Biotechnology: Laboratory Analytical Instruments": 139,
    "Other Specialty Stores": 140,
    "Oil Refining/Marketing": 141,
    "Fluid Controls": 142
}
sectors = {
    'Utilities': 1,
    'Basic Materials': 2,
    'Health Care': 3,
    'Real Estate': 4,
    'Industrials': 5,
    'Consumer Staples': 6,
    'Energy': 7,
    'Technology': 8,
    'Finance': 9,
    'Telecommunications': 10,
    'Consumer Discretionary': 11,
    'Miscellaneous': 12
}

def process_field_dict(dic):
    """Firstly name, then id in dic.
    For example, "Oil & Gas": 2, "Oil & Gas" - name, 2 - id"""
    name_temp = []
    id_temp = []
    for key, value in dic.items():
        name_temp.append(key)
        id_temp.append(value)

    temp_df = pd.DataFrame({'name': name_temp, 'id': id_temp})
    return temp_df
temp_df = process_field_dict(industries)
temp_df.to_csv('com_names\\industries.csv')