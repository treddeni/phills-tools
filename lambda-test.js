var aws = require('aws-sdk');

function lambdaCallback(id) {
    return function(error, data) {
        if(error) {
            console.log(id, error);
        }
        else {
            console.timeEnd(id);
        }
    }
}

exports.handler = (event, context, callback) => {

    var lambda = new aws.Lambda({ region: 'us-east-1' });

    for (var i = 0; i < event.numCalls; i++) {
        setTimeout(function(i) {
            console.time("lambda" + i);

            lambda.invoke({
              FunctionName: event.functionName,
              InvocationType: 'Event',
              Payload: "{}"
            }, lambdaCallback("lambda" + i));
        }, i*event.intervalMilliseconds, i)
    }
}
