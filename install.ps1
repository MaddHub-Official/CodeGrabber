# Copyright 2024 maddjester
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

$getpip = ".\get-pip.py"

$uri = "https://bootstrap.pypa.io/get-pip.py"

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) { Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"$url = (Invoke-WebRequest -Uri 'https://www.python.org/downloads/windows/').Content | Select-String -Pattern 'https://www.python.org/ftp/python/\d+\.\d+\.\d+/python-\d+\.\d+\.\d+-amd64\.exe' -AllMatches | % { `$_.Matches[0].Value }; $path = `$env:USERPROFILE\Downloads\ + (`$url -split '/')[-1]; Invoke-WebRequest -Uri `$url -OutFile $path; if ((Read-Host 'Python not found! Install? (Y/N)') -ieq 'y') { Start-Process -FilePath $path -Wait }`"" -Verb RunAs } else { $url = (Invoke-WebRequest -Uri 'https://www.python.org/downloads/windows/').Content | Select-String -Pattern 'https://www.python.org/ftp/python/\d+\.\d+\.\d+/python-\d+\.\d+\.\d+-amd64\.exe' -AllMatches | ForEach-Object { $_.Matches[0].Value }; $path = "$env:USERPROFILE\Downloads\" + ($url -split '/')[-1]; Invoke-WebRequest -Uri $url -OutFile $path; if ((Read-Host "Python not found! Install? (Y/N)") -ieq 'y') { Start-Process -FilePath $path -Wait }}

if (-not (Test-Path $getpip)) {

    Write-Progress "Configuring pip..."

    Invoke-WebRequest -Uri $uri -OutFile ".\get-pip.py" -Verbose

    ICACLS ".\" /grant:r "users:(RX)" /C

    Start-Process -FilePath $getpip -ArgumentList $getpip -Wait
}

$ps1path = ".\venv\Scripts\activate.ps1"

if (-not(Test-Path $ps1path)) {

    Write-Progress "Creating a new python enviroment."

    Start-Process "python" -ArgumentList "-m venv venv" -Wait 

    Start-Process $ps1path -Wait -NoNewWindow

}

Write-Progress "Installing Dependencies"

Start-Process "pip" -ArgumentList "install -r requirements.txt" -Wait

Write-Host "Press any key to continue..."