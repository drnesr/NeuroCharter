from NeuroCharter import Study
import time
print time.time

Study('DataNT.csv', 'cross validation', num_outputs=4, data_partition=(75, 15),
       tolerance=0.0000001, learning_rate=0.4, maximum_epochs=1000,
       adapt_learning_rate=False, annealing_value=2000,
       display_graph_windows=False, display_graph_pdf=True,
       data_file_has_titles=True, data_file_has_brief_titles=True,
       minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10,
       relative_importance_method="M", validation_epochs=31,
       using_numpy=True, find_activation_function=False)


# # Querying for inputs: Temperature,Relative Humidity, Radiation, Site
# Study(purpose= "advanced query", previous_study_data_file="NrCh_StoredANN_B44H.nsr", start_time=time.time(),
#      input_parameters_suggested_values= ([10, 45, 5], 7.5, (0.5, 0.8), ('A', 'C')))

# Study(purpose= "advanced query", previous_study_data_file="M09n3V.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((1, 2, 4, 8), ('*', ), [30, 330, 60], ('*',), 6.2,
#                                           (0.08, 0.16, 0.24,0.32),
#                                           (0.966, 0.667, 0.333, 0, -0.333 , -0.667, -0.966),
#                                           (.05, .15, .3, .495), (.04, 0.07, .1), (.38, .4, .42)))

# Study(purpose= "advanced query", previous_study_data_file="M09n3V.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((1, 2), 'VGN', [30, 720, 60], 'SND', 6.2,
#                                           (0.085, 0.157, 0.229,0.300, 0.372),
#                                           (0.966, 0.667, 0.333, 0, -0.333 , -0.667, -0.966),
#                                           0.05, (.04, 0.08, .1), (.3, .37, .4)))

# Study(purpose='info', previous_study_data_file="M09n3V.nsr")

# t1 = time.time()
# study1 = Study('dataN.csv', 'full run', num_outputs=4 , tolerance=0.001, learning_rate=0.45, maximum_epochs=500)
# study1.run()
# study2 = Study('dataN.csv', 'validation run', num_outputs=4, data_partition=(60, 25),
#                tolerance=0.0001, learning_rate=0.45, maximum_epochs=500)
# study2.run()
# study3 = Study('dataN.csv', 'optimization', num_outputs=4, data_partition=(60, 25),
#                tolerance=0.001, learning_rate=0.45, maximum_epochs=1000,
#                refresh_weights_after_determining_structure=False, layer_size_range=(0.5, 2, 1),
#                find_activation_function=False, validation_epochs=30, start_time=t1, adapt_learning_rate=True)
# study4 = Study('dataSW2.csv', 'optimization', num_outputs=3, data_partition=(65, 15),
#                tolerance=0.0001, learning_rate=0.3, maximum_epochs=10000,
#                refresh_weights_after_determining_structure=False, layer_size_range=(0.75, 1.25, 1),
#                find_activation_function=False, validation_epochs=30, start_time=t1, adapt_learning_rate=True)

# Study('dataNT.csv', 'validation run', num_outputs=4, data_partition=(65, 15),
#                tolerance=0.001, learning_rate=0.4, maximum_epochs=300,
#                refresh_weights_after_determining_structure=False, layer_size_range=(0.75, 1.25, 1),
#                find_activation_function=False, validation_epochs=30, start_time=t1,
#                adapt_learning_rate=False, annealing_value=2000,
#                display_graph_windows=False, display_graph_pdf=True, categorical_extra_divisor=2,
#                data_file_has_titles=True, data_file_has_brief_titles=True)

# study6 = Study('QueryN.csv', "query", previous_study_data_file="NeuroCharterNet.nsr", start_time=t1)
# from NeuroCharter import *

# Study('dataNT.csv', 'cross validation', num_outputs=4, data_partition=(65, 15),
#       tolerance=0.001, learning_rate=0.4, maximum_epochs=300,
#       adapt_learning_rate=False, annealing_value=2000,
#       display_graph_windows=True, display_graph_pdf=True,
#       data_file_has_titles=True, data_file_has_brief_titles=True)


# Study('TestSW_data.csv', 'cross validation', num_outputs=3, data_partition=(75, 15),
#       tolerance=0.001, learning_rate=0.4, maximum_epochs=8000,
#       adapt_learning_rate=False, annealing_value=2000,
#       display_graph_windows=False, display_graph_pdf=True,
#       data_file_has_titles=True, data_file_has_brief_titles=True,
#       minimum_slope_to_consider_overfitting=3, number_of_epochs_for_overfit_check=10)


