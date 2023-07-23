import pandas as pd
import re
import streamlit as st
import numpy as np

### The following is used to store the dataframes between reruns
if 'df2' not in st.session_state:
	st.session_state.df2 = None
if 'kw_data' not in st.session_state:
	st.session_state.kw_data = None

html = f"<img width='250' src='data:image/png;base64,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'/>"
st.markdown(html, unsafe_allow_html=True)
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
	#with st.expander("Show filter lists (with plurals)"):
		#st.write(lists)
	#with st.expander("Show singular lists"):
		#st.write(lists_singular)

	keywords_csv = st.file_uploader("Upload your keywords in csv format:", accept_multiple_files=False, type=['csv'], key="keywords_csv")
	if keywords_csv is not None:
		kw_data = pd.read_csv(keywords_csv, encoding='utf-16', sep='\t', skiprows=2)
		kw_data = kw_data.drop(['Currency', 'Competition', 'Competition (indexed value)', 'Ad impression share', 'Organic impression share', 'Organic average position', 'In account?', 'In plan?'], axis=1)
		kw_data["Singular"] = kw_data["Keyword"].str.rstrip(",s")
		dimens_no = 0
		lists_df = pd.DataFrame(lists)
		for n in col_names:
			kw_data[n] = kw_data["Singular"].str.extract("(" + "|".join(lists_singular[dimens_no]) +")", expand=False)
			#mask = kw_data[n].replace(r'^\s+$', np.nan).astype(bool)
			#st.write(mask)
			#kw_data[n] = lists_df[dimens_no].where(mask, other=temp_kw_data[n])
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
					return kw_data.to_csv(index=False).encode('utf-8')
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
					return df2.to_csv(index=False).encode('utf-8')
				csv = convert_df(df2)
				st.download_button('Download Categories', csv, file_name="1. categories.csv",mime='text/csv')
			except TypeError:
				pass
			except AttributeError:
			    	pass
			except NameError:
				pass
