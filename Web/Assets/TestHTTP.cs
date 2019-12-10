using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class TestHTTP : MonoBehaviour
{
    Text text;
    // Start is called before the first frame update
    void Start()
    {
        text = this.GetComponent<Text>();
        StartCoroutine(SendHTTP());
    }

    IEnumerator SendHTTP() {
        UnityWebRequest www = UnityWebRequest.Get("http://localhost:10000/hello/sdfa/123");
        yield return www.SendWebRequest();
        string hi = www.downloadHandler.text;
        text.text = hi;
    }
}
