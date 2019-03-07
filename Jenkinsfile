def artifactory_name = "Art"
def artifactory_repo = "conan-local"
def repo_url = 'https://github.com/srihari198/conanexample.git'
def repo_branch = "release/1.0.0"

node {
    def server = Artifactory.server artifactory_name
    def client = Artifactory.newConanClient()
    def serverName = client.remote.add server: server, repo: artifactory_repo

    stage("Get recipe"){
        git branch: repo_branch, url: repo_url
    }

    stage("Test recipe"){
        client.run(command: "create")
    }

    stage("Upload packages"){
        String command = "upload * --all -r ${serverName} --confirm"
        def b = client.run(command: command)
        server.publishBuildInfo b
    }
}
