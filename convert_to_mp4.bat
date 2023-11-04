@REM @echo off
for %%f in (%*) do (
ffmpeg -i %%f -c:v copy -c:a copy %%~nf.mp4
)
pause
exit /B 0
