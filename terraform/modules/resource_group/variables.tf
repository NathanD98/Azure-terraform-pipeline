# variables.tf

variable "resource_group_name" {
  description = "The name for the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "The Azure region where the Resource Group will be created (e.g., 'East US', 'West Europe')."
  type        = string
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