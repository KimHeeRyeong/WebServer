using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;
[System.Serializable]
public class Start {
    public int coin;
    public int nowLevel;
    public int strengthCoin;
    public int sellCoin;
}
[System.Serializable]
public class Strength
{
    public bool result;
    public int coin;
    public int nowLevel;
    public int strengthCoin;
    public int sellCoin;
}
[System.Serializable]
public class Sell
{
    public int coin;
    public int nowLevel;
    public int strengthCoin;
    public int sellCoin;
}
public class WeaponStrength : MonoBehaviour
{
    public Text coin;
    public Text context;
    public Text strengthText;
    public Text sellText;

    void Start()
    {
        StartCoroutine(SendStart());
    }
    IEnumerator SendStart()
    {
        UnityWebRequest www = UnityWebRequest.Get("http://localhost:10000/start");
        yield return www.SendWebRequest();
        
        string json = www.downloadHandler.text;
        Sell start = JsonUtility.FromJson<Sell>(json);
        coin.text = "코인 : "+start.coin.ToString();
        context.text = "강화하시겠습니까? ("+start.nowLevel.ToString()+"->"+(start.nowLevel+1).ToString()+")";
        strengthText.text = "강화(" + start.strengthCoin.ToString() + "코인)";
        sellText.text = "판매(" + start.sellCoin.ToString() + "코인)";
    }
    IEnumerator SendStrength()
    {
        UnityWebRequest www = UnityWebRequest.Get("http://localhost:10000/strength");
        yield return www.SendWebRequest();
        string json = www.downloadHandler.text;
        Debug.Log(json);
        Strength strength = JsonUtility.FromJson<Strength>(json);
        coin.text = "코인 : " + strength.coin.ToString();
        if(!strength.result)
            context.text = "강화 실패! 강화하시겠습니까? (" + strength.nowLevel.ToString() + "->" + (strength.nowLevel + 1).ToString() + ")";
        else
            context.text = "강화 성공! 강화하시겠습니까? (" + strength.nowLevel.ToString() + "->" + (strength.nowLevel + 1).ToString() + ")";
        strengthText.text = "강화(" + strength.strengthCoin.ToString() + "코인)";
        sellText.text = "판매(" + strength.sellCoin.ToString() + "코인)";
    }
    IEnumerator SendSell()
    {
        UnityWebRequest www = UnityWebRequest.Get("http://localhost:10000/sell");
        yield return www.SendWebRequest();
        string json = www.downloadHandler.text;
        Sell sell = JsonUtility.FromJson<Sell>(json);
        coin.text = "코인 : " + sell.coin.ToString();
        context.text = "판매 완료! 강화하시겠습니까? (" + sell.nowLevel.ToString() + "->" + (sell.nowLevel + 1).ToString() + ")";
        strengthText.text = "강화(" + sell.strengthCoin.ToString() + "코인)";
        sellText.text = "판매(" + sell.sellCoin.ToString() + "코인)";
    }
    public void StrengthButtonClick() {
        StartCoroutine(SendStrength());
    }
    public void SellButtonClick() {
        StartCoroutine(SendSell());
    }
}
