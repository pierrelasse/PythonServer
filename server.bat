@rem @echo off & title Server & cls & python server/main.py & pause > nul

@echo off

@rem Settings

set name=Server

@rem Settings end


title  
echo Starting...
:start

@rem java -Xmx2G -Xms2G -DIReallyKnowWhatIAmDoingISwear=true -jar server.jar nogui
python server/main.py

echo.
echo Program ended. Press return to restart!
pause > nul
goto start
