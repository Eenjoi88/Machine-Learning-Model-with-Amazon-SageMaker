# deploys the model on a server and creates a SageMaker endpoint to access.
xgb_predictor = xgb.deploy(initial_instance_count=1,instance_type='ml.m4.xlarge')