"""
Mask R-CNN serve, profile and manage demo using ModelCI.
"""

from modelci.hub.client.tfs_client import CVTFSClient
from modelci.hub.manager import retrieve_model_by_name, register_model_from_yaml
from modelci.hub.profiler import Profiler
from modelci.persistence.bo.model_objects import Engine, Framework

if __name__ == "__main__":
    data_path = '' # test data path
    with open(data_path, 'rb') as f: # for TensorFlow Serving
        model_path = '' # Mask R-CNN model saved path
        tfs_client = CVTFSClient(f.read(), batch_num=100, batch_size=32, asynchronous=True)

        register_model_from_yaml(model_path) # register your model in the database
        mode_info = retrieve_model_by_name(architecture_name='ResNet50', framework=Framework.PYTORCH,engine=Engine.TORCHSCRIPT) # retrieve modelm information

        profiler = Profiler(model_info=mode_info, server_name='tfs', inspector=tfs_client)
        profiler.auto_diagnose([2, 4, 16]) # profile batch size 2, 4, 6 inb all availavle devices