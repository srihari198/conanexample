node{
    def server = Artifactory.server "Art"
    def client = Artifactory.newConanClient()
    def name = client.remote.add server: server, repo: "conan-local"

    stage("Get recipe"){
        checkout scm
    }
    stage("Create package"){
        client.run(command: "create . user/test -s arch=x86")
    }
    stage("Upload packages"){
        String command = "upload * --all -r ${name} --confirm"
        def b = client.run(command: command)
    }
}
