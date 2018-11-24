# JBL E55BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.6; 28 -2.9; 31 -3.0; 34 -3.1; 37 -3.1; 41 -3.1; 45 -3.0; 49 -3.0; 54 -3.0; 60 -3.1; 66 -3.1; 72 -2.9; 79 -2.8; 87 -3.0; 96 -3.4; 106 -3.9; 116 -4.2; 128 -4.2; 141 -4.0; 155 -3.3; 170 -2.4; 187 -1.2; 206 0.2; 227 2.2; 249 4.2; 274 5.9; 302 6.0; 332 6.0; 365 6.0; 402 5.7; 442 4.8; 486 3.8; 535 2.6; 588 1.4; 647 0.8; 712 0.4; 783 0.2; 861 0.1; 947 0.0; 1042 0.1; 1146 0.3; 1261 0.7; 1387 1.0; 1526 1.2; 1678 1.2; 1846 1.4; 2031 1.3; 2234 1.3; 2457 1.3; 2703 1.1; 2973 0.9; 3270 1.7; 3597 3.6; 3957 4.4; 4353 4.7; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.6; 9330 -1.9; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E55BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E55BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.53 | -2.9 dB |
| Peaking | 141 Hz  | 1.08 | -4.9 dB |
| Peaking | 315 Hz  | 1.22 | 7.9 dB  |
| Peaking | 5030 Hz | 1.75 | 6.6 dB  |
| Peaking | 466 Hz  | 3.22 | 1.6 dB  |
| Peaking | 765 Hz  | 0.81 | -1.2 dB |
| Peaking | 1623 Hz | 1.47 | 1.3 dB  |
| Peaking | 6368 Hz | 7.28 | 2.4 dB  |
| Peaking | 8806 Hz | 4.05 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20E55BT/JBL%20E55BT.png)