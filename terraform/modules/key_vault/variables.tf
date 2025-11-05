# variables.tf

variable "key_vault_name" {
  description = "The name for the Azure Key Vault. Must be globally unique."
  type        = string
}

variable "resource_group_name" {
  description = "The name of the Resource Group where the Key Vault should be deployed."
  type        = string
}

variable "location" {
  description = "The Azure region where the Key Vault will be created."
  type        = string
}

variable "sku_name" {
  description = "The SKU for the Key Vault. Options are 'standard' or 'premium'."
  type        = string
  default     = "standard"
}

# Variables whose values will be used directly in the tags object
variable "project_name" {
  description = "The name of the project. Used for the 'Project' tag."
  type        = string
}

variable "environment" {
  description = "The deployment environment (e.g., 'dev', 'prod'). Used for the 'Environment' tag."
  type        = string
}