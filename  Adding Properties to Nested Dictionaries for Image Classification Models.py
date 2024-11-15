{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "machine_shape": "hm",
      "gpuType": "T4",
      "authorship_tag": "ABX9TyNugJD7OayO7FSUQ4I2Wr8u",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/elifnuryaygin03/elifnuryaygin/blob/main/%20Adding%20Properties%20to%20Nested%20Dictionaries%20for%20Image%20Classification%20Models.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1aL_VAzddD0d",
        "outputId": "b8dd27d2-f32e-4337-d006-ae0107a4ca52"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Your code passes all of our tests, nice work!\n"
          ]
        }
      ],
      "source": [
        "##Lightweight Models in Deep Learning\n",
        "#Lightweight models are deep learning models designed to be efficient in terms of memory usage,\n",
        "#computational cost, and power consumption. These models are particularly useful for deployment on devices with limited resources,\n",
        "# such as mobile phones, embedded systems, and edge devices. The primary goals of lightweight models are to reduce the number of\n",
        "# parameters and operations required for inference while maintaining a high level of accuracy.\n",
        "\n",
        "#Lightweight models play a crucial role in making AI accessible and practical for a wide range of applications, especially in\n",
        "# scenarios where computational resources are limited.\n",
        "\n",
        "#Here are some key characteristics and benefits of lightweight models:\n",
        "\n",
        "#1-)Reduced Parameters and Computations:\n",
        "\n",
        "#Lightweight models have fewer parameters compared to traditional deep learning models. This reduction is achieved\n",
        "#through techniques like depthwise separable convolutions and pruning.\n",
        "#Fewer parameters lead to fewer computations, making the models faster and more efficient.\n",
        "\n",
        "#2-)Lower Memory Footprint:\n",
        "\n",
        "#These models require less memory for storing parameters and intermediate feature maps, making them suitable for deployment on devices with limited RAM.\n",
        "\n",
        "#3-)Energy Efficiency:\n",
        "\n",
        "#Lightweight models consume less power, which is crucial for battery-powered devices like smartphones and IoT devices.\n",
        "\n",
        "#4-)Faster Inference:\n",
        "\n",
        "#Due to reduced complexity, lightweight models can perform inference faster, enabling real-time applications such as augmented reality, real-time video analysis, and on-device AI.\n",
        "#Examples of Lightweight Models\n",
        "#MobileNet\n",
        "#MobileNet is a family of lightweight deep learning models developed by Google. MobileNet models use depthwise separable convolutions to reduce the number of parameters and computational cost. This makes them suitable for real-time applications on devices with limited resources. MobileNet architectures include versions like MobileNetV1, V2, and V3, each providing improvements in accuracy and efficiency.\n",
        "\n",
        "#SqueezeNet\n",
        "#SqueezeNet is another lightweight model designed to achieve AlexNet-level accuracy with significantly fewer parameters. It introduces \"fire modules,\" which consist of squeeze layers (with 1x1 filters) and expand layers (with both 1x1 and 3x3 filters). SqueezeNet is highly efficient, making it suitable for deployment on devices with limited computational resources.\n",
        "\n",
        "#EfficientNet\n",
        "#EfficientNet is a family of convolutional neural network (CNN) architectures and scaling methods developed by Google. EfficientNet optimizes both the network architecture and scaling methods by using a compound scaling method that uniformly scales the depth, width, and resolution of the network. This approach achieves high performance with fewer parameters and lower computational cost compared to traditional models.\n",
        "\n",
        "###Quiz: Adding Properties to Nested Dictionaries for Image Classification Models\n",
        "#In this exercise, you will work with nested dictionaries. Add another entry, is_lightweight, to each dictionary in the models dictionary. After inserting the new entries, you should be able to perform these lookups:\n",
        "\n",
        "#>>> print(models['ResNet']['is_lightweight'])\n",
        "#False\n",
        "#>>> print(models['MobileNet']['is_lightweight'])\n",
        "#True\n",
        "###Here is the initial models dictionary:\n",
        "\n",
        "models = {\n",
        "    'ResNet': {'layers': 50, 'accuracy': 0.91, 'type': 'CNN'},\n",
        "    'MobileNet': {'layers': 28, 'accuracy': 0.89, 'type': 'CNN'}\n",
        "}\n",
        "\n",
        "# TODO: Add an 'is_lightweight' entry to the ResNet and MobileNet dictionaries\n",
        "# hint: MobileNet is a lightweight model, ResNet isn't\n",
        "models['ResNet']['is_lightweight'] = False\n",
        "models['MobileNet']['is_lightweight'] = True\n",
        "### Notebook grading\n",
        "explanation_str = '''Your code produced the wrong result. Looks like you did not add the 'is_lightweight' property properly for {}.'''\n",
        "if not('is_lightweight' in models['ResNet'].keys()) or models['ResNet']['is_lightweight'] != False:\n",
        "    print(explanation_str.format(\"'ResNet'\"))\n",
        "elif not('is_lightweight' in models['MobileNet'].keys()) or models['MobileNet']['is_lightweight'] != True:\n",
        "    print(explanation_str.format(\"'MobileNet'\"))\n",
        "else:\n",
        "    print(\"\"\"Your code passes all of our tests, nice work!\"\"\")"
      ]
    }
  ]
}