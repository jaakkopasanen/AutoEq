# JBL E45BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.2; 23 -1.3; 25 -1.5; 28 -1.6; 31 -1.7; 34 -1.8; 37 -1.9; 41 -2.0; 45 -2.0; 49 -2.0; 54 -2.2; 60 -2.5; 66 -2.8; 72 -3.0; 79 -3.0; 87 -3.0; 96 -2.8; 106 -2.7; 116 -2.5; 128 -2.4; 141 -2.2; 155 -2.1; 170 -1.9; 187 -1.7; 206 -1.4; 227 -0.7; 249 0.8; 274 2.6; 302 4.1; 332 5.3; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 5.9; 647 5.2; 712 3.5; 783 2.1; 861 1.0; 947 0.2; 1042 0.0; 1146 0.3; 1261 0.5; 1387 0.3; 1526 -0.3; 1678 0.1; 1846 1.9; 2031 1.8; 2234 1.6; 2457 1.2; 2703 0.3; 2973 -1.2; 3270 -2.0; 3597 -2.0; 3957 -1.9; 4353 -0.6; 4788 3.3; 5267 3.1; 5793 3.1; 6373 0.4; 7010 -2.2; 7711 -1.0; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E45BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E45BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 90 Hz   | 0.42 | -3.2 dB |
| Peaking | 207 Hz  | 2.46 | -2.0 dB |
| Peaking | 416 Hz  | 0.97 | 7.6 dB  |
| Peaking | 3813 Hz | 2.86 | -3.1 dB |
| Peaking | 5084 Hz | 4.24 | 4.8 dB  |
| Peaking | 463 Hz  | 2.88 | -2.2 dB |
| Peaking | 612 Hz  | 1.32 | 3.8 dB  |
| Peaking | 855 Hz  | 1.15 | -3.1 dB |
| Peaking | 2083 Hz | 3.35 | 2.2 dB  |
| Peaking | 7087 Hz | 8.54 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20E45BT/JBL%20E45BT.png)