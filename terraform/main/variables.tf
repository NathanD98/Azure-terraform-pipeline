variable "resource_groups" {
  description = "List of resource group names to create."
}

variable "key_vaults" {
  description = "List of Key Vault names to create. Must match the order of resource groups."
}