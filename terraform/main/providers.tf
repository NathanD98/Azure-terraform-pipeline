terraform {
  required_version = ">= 1.0"

  # Configure the remote backend (used by the Azure DevOps pipeline to store state)
  backend "azurerm" {
    # These values are often overridden by the pipeline's 'terraform init' command
    # using the backend-config flag for dynamic access keys and environment separation.
  }

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# Provider configuration
provider "azurerm" {
  features {}
  # Authentication details are usually inherited from the pipeline's service connection (SPN)
}