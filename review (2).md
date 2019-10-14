In the django views.py
```python
# GET /posts.json
def api_posts(req):
    stories = Story.objects.all()
    stories = stories[:30]
    resp = []
    for story in stories:
        data = {}
        data["title"] = story.title
        ...
        data["comment_count"] = story.comment_set.count()
        data["username"] = story.user.username
        resp.append(data)
    return JsonResponse({"stories": resp})
```
at /stories.json you get [{"title": "...", "score": 728,...},...]

to work with react

`npm build` ? some command like that
this creates an index.html and some static files
throw the static files into static
and then make the index.html the "rendered" template

HackerNews needs <Story/> and <News/> which will load the <Story/> elements
```jsx
function Story(props) {
    return (
        <div>
            {props.title} and .link, .user, ...
        </div>
    )
}

class News extends Component {
    state = {
        stories: null
    }

    componentDidMount = async () => {
        // where baseURL is a var in index.html
        // i.e. var baseURL = "http://cors.../localhost:8000"
        let resp = await axios.get(baseURL+"/stories.json")
        let ss = resp.data
        this.setState({stories: ss})
    }

    render() {
        let stories = <p>Loading...</p>

        if (this.state.stories) {
            // now need to map the objs to elems
            let ss = this.state.stories
            stories = ss.map(s => <Story title={s.title} />)
        }
        return (
            <div>
                Posts: {stories}
            </div>
        )
    }
}
```

all the comment links would really be <NavLink>

also, your routes can have patterns in them

<Route path="/story/:id" component={FullStory}>

```jsx

class FullStory extends Component {
    state = {
        comments: null,
        story: null,
        comment: "",
    }

    submitPost = () => {

    }

    upvote = (id) => {
        let comments = this.state.comments.map(c => {
            if (c.id == id) {
                return {...c, score: (c.score+1)}
            }
            return c
        })
        this.setState({
            comments: comments
        })
        
        // also axios.post(..., {"id": id})
    }

    render() {
        let story = <p>Loading...</p>
        let comments = <p>Loading...</p>

        // somehow get the id from the <Route> tag
        // I think, this.props.match.args.id ? something like this
        // we'll call it id
        let id = this.props...id
        
        if (this.state.story) {
            let s = this.state.story
            story = <Story title={s.title} />
        }

        if (this.state.comments) {
            comments = this.state.comments.map(c => (
                <Comment content={c.content} onClick={() => this.upvote(c.id)} />
            ))
        }

        return (
            <div>
                {story}
                <form onSubmit={() => this.submitPost()}>
                    <textarea onChange={(e) => this.setState({comment: e.target.value})}>
                    {this.state.comment}
                    </textarea>
                    <input type="submit" value="Add comment"/>
                </form>
                <hr>
                {comments}
            </div>
        )
    }
}
```