# Study('dataSW3.csv', 'cross validation', num_outputs=3, data_partition=(75, 15),
#       tolerance=0.000001, learning_rate=0.4, maximum_epochs=3000,
#       adapt_learning_rate=False, annealing_value=2000,
#       display_graph_windows=False, display_graph_pdf=True,
#       data_file_has_titles=True, data_file_has_brief_titles=True,
#       minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10)

# Study(purpose= "advanced query", previous_study_data_file="NeuroCharterNet.nsr", start_time=t1,
#       input_parameters_suggested_values= (4, ('VGN', 'KSG'), [50, 150, 50], [15, 19, 2],
#                                           6.2, [-.5, 1, 0.5], [0.25, 1, 0.25], 0.047))

# Study(purpose= "advanced query", previous_study_data_file="NeuroCharterNet.nsr", start_time=t1,
#       input_parameters_suggested_values= ([1, 8, 2], ('VGN', 'KSG'), [30, 360, 30], [11, 19, 2],
#                                           6.2, [-.97, 0.97, 0.25], [0.25, 1, 0.25], 0.047))
# from NeuroCharter import *

# Study('Method6.5.csv', 'cross validation', num_outputs=3, data_partition=(75, 15),
#       tolerance=0.000001, learning_rate=0.4, maximum_epochs=650,
#       adapt_learning_rate=False, annealing_value=2000,
#       display_graph_windows=False, display_graph_pdf=False,
#       data_file_has_titles=True, data_file_has_brief_titles=True,
#       minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10,
#       relative_importance_method="M")



# Study('datan.csv', 'cross validation', num_outputs=4, data_partition=(75, 15),
#
# for study in range(2, 5):
#     filename = 'M%02d.csv' % study
#     prefix = 'M%02d_'% study
#     # print filename, prefix
#
#     Study(filename, 'cross validation', num_outputs=3, data_partition=(80, 5),
#           tolerance=0.000001, learning_rate=0.4, maximum_epochs=500,
#           adapt_learning_rate=False, annealing_value=2000,
#           display_graph_windows=False, display_graph_pdf=False,
#           data_file_has_titles=True, data_file_has_brief_titles=True,
#           minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10,
#           relative_importance_method="M", folder_prefix=prefix )

