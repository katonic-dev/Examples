import kfp
import kfp.dsl as dsl
from kfp import compiler
from kfp import components

EXPERIMENT_NAME = 'sample pipeline'        # Name of the experiment in the UI
BASE_IMAGE = 'python:3.8.11-slim'    # Base image used for components in the pipeline

@dsl.python_component(
    name='add_op',
    description='adds two numbers',
    base_image=BASE_IMAGE  # you can define the base image here, or when you build in the next step. 
)
def add(a: float, b: float) -> float:
    '''Calculates sum of two arguments'''
    print(a, '+', b, '=', a + b)
    return a + b


# Convert the function to a pipeline operation.
add_op = components.func_to_container_op(
    add,
    base_image=BASE_IMAGE, 
)


@dsl.pipeline(
   name='Calculation pipeline',
   description='A toy pipeline that performs arithmetic calculations.'
)
def calc_pipeline(
   a: float =2,
   b: float =8
):
    #Passing pipeline parameter and a constant value as operation arguments
    add_task = add_op(a, 4) #Returns a dsl.ContainerOp class instance. 
    
    #You can create explicit dependency between the tasks using xyz_task.after(abc_task)
    add_2_task = add_op(b, 4)
    
    add_3_task = add_op(add_task.output, add_2_task.output)
    
    add_4_task = add_op(a, add_3_task.output)
    
    add_5_task = add_op(b, add_3_task.output)
    
    add_6_task = add_op(add_4_task.output, add_5_task.output)
    
    
kfp_url = "http://ml-pipeline.kubeflow.svc.cluster.local:8888"
client = kfp.Client(host=kfp_url)

# Compile the pipeline
pipeline_func = calc_pipeline
pipeline_filename = pipeline_func.__name__ + '.pipeline.zip'
kfp.compiler.Compiler().compile(pipeline_func, pipeline_filename)


experiment = client.create_experiment(EXPERIMENT_NAME)
arguments = {'a': '7', 'b': '8'}

# Submit a pipeline run
run_name = pipeline_func.__name__ + ' run'
run_result = client.run_pipeline(experiment.id, run_name, pipeline_filename, arguments)
