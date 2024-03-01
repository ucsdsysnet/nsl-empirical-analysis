import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt

colors = plt.cm.get_cmap('hsv', 50)

csv_google = pd.read_csv('../../data/extracted/nsl_letters_google.csv')
csv_apple = pd.read_csv('../../data/extracted/nsl_letters_apple.csv')
csv_nslarchive = pd.read_csv('../../data/extracted/nsl_letters_nslarchive.csv')
csv = pd.concat([csv_google, csv_apple, csv_nslarchive])

# earllier date when the letter is served
csv['date_let'] = date_let = [datetime.strptime(val, "%Y-%m-%d") for val in csv['issue date'].values]

# later date when the letter is published
csv['date_pub'] = date_pub = [datetime.strptime(val, "%Y-%m-%d") for val in csv[' release date'].values]

gag_time = [(date_pub[i] - date_let[i]).days for i in range(len(date_pub))]

date_let_zip_gag_time = zip(date_let, gag_time)
date_let_zip_gag_time_s = sorted(date_let_zip_gag_time, key=lambda x: x[0])
date_let_s, gag_time_s = zip(*date_let_zip_gag_time_s)
gag_time_s = [float(ss) for ss in gag_time_s]

g_t_o_t = pd.DataFrame({'date_let' : date_let_s, 'gag_time' : gag_time_s}, columns=['date_let', 'gag_time'])

g_t_o_t__year = g_t_o_t.groupby(g_t_o_t.date_let.dt.year).mean()
g_t_o_t__year_min = g_t_o_t.groupby(g_t_o_t.date_let.dt.year).min()
g_t_o_t__year_max = g_t_o_t.groupby(g_t_o_t.date_let.dt.year).max()



plt.rc("axes", axisbelow=True)
plt.rcParams["font.size"] = 24
plt.rcParams["mathtext.default"] = "regular"
plt.rcParams["figure.figsize"] = (14,8)
#colors1 = ["#B0EFEF", "#FEFFBF", "#F498C2"]
#colors2 = ["#83D9DC", "#FCDCDF", "#C997C6"]

plt.figure()

plt.grid(True, which="major")
plt.grid(True, which="minor")
#plt.minorticks_on()
plt.tight_layout()
plt.ticklabel_format(style='plain')
plt.errorbar([datetime(v, 6, 1) for v in g_t_o_t__year.index.values], g_t_o_t__year['gag_time' ].values.tolist(),
   yerr =  (np.array(g_t_o_t__year['gag_time' ].values.tolist()) - np.array(g_t_o_t__year_min['gag_time' ].values.tolist()),
            np.array(g_t_o_t__year_max['gag_time' ].values.tolist()) - np.array(g_t_o_t__year['gag_time' ].values.tolist())),
   linestyle='dotted', marker='o', label="Gag order time (min, avg, max yearly)", color="#56b4e9", fmt='o', elinewidth=3, linewidth=3)
plt.legend()
plt.grid(axis="y")
#plt.ticklabel_format(axis='both', style='sci', scilimits=(4,4))                                                                                                                                                                             
plt.xlabel(None)
plt.ylabel(None)
plt.legend()
plt.tight_layout()
plt.savefig(f"../../data/processed/mean_gag_time_over_time_yearly_date_let__errorbar.pdf")
plt.savefig(f"../../data/processed/mean_gag_time_over_time_yearly_date_let__errorbar.png")