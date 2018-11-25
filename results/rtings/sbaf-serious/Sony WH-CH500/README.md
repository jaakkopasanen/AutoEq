# Sony WH-CH500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.5; 34 4.0; 37 2.2; 41 0.1; 45 -1.5; 49 -2.8; 54 -3.9; 60 -4.8; 66 -5.4; 72 -5.5; 79 -5.3; 87 -4.9; 96 -4.3; 106 -3.7; 116 -3.1; 128 -2.5; 141 -1.8; 155 -1.1; 170 -0.5; 187 -0.1; 206 0.4; 227 0.6; 249 1.0; 274 1.3; 302 1.5; 332 1.7; 365 1.9; 402 2.4; 442 2.4; 486 2.0; 535 1.5; 588 1.2; 647 1.5; 712 1.5; 783 1.1; 861 0.6; 947 0.1; 1042 0.1; 1146 0.3; 1261 -0.0; 1387 -0.4; 1526 -0.8; 1678 -0.7; 1846 -0.0; 2031 0.6; 2234 1.5; 2457 2.0; 2703 1.9; 2973 1.6; 3270 2.4; 3597 3.3; 3957 5.1; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.1; 8482 -2.9; 9330 -5.4; 10263 -1.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.92 | 8.7 dB  |
| Peaking | 65 Hz   | 0.8  | -7.6 dB |
| Peaking | 362 Hz  | 0.87 | 2.5 dB  |
| Peaking | 5205 Hz | 1.26 | 7.0 dB  |
| Peaking | 9125 Hz | 3.5  | -7.3 dB |
| Peaking | 714 Hz  | 5.11 | 0.7 dB  |
| Peaking | 966 Hz  | 6.3  | -0.5 dB |
| Peaking | 1589 Hz | 2.86 | -1.8 dB |
| Peaking | 1599 Hz | 2.97 | 0.3 dB  |
| Peaking | 2365 Hz | 6.15 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WH-CH500/Sony%20WH-CH500.png)