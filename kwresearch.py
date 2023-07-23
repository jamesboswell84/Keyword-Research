import pandas as pd
import re
import streamlit as st
import numpy as np

### The following is used to store the dataframes between reruns
if 'df2' not in st.session_state:
	st.session_state.df2 = None
if 'kw_data' not in st.session_state:
	st.session_state.kw_data = None

#html = f"<img width='250' src='data:image/png;base64,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'/>"
#st.markdown(html, unsafe_allow_html=True)
st.write("""
	# Keyword Categoriser
	#### Add categories to your Google Keyword Planner keywords.
""")
st.write("""
	[Instructions here](https://github.com/jamesboswell84/Keyword-Research/blob/main/README.md)
""")
st.divider()



## streamlit data_editor test
##st.write("""
##	Paste your KWP categories from clipboard into the below table:
##""")
##if 'df' not in st.session_state:
##	num_cols = 800
##	df = pd.DataFrame()
##	for i in range(num_cols):
##		col_name = f'col{i+1}'
##		df[col_name] = np.random.randint(low=0, high=100, size=1)
##		df[col_name] = df[col_name].astype(str)
##	st.session_state.df = df
##
##if 'df1' not in st.session_state:
##	df1 = st.data_editor(st.session_state.df, key="data_editor", num_rows="dynamic", use_container_width=True)
##	st.session_state.df = df1
##

### Upload your Excel files

categories_csv = st.file_uploader("Upload your categories in csv format:", accept_multiple_files=False, type=['csv'], key="categories_csv")

if categories_csv is not None:
	cat_data = pd.read_csv(categories_csv, header=0)
	df1 = cat_data
	if len(df1) < 20:
		df2 = df1[df1.columns.drop(list(df1.filter(regex=r'^Keywords$|.*\_.*|^Brand$|^Non\-Brands$|.*\..*|^[0-9]*$')))]
		df2 = df2.rename(columns={"Brand or Non-Brand": "Brand"})
		df2 = df2.T.reset_index()
		df2.columns = df2.iloc[0]	
		df2 = df2.drop(df2.index[0])
	else:
		df2 = df1
	st.session_state.df2 = df2		
	col_names = []
	lists = []
	lists_singular = []
	for col in df2:
		col_names.append(col)
		try:
			list = df2[col].dropna()
		except:
			pass
		try:
			list_singular = list.str.rstrip(",s")
		except:
			pass
		try:
			list = list.tolist()
		except:
			pass
		lists.append(list)
		try:
			list_singular = list_singular.tolist()
		except:
			pass
		lists_singular.append(list_singular)
		
	with st.expander("Show category data"):
		st.dataframe(df2)
	with st.expander("Show filter lists (with plurals)"):
		st.write(lists)
	with st.expander("Show singular lists"):
		st.write(lists_singular)

	keywords_csv = st.file_uploader("Upload your keywords in csv format:", accept_multiple_files=False, type=['csv'], key="keywords_csv")
	if keywords_csv is not None:
		kw_data = pd.read_csv(keywords_csv, encoding='utf-16', sep='\t', skiprows=2)
		kw_data["Singular"] = kw_data["Keyword"].str.rstrip(",s")
		dimens_no = 0
		for n in col_names:
			kw_data[n] = kw_data["Singular"].str.extract("(" + "|".join(lists_singular[dimens_no]) +")", expand=False)
			dimens_no = dimens_no + 1
		st.session_state.kw_data = kw_data
		with st.expander("Show keyword data"):
			st.dataframe(kw_data)
		
		### The following prints the output and saves it to csv file
		st.divider()
		kw_data = st.session_state.kw_data
		df2 = st.session_state.df2
		col1, col2 = st.columns(2)
		with col1:
			try:	
				def convert_df(kw_data):
				# IMPORTANT: Cache the conversion to prevent computation on every rerun
					return kw_data.to_csv().encode('utf-8')
				csv = convert_df(kw_data)
				st.download_button('Download Keyword Data', csv, file_name="1. keyword_data.csv",mime='text/csv')
			except TypeError:
				pass
			except AttributeError:
			    	pass
			except NameError:
				pass
		with col2:	
			try:	
				def convert_df(df2):
				# IMPORTANT: Cache the conversion to prevent computation on every rerun
					return df2.to_csv().encode('utf-8')
				csv = convert_df(df2)
				st.download_button('Download Categories', csv, file_name="1. categories.csv",mime='text/csv')
			except TypeError:
				pass
			except AttributeError:
			    	pass
			except NameError:
				pass
