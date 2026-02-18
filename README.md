pipeline
{
agent any
stages
{
stage("build")
{
steps
{
echo"building project"
sh'javac helloworld.java'
}
}
stage("test")
{
steps
{
echo"testing  project"
sh'javac helloworld.java'
}
}
}}
