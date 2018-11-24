# JBL E50BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.3; 25 -1.0; 28 -1.7; 31 -2.3; 34 -2.7; 37 -2.9; 41 -3.0; 45 -3.0; 49 -3.1; 54 -3.1; 60 -3.0; 66 -2.9; 72 -2.7; 79 -2.5; 87 -2.3; 96 -2.3; 106 -2.3; 116 -2.3; 128 -2.3; 141 -2.1; 155 -1.8; 170 -1.3; 187 -0.8; 206 0.0; 227 1.2; 249 2.7; 274 4.7; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 5.6; 588 4.5; 647 3.6; 712 2.6; 783 1.4; 861 0.5; 947 0.0; 1042 0.1; 1146 -0.1; 1261 -0.7; 1387 -1.8; 1526 -2.8; 1678 -4.1; 1846 -3.9; 2031 -3.2; 2234 -2.2; 2457 -0.7; 2703 -0.2; 2973 0.5; 3270 2.3; 3597 4.5; 3957 4.2; 4353 1.0; 4788 0.7; 5267 3.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.0; 9330 -5.3; 10263 -3.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 425 Hz  | 1.37 | 7.1 dB  |
| Peaking | 1771 Hz | 2.09 | -4.6 dB |
| Peaking | 3676 Hz | 5.04 | 5.2 dB  |
| Peaking | 6090 Hz | 3.56 | 6.7 dB  |
| Peaking | 9279 Hz | 4.23 | -6.3 dB |
| Peaking | 45 Hz   | 1.04 | -2.6 dB |
| Peaking | 152 Hz  | 0.51 | -2.5 dB |
| Peaking | 295 Hz  | 2.21 | 4.9 dB  |
| Peaking | 424 Hz  | 1.41 | -2.1 dB |
| Peaking | 561 Hz  | 2.31 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20E50BT/JBL%20E50BT.png)