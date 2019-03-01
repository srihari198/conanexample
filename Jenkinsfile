node{
    def server = Artifactory.server "Artprod"
    def client = Artifactory.newConanClient()
    def name = client.remote.add server: server, repo: "conan-local"

    stage("Get recipe"){
        checkout scm
    }
    stage("Create package"){
        client.run(comman: "create . user/test -s os=Macos")
    }
    stage("Upload packages"){
        String command = "upload LibA* -- all -r ${name} --confirm"
        def b = client.run(command: command)
    }
}
