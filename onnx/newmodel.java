import ai.onnxruntime.*;

import java.util.*;

public class OnnxModelRunner {
    public static void main(String[] args) {
        try {
            // 1. Create the ONNX Runtime environment
            OrtEnvironment env = OrtEnvironment.getEnvironment();

            // 2. Load the model
            OrtSession.SessionOptions sessionOptions = new OrtSession.SessionOptions();
            OrtSession session = env.createSession("logistic_model.onnx", sessionOptions);

            // 3. Prepare input: 1 sample with 4 features (adjust size as per your model)
            float[][] inputData = new float[][]{
                {0.5f, -1.2f, 1.1f, 0.7f}  // Example input
            };

            // 4. Create input tensor
            OnnxTensor inputTensor = OnnxTensor.createTensor(env, inputData);

            // 5. Create input map
            Map<String, OnnxTensor> inputMap = new HashMap<>();
            inputMap.put("float_input", inputTensor);  // Must match the input name from Python export

            // 6. Run inference
            OrtSession.Result result = session.run(inputMap);

            // 7. Get and print result
            float[][] output = (float[][]) result.get(0).getValue();
            System.out.println("Prediction: " + Arrays.toString(output[0]));

            // Cleanup
            inputTensor.close();
            session.close();
            env.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
