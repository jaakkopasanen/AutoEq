# JBL E55BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.5; 23 -2.7; 25 -2.8; 28 -3.0; 31 -3.1; 34 -3.1; 37 -3.0; 41 -2.9; 45 -2.8; 49 -2.6; 54 -2.6; 60 -2.8; 66 -2.9; 72 -2.9; 79 -3.0; 87 -3.3; 96 -3.8; 106 -4.4; 116 -4.7; 128 -4.8; 141 -4.5; 155 -3.9; 170 -3.0; 187 -1.8; 206 -0.3; 227 1.7; 249 3.7; 274 5.6; 302 6.0; 332 6.0; 365 5.8; 402 4.6; 442 3.7; 486 2.6; 535 1.4; 588 0.3; 647 -0.3; 712 -0.4; 783 -0.3; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.1; 1261 0.5; 1387 1.1; 1526 1.5; 1678 1.6; 1846 1.3; 2031 0.9; 2234 0.8; 2457 0.9; 2703 0.5; 2973 -0.2; 3270 -0.2; 3597 1.4; 3957 3.2; 4353 4.6; 4788 6.0; 5267 5.7; 5793 5.7; 6373 4.8; 7010 2.5; 7711 0.3; 8482 -2.0; 9330 -3.4; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E55BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E55BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.56 | -2.8 dB |
| Peaking | 136 Hz  | 0.98 | -5.4 dB |
| Peaking | 308 Hz  | 1.53 | 8.0 dB  |
| Peaking | 5380 Hz | 1.72 | 6.6 dB  |
| Peaking | 9057 Hz | 3.83 | -4.9 dB |
| Peaking | 459 Hz  | 2.47 | 1.8 dB  |
| Peaking | 621 Hz  | 1.29 | -1.7 dB |
| Peaking | 1627 Hz | 2.59 | 1.5 dB  |
| Peaking | 3204 Hz | 5.05 | -2.0 dB |
| Peaking | 4271 Hz | 4.9  | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/JBL%20E55BT/JBL%20E55BT.png)