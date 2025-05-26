const ort = require('onnxruntime-node');

async function runModel() {
  try {
    // Load the model
    const session = await ort.InferenceSession.create('logistic_model.onnx');

    // Example input: 1 sample with 4 features
    const inputData = Float32Array.from([0.5, -1.2, 1.1, 0.7]);

    // Create a tensor (shape [1, 4] for 1 sample with 4 features)
    const tensor = new ort.Tensor('float32', inputData, [1, 4]);

    // Run inference
    const feeds = { float_input: tensor };  // Must match input name from Python
    const results = await session.run(feeds);

    // Print prediction result
    const output = results[Object.keys(results)[0]];
    console.log('Prediction:', output.data);
  } catch (err) {
    console.error('Failed to run model:', err);
  }
}

runModel();
