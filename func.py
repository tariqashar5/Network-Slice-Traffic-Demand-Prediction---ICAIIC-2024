import random
import numpy as np
import pandas as pd

def random_sum_to(n, num_terms = None):
    num_terms = (num_terms or random.randint(2, n)) - 1
    a = random.sample(range(1, n), num_terms) + [0, n]
    list.sort(a)
    return [a[i+1] - a[i] for i in range(len(a) - 1)]


# smart_transport = random_sum_to(3696,2016)
# safety = random_sum_to(3696,2016)
# industry = random_sum_to(7392,2016)
# ar_vr_gaming = random_sum_to(6720,2016)
# smartphone = random_sum_to(16800,2016)

# np.savetxt("traffic.csv", np.c_[smart_transport,safety,
#                                     industry,ar_vr_gaming,
#                                     smartphone], fmt='%d', delimiter = ',')



# df = pd.DataFrame(
#         {'Hours': pd.date_range('01/01/2018', '01/01/2019',  
#                                 freq='1H', inclusive='left')}
#      )
# df.to_csv('time.csv')

service_types_list = ['ar_vr_gaming', 'industry', 'safety', 'smartphone', 'transport']
average_df = []
for i in range (len(service_types_list)):
    service_type = service_types_list[i]
    print(service_type)
    file = 'results/' + service_type + '_output.csv'
    df1 = pd.read_csv(file, encoding='utf-8')
    predicted_data = df1['predicted'].tolist()
    print(predicted_data)
    average = sum(predicted_data) / len(predicted_data)
    print('average: ', average)
    average_df = average_df.append(average)
    # print(average_df)
    # average_df = np.savetxt('results/avg_all_services.csv',np.c_[average_df],  header=[service_types_list])
    # average_df = pd.DataFrame(average, columns=[service_types_list[i]])
    # average_df.to_csv('avg_all_services.csv', columns=[service_type])