# market_data_helper.py
import json

Test = 1
if Test == 1:
    
    market_data = ['']
else:
    # MULTIFAMILY DATA
    print("\n--------------------\n--------------------\nMULTI FAMILY \n")
    mf_inventory_units = input('Inventory Units: ')
    mf_under_construction = input('Under Constr Units: ')
    mf_12_mo_absorp_units = input('12 Mo Absorp Units: ')
    mf_vacancy_rate = input('Vacancy Rate: ')
    mf_market_asking_rent_unit = input('Market Askin Rent/Unit: ')
    mf_market_annual_rent_growth = input('Annual Rent Growth: ')
    mf_market_sale_price_unit = input('Market Sale Price/Unit: ')
    mf_12_mo_sales_vol = input('12 Mo Sales Vol: ')
    mf_data = {
        "id": "1",
        "productType": "Multi-Family",
        "col1": "Inventory Units",
        "col1data": mf_inventory_units,
        "col2": "Under Constr Units",
        "col2data": mf_under_construction,
        "col3": "12 Mo Absorp Units",
        "col3data": mf_12_mo_absorp_units,
        "col4": "Vacancy Rate",
        "col4data": mf_vacancy_rate+'%',
        "col5": "Market Askin Rent/Unit",
        "col5data": '$'+mf_market_asking_rent_unit,
        "col6": "Annual Rent Growth",
        "col6data": mf_market_annual_rent_growth+'%',
        "col7": "Market Sale Price/Unit",
        "col7data": '$'+mf_market_sale_price_unit,
        "col8": "12 Mo Sales Vol",
        "col8data": '$'+mf_12_mo_sales_vol
    }
    # OFFICE DATA
    print("\n--------------------\n--------------------\nOffice \n")
    of_col1 = input("Inventory SF: ")
    of_col2 = input("Under Constr SF: ")
    of_col3 = input("12 Mo Net Absorp SF: ")
    of_col4 = input("Vacancy Rate: ")
    of_col5 = input("Market Rent/SF: ")
    of_col6 = input("Annual Rent Growth: ")
    of_col7 = input("Market Sale Price/SF: ")
    of_col8 = input("12 Mo Sales Vol: ")
    of_data = {
        "id": "2",
        "productType": "Office",
        "col1": "Inventory SF", "col1data": of_col1,
        "col2": "Under Constr SF", "col2data": of_col2,
        "col3": "12 Mo Net Absorp SF", "col3data": of_col3,
        "col4": "Vacancy Rate", "col4data": of_col4+'%',
        "col5": "Market Rent/SF", "col5data": '$'+of_col5,
        "col6": "Annual Rent Growth", "col6data": of_col6+'%',
        "col7": "Market Sale Price/SF", "col7data": '$'+of_col7,
        "col8": "12 Mo Sales Vol", "col8data": '$'+of_col8
    }
    # RETAIL DATA
    print("\n--------------------\n--------------------\nRetail \n")
    ret_col1 = input("Inventory SF: ")
    ret_col2 = input("Under Constr SF: ")
    ret_col3 = input("12 Mo Net Absorp SF: ")
    ret_col4 = input("Vacancy Rate: ")
    ret_col5 = input("arket Rent/SF: ")
    ret_col6 = input("Annual Rent Growth: ")
    ret_col7 = input("Market Sale Price/SF: ")
    ret_col8 = input("12 Mo Sales Vol: ")
    ret_data = {
        "id": "3",
        "productType": "Retail",
        "col1": "Inventory SF", "col1data": ret_col1,
        "col2": "Under Constr SF", "col2data": ret_col2,
        "col3": "12 Mo Net Absorp SF", "col3data": ret_col3,
        "col4": "Vacancy Rate", "col4data": ret_col4+'%',
        "col5": "Market Rent/SF", "col5data": '$'+ret_col5,
        "col6": "Annual Rent Growth", "col6data": ret_col6+'%',
        "col7": "Market Sale Price/SF", "col7data": '$'+ret_col7,
        "col8": "12 Mo Sales Vol", "col8data": '$'+ret_col8
    }

    # INDUSTRIAL DATA
    print("\n--------------------\n--------------------\Industrial \n")
    ind_col1 = input("Inventory SF: ")
    ind_col2 = input("Under Constr SF: ")
    ind_col3 = input("12 Mo Net Absorp SF: ")
    ind_col4 = input("Vacancy Rate: ")
    ind_col5 = input("Market Rent/SF: ")
    ind_col6 = input("Annual Rent Growth: ")
    ind_col7 = input("Market Sale Price/SF: ")
    ind_col8 = input("12 Mo Sales Vol: ")
    ind_data = {
        "id": "4",
        "productType": "Industrial",
        "col1": "Inventory SF", "col1data": ind_col1+'',
        "col2": "Under Constr SF", "col2data": ind_col2,
        "col3": "12 Mo Net Absorp SF", "col3data": ind_col3,
        "col4": "Vacancy Rate", "col4data": ind_col4+'%',
        "col5": "Market Rent/SF", "col5data": '$'+ind_col5,
        "col6": "Annual Rent Growth", "col6data": ind_col6,
        "col7": "Market Sale Price/SF", "col7data": '$'+ind_col7,
        "col8": "12 Mo Sales Vol", "col8data": '$'+ind_col8
    }
    market_data = [mf_data, of_data, ret_data, ind_data]

with open('marketData.js','w') as outfile:
    outfile.write('const marketData =\n')
    json.dump(market_data, outfile)
    outfile.write('\nmodule.exports = marketData')