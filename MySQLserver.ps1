$ResourceGroupName = "Mehrnoush_DR"
$MySQLServername = "mehrnoushsql11"
$MySQLuser = "Mehrnoush"
$Password = ConvertTo-SecureString -String "Mehrnoush123" -AsPlainText -Force
$Location = "EastUS"

New-AzMySqlServer -Name $MySQLServername `
    -ResourceGroupName $ResourceGroupName `
    -Location $Location `
    -AdministratorUser $MySQLuser `
    -AdministratorLoginPassword $Password