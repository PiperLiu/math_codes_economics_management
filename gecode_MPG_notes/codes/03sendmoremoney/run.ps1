$filename = main
if ($args.Count -eq 1)
{
    $filename = $args[0]
}
else
{
    Write-Output "There must be one filename as arg!"
    exit
}

if (Test-Path ./$filename.obj)
{
    Remove-Item ./$filename.obj
}

if (Test-Path ./$filename.exe)
{
    Remove-Item ./$filename.exe
}

try
{
    Write-Output "compile..."
    cl /DNDEBUG /EHsc /MD /wd4355 -I "D:\Program Files\gecode\include" `
        -c ./$filename.obj -Tp ./$filename.cpp

    Write-Output "link..."
    cl /DNDEBUG /EHsc /MD /wd4355 -I "D:\Program Files\gecode\include" `
        -Fe ./$filename.obj /link /LIBPATH:"D:\Program Files\gecode\lib"

    Write-Output "run..."
    sudo ./$filename.exe
}
catch
{
    # 目前 try 捕获不到编译器的异常
    # issue: need help
    Write-Warning "Error: $_"
    exit
}
