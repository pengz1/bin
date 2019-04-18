package main

import (
	"encoding/json"
	"flag"
	"fmt"
	// "io/ioutil"
	"log"
	"net/http"
	// "os"
	// "strings"
	// "time"
)

var shouldExit bool

func home(response http.ResponseWriter, request *http.Request) {
	fmt.Fprint(response, "<html><head><title>Asaka Exporter</title></head><body><h1>Asaka Exporter</h1><p><a href=\"/metrics\">Metrics</a></p></body></html>")
}

func exit(response http.ResponseWriter, request *http.Request) {
	shouldExit = true
	fmt.Fprint(response, "exiting")
}

func hello(w http.ResponseWriter, r *http.Request) {
	// if r.URL.Path != "/" {
	// http.Error(w, "404 not found.", http.StatusNotFound)
	// return
	// }

	switch r.Method {
	case "GET":
		fmt.Println("GET")
	case "POST":
		fmt.Println("POST")
		// Call ParseForm() to parse the raw query and update r.PostForm and r.Form.
		if err := r.ParseForm(); err != nil {
			fmt.Fprintf(w, "ParseForm() err: %v", err)
			return
		}
		var objmap map[string]interface{}
		if err := json.Unmarshal(r.Body, &objmap); err != nil {
			fmt.Println(objmap) // to parse out your value
		}
		fmt.Fprintf(w, "Post from website! r.PostFrom = %v\n", r.PostForm)
		name := r.FormValue("name")
		address := r.FormValue("address")
		fmt.Fprintf(w, "Name = %s\n", name)
		fmt.Fprintf(w, "Address = %s\n", address)
	default:
		fmt.Fprintf(w, "Sorry, only GET and POST methods are supported.")
	}
}

func main() {
	shouldExit = false
	addr := flag.String("p", "8080", "Http server accessing port")
	// asakaUrl := flag.String("a", "localhost:9527", "Asaka dashboard API address ")

	flag.Parse()
	*addr = ":" + *addr
	http.HandleFunc("/bitbucket-hook", hello)
	http.HandleFunc("/", home)
	http.HandleFunc("/exit", exit)

	log.Printf("I-Listen port http://0.0.0.0%s\n", *addr)
	// log.Printf("Asaka querying address http://%s\n", *asakaUrl)

	err := http.ListenAndServe(*addr, nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
