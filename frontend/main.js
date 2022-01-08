let loginBtn = document.getElementById('login-btn');
let logoutBtn = document.getElementById('logout-btn');
let token = localStorage.getItem('token');

if(token){
    loginBtn.remove()
}else{
    logoutBtn.remove()
}

logoutBtn.addEventListener('');

let projectUrl = "http://127.0.0.1:8000/api/projects/";
let getProjects = () =>{
    fetch(projectUrl).then(response => response.json())
    .then(data => {
        console.log(data);
        buildProjects(data);
    });
}
getProjects();

buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper');
    projectsWrapper.innerHTML = ''
    console.log('projectsWrapper:',projectsWrapper);
    for(let i=0;projects.length>i;i++){
        let project = projects[i];
        console.log(project);
        let  projectCard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}" height='200px' width='200px'/>
                
                <div>
                    <div class="card--header">
                    <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project=${project.id}>&#43;</strong>
                        <strong class="vote--option" data-vote="down">&#8722;</strong>
                    </div>
                    <i>${project.vote_ratio}% Postive Feedback</i>
                    <p>${project.description.substring()}</p>
                </div>
            </div>
        `;
        projectsWrapper.innerHTML += projectCard;
    }
    addVoteEvents();
}

let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option');
    console.log(voteBtns)
    for(let i=0;i<voteBtns.length;i++){
        let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxNjI5OTcyLCJpYXQiOjE2NDE2Mjk2NzIsImp0aSI6IjJjNmM5NTEwMTE5NjRkOTZhZDMxY2U2YTgzYjQ3ZWY3IiwidXNlcl9pZCI6MX0.oSeUvk25lVNJWq5NokcilfSNw7Z7M_mWPJ8wrq84lxg";
        voteBtns[i].addEventListener('click',(e)=>{
            console.log('Vote was  clicked:',i)
            let vote = e.target.dataset.vote;
            let project = e.target.dataset.project; 
            fetch('http://127.0.0.1:8000/api/projects/${projects}/vote/',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    'Authorization':`Bearer ${token}`
                },
                body:JSON.stringify({'value':vote}),
            })
            .then(response => response.json())
            .then(data =>{
                console.log('Success:',data)
                getProjects()
            })
        })
    }
}
