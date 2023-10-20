# Katonic Studio - Working with Pipeline Parameters

Katonic Studio provides a powerful way to create and manage data pipelines. One of the key features is the ability to use pipeline parameters. Pipeline parameters allow you to create dynamic and reusable pipelines that can be configured with different values for various components in your pipeline.

## Table of Contents

- [Defining Pipeline Parameters](#defining-pipeline-parameters)
- [Using Pipeline Parameters in Components](#using-pipeline-parameters-in-components)
- [Passing Parameter Values](#passing-parameter-values)

## Defining Pipeline Parameters

Pipeline parameters are defined in the "Properties" window in Katonic Studio. Here's how to define pipeline parameters:

1. **Open Your Pipeline**: Start by opening your pipeline project in Katonic Studio or create a new pipeline editor from the launcher.

![katonic pipeline editor:](https://github.com/katonic-dev/Examples/blob/master/Katonic_studio_pipeline_parameters/Screenshots/katonic%20pipeline%20editor.png)


2. **Access the Properties Window**: In the pipeline canvas/panel, select the panel and In the right-hand sidebar, you'll see the an exit icon decribing "open panel" right next to the "Runtime:" description. Click on it to open the Properties window of the pipeline panel.

!["open panel" icon:](https://github.com/katonic-dev/Examples/blob/master/Katonic_studio_pipeline_parameters/Screenshots/Properties%20icon.png)

3. **Add a New Parameter**: In the Pipleline Parameter window, click the "Add Parameter" button. This will allow you to define a new parameter/set of parameters.

4. **Configure the Parameter**: Give your parameter a name, a description (optional), and specify its data type. Data types can be string, integer, float, boolean, etc. You can also set a default value for the parameters.

5. **Repeat as Needed**: You can add as many parameters as needed for your pipeline components.

![Adding the parameters](https://github.com/katonic-dev/Examples/blob/master/Katonic_studio_pipeline_parameters/Screenshots/Adding%20parameters.png)

## Using Pipeline Parameters in Components

Now that you've defined pipeline parameters, you can use them in your pipeline components. Here's how to use pipeline parameters in components:

1. **Select a Component**: select/click on the component where you want to the pipeline parameter defined before.

2. **Access the Parameters Properties Window**: Just like before, access the "open panel" icon or right click on the for the component where you will see an option to open the "properties window".

3. **Open the Node parameters tab**: While in the properties window click/select the "Node Parameters" tab and select the component u want to edit the propeties of in the panel, after this step scroll down the "Node Parameters" window where you will see a list of Checkboxes under the .

3. **Include the Parameters for the needed components usage**: After the above step scroll down the "Node Parameters" window where you will see a list of Checkboxes under "Pipeline Parameters" where you can select on the parameters to use for the component.

![Using the Defined paramters for the selected components:](https://github.com/katonic-dev/Examples/blob/master/Katonic_studio_pipeline_parameters/Screenshots/Using%20the%20Defined%20paramters%20.png)

3. **Reference and use the Parameter in your code**: To use a parameter, you can reference it in a field by enclosing its name in double curly braces, e.g., `{{data_path}}` or you can use the os.environ.get() to get the values of the parameter, e.g., `data_path_param = os.environ.get("data_path", "No value found")
data_path=f"{data_path_param}" `. The parameter name should match the one you defined in "Pipeline Parameters".

4. **Configure Other Properties**: You can configure other properties of the component as needed.

6. **Repeat for Other Components**: You can use pipeline parameters in multiple components as required.

## Passing Parameter Values

After defining and using pipeline parameters, you need to pass values to these parameters when running a pipeline. Here's how to do it:

1. **Run the Pipeline**: Start running your pipeline in Katonic Studio.

![Run Pipeline:](https://github.com/katonic-dev/Examples/blob/master/Katonic_studio_pipeline_parameters/Screenshots/Run%20pipeline.png)

2. **Configure Parameters**: During the pipeline run, you will have the option to configure parameter values. You can provide specific values for each parameter.

![Asssigning pipieline parameter value:](https://github.com/katonic-dev/Examples/blob/master/Katonic_studio_pipeline_parameters/Screenshots/Asssigning%20pipieline%20value.png)

3. **Run the Pipeline with Custom Values**: Start the pipeline run with the custom parameter values you've provided. The pipeline will execute using the values you specified. As for the above "Amazon_revenue" pipeline, you can use "https://raw.githubusercontent.com/katonic-dev/Examples/master/amazon_revenue_forcasting/amazon_revenue_data.csv" to run for the example pipeline created.

4. **Reuse with Different Values**: You can reuse the same pipeline with different parameter values by reconfiguring them each time.

By following these steps, you can effectively use and manage pipeline parameters in Katonic Studio, making your data pipelines more dynamic and versatile.


