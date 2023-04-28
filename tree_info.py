import cohere

# Set up the Cohere client
client = cohere.Client(api_key="lEhi1tgPfVEA4ha4FFDRCeKhyEVnrgHURtPhnO8R")
model = "command-xlarge-nightly"


def get_tree_info(name):
    # Define the prompt for the model
    #prompt = "Describe the " + name + " tree, tell me about its benefits and availability, in detail"
    prompt = "How do I identify "+name+" tree, in detail. Describe its characteristics and features in detail"

    response = client.generate(model = "command-nightly",prompt=prompt,temperature = 0.8,max_tokens=500)
    #print(type(response))
    #print(response)
    info = response.data[0]
    return info


while True:
    # Prompt the user for input
    name = input("Please enter the name of a tree: ")

    # Get information based on the tree name
    info = get_tree_info(name)

    # Print the information
    t = info.split(".")
    for sentence in t:
      print(sentence)
