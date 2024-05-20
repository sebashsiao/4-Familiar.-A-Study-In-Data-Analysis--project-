import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

vein_pack_lifespans = familiar.lifespans(package='vein')
# print(vein_pack_lifespans)
artery_pack_lifespans = familiar.lifespans(package='artery')
# print(artery_pack_lifespans)

# compara vein_pack_lifespans to the average life expectancy 71
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)    # evaluate p-value with 1 Sample T-Test
# print(vein_pack_test)

# print messages according to the p-value result.    # Threshold set to 5%
if vein_pack_test[1] < 0.05:
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

# analyze the difference between the two suscriptions vein_pack_lifespans and artery_pack_lifespans
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)    # evaluate p-value with 2 Sample T-Test
# print(package_comparison_results)

# print messages according to the p-value result.    # Threshold set to 5%
if package_comparison_results[1] < 0.05:
  print("The Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")

# import contingency data
iron_contingency_table = familiar.iron_counts_for_package()
# print(iron_contingency_table)

# Chi-Squared Test, iron contingency table
chi2_tstat, iron_pvalue, dof, expected_freq = chi2_contingency(iron_contingency_table)
# print(iron_pvalue)

# print messages according to the p-value result.    # Threshold set to 5%
if vein_pack_test[1] < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
