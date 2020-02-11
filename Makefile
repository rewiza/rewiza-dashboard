help:
	@echo "build         Build docker container"
	@echo "publish       Push docker container"

build:
	docker build -t registry.gitlab.com/dresl/kubernetes/rewiza-dashboard .

publish:
	docker push registry.gitlab.com/dresl/kubernetes/rewiza-dashboard
