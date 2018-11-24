# Anker Soundcore Spirit X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 -4.7; 23 -4.7; 25 -4.8; 28 -4.8; 31 -4.8; 34 -4.8; 37 -4.8; 41 -4.7; 45 -4.6; 49 -4.5; 54 -4.4; 60 -4.3; 66 -4.2; 72 -4.0; 79 -3.8; 87 -3.6; 96 -3.4; 106 -3.5; 116 -3.4; 128 -3.3; 141 -3.1; 155 -2.8; 170 -2.5; 187 -1.8; 206 -0.9; 227 0.2; 249 1.2; 274 1.8; 302 1.7; 332 1.3; 365 0.8; 402 0.4; 442 0.3; 486 0.4; 535 0.6; 588 0.9; 647 1.4; 712 1.7; 783 1.6; 861 1.2; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -1.6; 1387 -2.3; 1526 -2.8; 1678 -3.0; 1846 -2.6; 2031 -2.2; 2234 -1.5; 2457 -0.7; 2703 -0.3; 2973 -0.3; 3270 -0.2; 3597 -0.3; 3957 -1.8; 4353 -3.6; 4788 -3.6; 5267 -2.9; 5793 -2.4; 6373 -0.7; 7010 2.0; 7711 0.3; 8482 -1.1; 9330 -4.2; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker Soundcore Spirit X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker Soundcore Spirit X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.14 | -4.9 dB |
| Peaking | 322 Hz  | 0.58 | 3.7 dB  |
| Peaking | 1629 Hz | 2.14 | -3.4 dB |
| Peaking | 4734 Hz | 3.56 | -4.1 dB |
| Peaking | 9291 Hz | 8.34 | -4.5 dB |
| Peaking | 177 Hz  | 2.3  | -1.3 dB |
| Peaking | 281 Hz  | 1.5  | 2.5 dB  |
| Peaking | 394 Hz  | 1.24 | -2.1 dB |
| Peaking | 742 Hz  | 3.09 | 1.6 dB  |
| Peaking | 6999 Hz | 9.48 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Anker%20Soundcore%20Spirit%20X/Anker%20Soundcore%20Spirit%20X.png)