# main.tf

resource "azurerm_key_vault" "kv" {
  name                        = var.key_vault_name
  location                    = var.location
  resource_group_name         = var.resource_group_name
  sku_name                    = var.sku_name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id

  # tags
  tags = {
    "Project"     = var.project_name,
    "Environment" = var.environment,
    "ManagedBy"   = "Terraform" # Example of a fixed tag value
  }
}

data "azurerm_client_config" "current" {}