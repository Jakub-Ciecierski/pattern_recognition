import data_calculations.data_manager as data
from data_calculations.distorter import Distorter

import util.global_variables as global_v
import util.logger as logger
import util.progress_bar as p_bar

import clustering.evaluation.prediction_strength as ps
import clustering.evaluation.mcclain_rao as mc_r
import clustering.evaluation.pbm as pbm

from gui.plot_3d import Plot3D
from clustering.clusterer import Clusterer

def run():
    logger.log_header("Cluster Evaluation")

    symbolClasses = __generate_symbol()
    '''
    global_v.K = 3
    Clusterer().computeClusters(symbolClasses)
    Plot3D().renderPlot(symbolClasses)
    '''
    __compute_cluster_evaluation(symbolClasses[0].learning_set)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

'''
    Generates symbol for cluster evaluation
'''
def __generate_symbol():
    characteristics = []
    data.generate_characteristic(characteristics)

    symbolClasses = []
    data.generate_symbol_classes(symbolClasses, characteristics)

    Distorter().create_cluster_assessment_cloud(global_v.K_CLOUD_DISTORTION,
                                            symbolClasses)

    return symbolClasses

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def __compute_cluster_evaluation(training_set):
    start_k = 2
    end_k   = global_v.MAX_K_CLUS_EVALUATION

    __ps_evaluation(training_set, start_k, end_k)

    __mc_r_evaluation(training_set, start_k, end_k)

    __pbm_evaluation(training_set, start_k, end_k)

#-------------------------------------------------------------------------------

def __ps_evaluation(training_set, start_k, end_k):
    logger.log_header("Prediction Strength")

    Results = ps.compute(training_set,
                start_k, end_k)

    for i in range(0, len(Results)):
        logger.log("ps(" + str(i+start_k) + ") = " + str(Results[i]),
                    styles=[logger.LogStyle.NONE])


#-------------------------------------------------------------------------------

def __mc_r_evaluation(training_set, start_k, end_k):
    logger.log_header("McClain-Rao")

    Results = mc_r.compute(training_set,
                start_k, end_k)

    for i in range(0, len(Results)):
        logger.log("mc_r(" + str(i+start_k) + ") = " + str(Results[i]),
                    styles=[logger.LogStyle.NONE])

#-------------------------------------------------------------------------------

def __pbm_evaluation(training_set, start_k, end_k):
    logger.log_header("PBM")

    Results = pbm.compute(training_set,
                start_k, end_k)

    for i in range(0, len(Results)):
        logger.log("pbm(" + str(i+start_k) + ") = " + str(Results[i]),
                    styles=[logger.LogStyle.NONE])
