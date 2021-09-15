
The machine learning processes are computationally heavy, that can't possibly be avoided.

On production though it is of paramount importance to reduce store the binary models using minio

in an equivalent of a google bucket (amazon s3 etc). If we had multiple inputs that had the need of simultaneous service

we could use celery & rabidMQ to handle the multiple messages at the same time and use workers to handle the inference.

In any case the best option is always to train our models asynchronously and the post the inference results using the

aforementioned method and show those results via rest calls.
