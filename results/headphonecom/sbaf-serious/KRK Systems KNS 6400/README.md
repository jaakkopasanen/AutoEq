# KRK Systems KNS 6400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.8; 25 4.5; 28 4.2; 31 3.9; 34 3.8; 37 3.7; 41 3.5; 45 3.8; 49 4.8; 54 5.4; 60 5.9; 66 6.0; 72 5.9; 79 4.0; 87 2.0; 96 0.8; 106 -0.0; 116 -0.7; 128 -1.5; 141 -2.2; 155 -1.7; 170 -2.0; 187 -3.7; 206 -4.5; 227 -4.4; 249 -3.3; 274 -3.8; 302 -3.9; 332 -4.0; 365 -3.5; 402 -2.5; 442 -1.5; 486 -1.0; 535 -1.2; 588 -2.0; 647 -1.9; 712 -0.1; 783 0.0; 861 -0.6; 947 -0.1; 1042 -0.0; 1146 -0.6; 1261 -0.9; 1387 -0.7; 1526 -1.1; 1678 -1.3; 1846 -2.8; 2031 -3.7; 2234 -3.5; 2457 -3.9; 2703 -3.4; 2973 -1.0; 3270 -1.1; 3597 2.0; 3957 1.1; 4353 0.5; 4788 2.4; 5267 3.2; 5793 1.1; 6373 -1.8; 7010 -1.0; 7711 0.3; 8482 -0.1; 9330 -2.8; 10263 -1.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.4; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 6400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.57 | 5.1 dB  |
| Peaking | 67 Hz   | 1.49 | 7.1 dB  |
| Peaking | 94 Hz   | 0.93 | -2.1 dB |
| Peaking | 252 Hz  | 0.91 | -4.3 dB |
| Peaking | 2234 Hz | 2.7  | -4.3 dB |
| Peaking | 2704 Hz | 6.31 | -2.0 dB |
| Peaking | 5345 Hz | 6.02 | 2.4 dB  |
| Peaking | 5403 Hz | 0.97 | 2.1 dB  |
| Peaking | 6411 Hz | 4.81 | -4.2 dB |
| Peaking | 9600 Hz | 5.96 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)