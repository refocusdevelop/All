problems and GIT up
2017-01
  
kullis-MacBook-Pro:~ kullirist$ ls -a   //et näha selle user .ssh kausta, kus on peidus võtmed
  cat .ssh/               //et näha sisse: id_rsa       id_rsa.pub   known_hosts 
  ls .ssh/*.pub          //et näha sisse faili, mille nimi sisaldab "pub"
  cat .ssh/id_rsa.pub   //et näha koodi,provaidib selle
  ssh   //to see which kind commands it possibly includes!!!
  ssh-keygen  //to gebereate new, shows and asks where in which name to genereate it, no need for code in my PC
  mv id_rsa2* .ssh/    KUI JUHTUB VALESSE KOHTA, siis me MOVE TO better LOCATION
  ls .ssh/*.pub        To see its full PATH
  cat .ssh/id_rsa2.pub TO COPY ITS CODE
  
  
Problem: THAT MUST BE OFF FROM SETTINGS OF GITHUB:
Restrict editing to collaborators only
Public wikis will still be readable by everyone

setting multiple github account on one pc  “mherman.org managing multiple github”
 2 accounts: FIRST IS MAIN ONE
  we created a sep file to Home catalogue, was instructed via:
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa
Host refocusdevelop
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa2
