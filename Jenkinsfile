node{
    def server = Artifactory.server "Art"
    def client = Artifactory.newConanClient()
    def name = client.remote.add server: server, repo: "conan-local"

    stage("Get recipe"){
        checkout scm
    }
    stage("Get dependencies and publish build info"){
    sh "mkdir -p build"
    dir ('build') {
      def b = client.run(command: "install ..")
      server.publishBuildInfo b
        }
    }
    stage("Build/Test project"){
        dir ('build') {
          sh "cmake ../ && cmake --build ."
        }
    }
    stage("Upload packages"){
        String command = "upload LibA* --all -r ${name} --confirm"
        def b = client.run(command: command)
    }
}
