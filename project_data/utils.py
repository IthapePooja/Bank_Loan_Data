import os
import pickle
import json
import config
import numpy as np


class Bank():
    def __init__(self,age,job,marital,education,default,housing,loan,contact,month,day_of_week,duration,campaign,pdays,previous,poutcome,
                 emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed):

                    self.age       = age                
                    self.job       = job         
                    self.marital   = marital           
                    self.education = education      
                    self.default   =  default              
                    self.housing   =  housing               
                    self.loan      = loan
                    self.contact   =  contact      
                    self.month     =  month             
                    self.day_of_week =  day_of_week            
                    self.duration   =   duration             
                    self.campaign    =   campaign            
                    self.pdays       =   pdays           
                    self.previous    =   previous             
                    self.poutcome    =   poutcome   
                    self.emp_var_rate  =  emp_var_rate  
                    self.cons_price_idx = cons_price_idx        
                    self.cons_conf_idx  =   cons_conf_idx
                    self.euribor3m    = euribor3m
                    self.nr_employed  =nr_employed 

    def load_path(self):
        with open(config.model_path,"rb")as file:
           self.model = pickle.load(file)

        with open(config.json_path,"r")as file:
            self.json = json.load(file)


    def Bank_predict(self):
         self.load_path()
         test_arr = np.zeros(len(self.json['columns']))

         test_arr[0] = self.age
         test_arr[1] = self.json['marital_value'][self.marital]
         test_arr[2] = self.json['default_value'][self.default]
         test_arr[3] = self.json['housing_value'][self.housing]
         test_arr[4] = self.json['loan_value'][self.loan]
         test_arr[5] = self.json['contact_value'][self.contact]
         test_arr[6] = self.json['month_value'][self.month]
         test_arr[7] = self.json['day_of_week_value'][self.day_of_week]
         test_arr[8] = self.duration
         test_arr[9] = self.campaign
         test_arr[10] = self.pdays
         test_arr[11] = self.previous
         test_arr[12] = self.json['poutcome_value'][self.poutcome]
         test_arr[13] = self.emp_var_rate
         test_arr[14] = self.cons_price_idx
         test_arr[15] = self.cons_conf_idx
         test_arr[16] = self.euribor3m
         test_arr[17] = self.nr_employed

         job_index = self.json['columns'].index("job_"+self.job)
         test_arr[job_index] = 1

         education_index = self.json['columns'].index("education_"+self.education)
         test_arr[education_index] = 1

         print("test_array :",test_arr)

         prediction = self.model.predict([test_arr])
         return prediction

