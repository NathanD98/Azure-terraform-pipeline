

module "resource_group" {
  source = "../../modules/resource_group"

  for_each = var.resource_groups

  name         = each.value.name
  location     = each.value.location
  project_name = var.project_name
  environment  = var.environment
}

module "key_vault" {
  source = "../../modules/key_vault"

  for_each = var.key_vaults

  name                = each.value.name
  location            = module.resource_group[each.value.resource_group_key].location
  resource_group_name = module.resource_group[each.value.resource_group_key].name
  sku_name            = each.value.sku_name
  project_name        = var.project_name
  environment         = var.environment
}
