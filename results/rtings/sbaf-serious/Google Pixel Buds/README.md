# Google Pixel Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.3; 49 3.8; 54 2.2; 60 0.6; 66 -0.5; 72 -1.4; 79 -2.2; 87 -3.1; 96 -3.9; 106 -4.7; 116 -5.3; 128 -5.8; 141 -6.1; 155 -6.2; 170 -6.1; 187 -6.1; 206 -6.0; 227 -5.7; 249 -5.2; 274 -4.6; 302 -3.8; 332 -3.1; 365 -2.4; 402 -2.0; 442 -1.9; 486 -1.7; 535 -1.7; 588 -1.6; 647 -1.4; 712 -1.2; 783 -1.1; 861 -0.9; 947 -0.4; 1042 0.4; 1146 1.4; 1261 2.5; 1387 3.0; 1526 3.3; 1678 3.8; 1846 4.4; 2031 4.5; 2234 4.1; 2457 2.5; 2703 0.9; 2973 -0.3; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -1.9; 4788 -1.4; 5267 -0.4; 5793 1.4; 6373 2.7; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -0.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Google Pixel Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Google Pixel Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.66 | 8.0 dB  |
| Peaking | 140 Hz  | 0.53 | -7.3 dB |
| Peaking | 1908 Hz | 0.98 | 9.4 dB  |
| Peaking | 2596 Hz | 0.43 | -5.0 dB |
| Peaking | 6493 Hz | 3.67 | 5.1 dB  |
| Peaking | 401 Hz  | 3.52 | 0.8 dB  |
| Peaking | 1035 Hz | 0.99 | -0.7 dB |
| Peaking | 1244 Hz | 3.74 | 1.4 dB  |
| Peaking | 8754 Hz | 6.59 | -2.2 dB |
| Peaking | 9976 Hz | 1.37 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Google%20Pixel%20Buds/Google%20Pixel%20Buds.png)