# methods = [('M01', '11110111001100001110'), ('M02', '11110111001100001101'), ('M03', '11101111001100001110'),
#            ('M04', '11101111001100001101'), ('M05', '11110101110000001110'), ('M06', '11110101110000001101'),
#            ('M07', '11101101110000001110'), ('M08', '11101101110000001101'), ('M09', '11110111011100001110'),
#            ('M10', '11110111011100001101'), ('M11', '11101111011100001110'), ('M12', '11101111011100001101'),
#            ('M13', '11110111001100011110'), ('M14', '11110111001100011101'), ('M15', '11101111001100011110'),
#            ('M16', '11101111001100011101'), ('M17', '11110101110000011110'), ('M18', '11110101110000011101'),
#            ('M19', '11101101110000011110'), ('M20', '11101101110000011101'), ('M21', '11110111011100011110'),
#            ('M22', '11110111011100011101'), ('M23', '11101111011100011110'), ('M24', '11101111011100011101'),
#            ('M25', '11110111001111101110'), ('M26', '11110111001111101101'), ('M27', '11101111001111101110'),
#            ('M28', '11101111001111101101'), ('M29', '11110101110011101110'), ('M30', '11110101110011101101'),
#            ('M31', '11101101110011101110'), ('M32', '11101101110011101101'), ('M33', '11110111011111101110'),
#            ('M34', '11110111011111101101'), ('M35', '11101111011111101110'), ('M36', '11101111011111101101'),
#            ('M37', '11110111001111111110'), ('M38', '11110111001111111101'), ('M39', '11101111001111111110'),
#            ('M40', '11101111001111111101'), ('M41', '11110101110011111110'), ('M42', '11110101110011111101'),
#            ('M43', '11101101110011111110'), ('M44', '11101101110011111101'), ('M45', '11110111011111111110'),
#            ('M46', '11110111011111111101'), ('M47', '11101111011111111110'), ('M48', '11101111011111111101'),
#            ('M49', '11111111111111111110'), ('M50', '11111111111111111101'), ('M51', "11111111111111111111")]

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Study('DataN.csv', 'cross validation', num_outputs=4, data_partition=(75, 15),
#       tolerance=0.0000001, learning_rate=0.4, maximum_epochs=350,
#       adapt_learning_rate=False, annealing_value=2000,
#       display_graph_windows=False, display_graph_pdf=False,
#       data_file_has_titles=True, data_file_has_brief_titles=True,
#       minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10,
#       relative_importance_method="M")
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# _dummy = None

# for repeat in range(1):
#     # for method in methods:
#     # for merging text files goto command prompt and execute this: copy *.txt @02newfile.txt
#     methods_selected = [5] # now write the actual number of the method, not the index of it
#     methods_selected = map(lambda y: y - 1, methods_selected)  # range(51)[::-1]  # [4, 8, 20]
#     random.shuffle(methods_selected)
#     for num_method in methods_selected:  # (50,49,-1)[::-1]:
#                                           # (51)[::-1]:  # (51, 48, -1) 8=M09, 4=M05, 20=M21, 50=M51
#         method = methods[num_method]
#         prefix = method[0] + '_'
#         key = method [1]
#         num = int(prefix[1:3])
#         outs = 4 if num == 51 else 3
#         # if num in [5, 9, 21]:
#         try:
#             # if num <= 20:
#             Study('GrossData3V.csv', 'cross validation', num_outputs=outs, data_partition=(75, 15),
#                   tolerance=0.0000001, learning_rate=0.4, maximum_epochs=500,
#                   adapt_learning_rate=False, annealing_value=2000,
#                   display_graph_windows=False, display_graph_pdf=False,
#                   data_file_has_titles=True, data_file_has_brief_titles=True,
#                   minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10,
#                   relative_importance_method="M", folder_prefix=prefix,
#                   variable_selection_key=key)
#         except Exception, err:
#             print '\n\n\nUnfortunately, the following method failed:' + str(method)
#             # traceback.print_exc()
#             # traceback.print_stack()
#             print err

# _dummy2 = None
# Study(purpose= "advanced query", previous_study_data_file="NeuroCharterNet.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ([1, 8, 2], ('VGN', 'KSG'), [30, 360, 30], [11, 19, 2],
#                                           6.2, [-.97, 0.97, 0.25], [0.25, 1, 0.25], 0.047))
#
# Study(purpose= "advanced query", previous_study_data_file="M05.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), 'SND',
#                                           6.2, [-.95, 0.80, 0.25], [0.25, 1, 0.25], 0.047))
#
# Study(purpose= "advanced query", previous_study_data_file="M09.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), 'SND',
#                                           6.2, [0.08, 0.39, .035], [-.95, 0.80, 0.25], 0.047, .045, .43))
#
# Study(purpose= "advanced query", previous_study_data_file="M21.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), 'SND',
#                                           6.2, [0.08, 0.39, .035], [-.95, 0.80, 0.25], 0.047, .045, .43, 0))
# print 'OK'
# Study(purpose= "advanced query", previous_study_data_file="M05.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), 'SND',
#                                           6.2,
#                                           (0.986111111, 0.958333333, 0.916666667, 0.875, 0.833333333, 0.666666667,
#                                            0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757,
#                                            -0.932480126),
#                                           (0.104514623, 0.197689766, 0.290864909, 0.384040052,0.477215195, 0.570390338,
#                                            0.663565481, 0.756740623,0.849915766),
#                                           0.047))
#
# Study(purpose= "advanced query", previous_study_data_file="M09.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), 'SND',
#                                           6.2,
#                                           (0.08523813, 0.12111056, 0.15698299, 0.19285542, 0.22872785, 0.26460028,
#                                            0.30047271, 0.33634514, 0.37221757),
#                                           (0.986111111, 0.958333333,0.916666667, 0.875, 0.833333333, 0.666666667,
#                                            0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757, -0.932480126),
#                                           0.047, .045, .43))
#
# Study(purpose= "advanced query", previous_study_data_file="M21.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), 'SND',
#                                           6.2,
#                                           (0.08523813, 0.12111056, 0.15698299, 0.19285542, 0.22872785, 0.26460028,
#                                            0.30047271, 0.33634514, 0.37221757),
#                                           (0.986111111, 0.958333333, 0.916666667, 0.875, 0.833333333, 0.666666667,
#                                            0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757, -0.932480126),
#                                           0.047, .045, .43, (0, 1)))
# print 'OK'

# methods = [('M01', '111101110011000011'), ('M02', '111101110011000011'), ('M03', '111011110011000011'),
#            ('M04', '111011110011000011'), ('M05', '111101011100000011'), ('M06', '111101011100000011'),
#            ('M07', '111011011100000011'), ('M08', '111011011100000011'), ('M09', '111101110111000011'),
#            ('M10', '111101110111000011'), ('M11', '111011110111000011'), ('M12', '111011110111000011'),
#            ('M13', '111101110011000111'), ('M14', '111101110011000111'), ('M15', '111011110011000111'),
#            ('M16', '111011110011000111'), ('M17', '111101011100000111'), ('M18', '111101011100000111'),
#            ('M19', '111011011100000111'), ('M20', '111011011100000111'), ('M21', '111101110111000111'),
#            ('M22', '111101110111000111'), ('M23', '111011110111000111'), ('M24', '111011110111000111'),
#            ('M25', '111101110011111011'), ('M26', '111101110011111011'), ('M27', '111011110011111011'),
#            ('M28', '111011110011111011'), ('M29', '111101011100111011'), ('M30', '111101011100111011'),
#            ('M31', '111011011100111011'), ('M32', '111011011100111011'), ('M33', '111101110111111011'),
#            ('M34', '111101110111111011'), ('M35', '111011110111111011'), ('M36', '111011110111111011'),
#            ('M37', '111101110011111111'), ('M38', '111101110011111111'), ('M39', '111011110011111111'),
#            ('M40', '111011110011111111'), ('M41', '111101011100111111'), ('M42', '111101011100111111'),
#            ('M43', '111011011100111111'), ('M44', '111011011100111111'), ('M45', '111101110111111111'),
#            ('M46', '111101110111111111'), ('M47', '111011110111111111'), ('M48', '111011110111111111'),
#            ('M49', '111111111111111111')]
#
#
#
# for dummy_repeat in range(5):
#     # for method in methods:
#     # for merging text files goto command prompt and execute this: copy *.txt @02newfile.txt
#     selected_range = [4, 8, 20] # range(49)[::-1]  # [4, 8, 20]
#     random.shuffle(selected_range)
#     for num_method in selected_range:
#         method = methods[num_method]
#         prefix = method[0] + '_'
#         key = method [1]
#         num = int(prefix[1:3])
#         outs = 2
#         # if num in [5, 9, 21]:
#         try:
#             # if num <= 20:
#             Study('d_ABLim.csv', 'cross validation', num_outputs=outs, data_partition=(85, 5),
#                   tolerance=0.0000001, learning_rate=0.4, maximum_epochs=1000,
#                   adapt_learning_rate=False, annealing_value=2000,
#                   display_graph_windows=False, display_graph_pdf=False,
#                   data_file_has_titles=True, data_file_has_brief_titles=True,
#                   minimum_slope_to_consider_overfitting=2, number_of_epochs_for_overfit_check=10,
#                   relative_importance_method="M", folder_prefix=prefix,
#                   variable_selection_key=key)
#         except:
#             print '\n\n\nUnfortunately, the following method failed:' + str(method)

# q_vals = (1, 2, 3, 4, 6, 8, 12)
# models = ('VGN', 'Dul', 'MVG', 'BrC', 'KSG', 'VG2')
# duration = (30, 60, 90, 120, 180, 240, 360)
# texture = ('ClL', 'SCL', 'SND', 'SnC', 'LSn', 'SnL', 'Lom', 'Slt')
# fem = (1.5, 2.5, 6.2, 10, 12.5, 20)
# time_factor = (0.986111111, 0.958333333, 0.916666667, 0.875, 0.833333333, 0.666666667,
#                 0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757, -0.932480126)
# eff_sat = (0.104514623, 0.197689766, 0.290864909, 0.384040052,0.477215195, 0.570390338,
#                                            0.663565481, 0.756740623,0.849915766)
# sat_cond = (.047, .1, .2, .24319, .3, .4, .495)
# print '.'
#
# Study(purpose= "advanced query", previous_study_data_file="M05n3V.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), ('SND', 'Lom'),
#                                           6.2,
#                                           (0.986111111, 0.958333333, 0.916666667, 0.875, 0.833333333, 0.666666667,
#                                            0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757,
#                                            -0.932480126),
#                                           (0.104514623, 0.197689766, 0.290864909, 0.384040052,0.477215195, 0.570390338,
#                                            0.663565481, 0.756740623,0.849915766),
#                                           0.495))
#
# Study(purpose= "advanced query", previous_study_data_file="M09n3V.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), ('SND', 'Lom'),
#                                           6.2,
#                                           (0.08523813, 0.12111056, 0.15698299, 0.19285542, 0.22872785, 0.26460028,
#                                            0.30047271, 0.33634514, 0.37221757),
#                                           (0.986111111, 0.958333333,0.916666667, 0.875, 0.833333333, 0.666666667,
#                                            0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757, -0.932480126),
#                                           0.495, .045, .43))
#
# Study(purpose= "advanced query", previous_study_data_file="M21n3V.nsr", start_time=time.time(),
#       input_parameters_suggested_values= ((2, 4), ('VGN', 'KSG'), (240, 360), ('SND', 'Lom'),
#                                           6.2,
#                                           (0.08523813, 0.12111056, 0.15698299, 0.19285542, 0.22872785, 0.26460028,
#                                            0.30047271, 0.33634514, 0.37221757),
#                                           (0.986111111, 0.958333333, 0.916666667, 0.875, 0.833333333, 0.666666667,
#                                            0.5, 0.333333333, 0, -0.732888922, -0.81010134, -0.887313757, -0.932480126),
#                                           0.495, .045, .43, (0, 1)))