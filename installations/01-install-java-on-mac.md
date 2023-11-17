

### List of commands

```sh
brew install openjdk
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

vim .zshrc
export JAVA_HOME=/Library/Java/JavaVirtualMachines/openjdk.jdk/Contents/Home

brew install maven

# Install javatuple
mvn dependency:get -Dartifact=org.javatuples:javatuples:1.2
```