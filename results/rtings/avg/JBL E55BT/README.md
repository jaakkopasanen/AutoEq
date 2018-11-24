# JBL E55BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.5; 23 -2.7; 25 -2.8; 28 -3.0; 31 -3.1; 34 -3.1; 37 -3.0; 41 -2.9; 45 -2.8; 49 -2.6; 54 -2.6; 60 -2.8; 66 -2.9; 72 -2.9; 79 -3.0; 87 -3.3; 96 -3.8; 106 -4.4; 116 -4.7; 128 -4.8; 141 -4.5; 155 -3.9; 170 -3.0; 187 -1.8; 206 -0.3; 227 1.7; 249 3.7; 274 5.6; 302 6.0; 332 6.0; 365 5.8; 402 4.6; 442 3.7; 486 2.6; 535 1.4; 588 0.3; 647 -0.3; 712 -0.4; 783 -0.3; 861 -0.1; 947 -0.0; 1042 0.1; 1146 0.1; 1261 0.5; 1387 1.1; 1526 1.5; 1678 1.6; 1846 1.3; 2031 0.9; 2234 0.8; 2457 0.8; 2703 0.3; 2973 -0.7; 3270 -0.9; 3597 0.4; 3957 2.0; 4353 3.3; 4788 4.9; 5267 3.3; 5793 3.2; 6373 3.6; 7010 2.5; 7711 0.3; 8482 -1.1; 9330 -0.8; 10263 0.0; 11289 0.0; 12418 -0.5; 13660 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E55BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E55BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.56 | -2.8 dB |
| Peaking | 135 Hz  | 0.98 | -5.3 dB |
| Peaking | 309 Hz  | 1.56 | 8.1 dB  |
| Peaking | 1657 Hz | 3.91 | 1.6 dB  |
| Peaking | 5114 Hz | 2.33 | 4.5 dB  |
| Peaking | 459 Hz  | 2.69 | 1.7 dB  |
| Peaking | 633 Hz  | 1.38 | -1.6 dB |
| Peaking | 3225 Hz | 4.34 | -2.6 dB |
| Peaking | 3814 Hz | 0.52 | 0.7 dB  |
| Peaking | 8764 Hz | 5.56 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E55BT/JBL%20E55BT.png)