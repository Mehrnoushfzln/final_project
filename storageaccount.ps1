
$resourceGroupName = "Mehrnoush_DR"
$storageAccountName = "mehrnoushstorage11"



New-AzResourceGroup -Name $resourceGroupName -Location "East US"


$storageAccount = New-AzStorageAccount -ResourceGroupName $resourceGroupName `
                                      -Name $storageAccountName `
                                      -SkuName "Standard_LRS" `
                                      -Location "East US" `
                                      -Kind "StorageV2" `
                                      -EnableHttpsTrafficOnly $true



