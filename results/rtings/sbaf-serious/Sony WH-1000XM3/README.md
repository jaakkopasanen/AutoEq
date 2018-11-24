# Sony WH-1000XM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 -6.4; 23 -6.4; 25 -6.4; 28 -6.5; 31 -6.5; 34 -6.5; 37 -6.5; 41 -6.4; 45 -6.4; 49 -6.3; 54 -6.3; 60 -6.4; 66 -6.5; 72 -6.6; 79 -6.7; 87 -6.9; 96 -7.1; 106 -7.3; 116 -7.4; 128 -7.3; 141 -6.9; 155 -6.2; 170 -5.4; 187 -4.5; 206 -3.6; 227 -2.8; 249 -1.9; 274 -1.3; 302 -0.8; 332 -0.5; 365 -0.3; 402 -0.3; 442 -0.4; 486 -0.6; 535 -0.8; 588 -0.9; 647 -1.0; 712 -0.2; 783 -0.5; 861 -0.7; 947 -0.3; 1042 0.2; 1146 0.8; 1261 0.5; 1387 -0.2; 1526 -2.6; 1678 -3.3; 1846 -3.2; 2031 -3.3; 2234 -2.9; 2457 -1.0; 2703 0.8; 2973 1.5; 3270 2.8; 3597 3.1; 3957 1.7; 4353 2.0; 4788 4.1; 5267 3.2; 5793 4.4; 6373 2.9; 7010 2.4; 7711 -0.7; 8482 -4.5; 9330 -5.5; 10263 -2.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-1000XM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.33 | -6.4 dB |
| Peaking | 127 Hz  | 1.14 | -5.1 dB |
| Peaking | 1951 Hz | 2.35 | -4.9 dB |
| Peaking | 6037 Hz | 0.66 | 5.0 dB  |
| Peaking | 9005 Hz | 2.57 | -9.5 dB |
| Peaking | 344 Hz  | 1.66 | 1.4 dB  |
| Peaking | 928 Hz  | 0.21 | -0.8 dB |
| Peaking | 1191 Hz | 3.56 | 2.0 dB  |
| Peaking | 3726 Hz | 1.8  | 2.3 dB  |
| Peaking | 4170 Hz | 5.69 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WH-1000XM3/Sony%20WH-1000XM3.png)