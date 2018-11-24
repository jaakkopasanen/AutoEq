# JBL E45BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -1.6; 25 -1.7; 28 -1.8; 31 -1.8; 34 -1.8; 37 -1.8; 41 -1.8; 45 -1.8; 49 -1.7; 54 -1.8; 60 -2.2; 66 -2.6; 72 -3.0; 79 -3.2; 87 -3.3; 96 -3.3; 106 -3.2; 116 -3.1; 128 -2.9; 141 -2.8; 155 -2.7; 170 -2.6; 187 -2.3; 206 -1.9; 227 -1.2; 249 0.3; 274 1.9; 302 3.3; 332 4.4; 365 5.6; 402 6.0; 442 6.0; 486 5.8; 535 5.3; 588 4.8; 647 4.2; 712 2.6; 783 1.7; 861 0.8; 947 0.2; 1042 -0.0; 1146 0.1; 1261 0.3; 1387 0.3; 1526 0.1; 1678 0.5; 1846 1.9; 2031 1.4; 2234 1.1; 2457 0.7; 2703 -0.5; 2973 -2.8; 3270 -4.6; 3597 -5.2; 3957 -4.4; 4353 -1.9; 4788 1.7; 5267 0.2; 5793 -0.9; 6373 -3.4; 7010 -5.4; 7711 -2.6; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.7; 15026 -1.5; 16529 -2.4; 18182 -3.3; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E45BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E45BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 172 Hz   | 0.31 | -4.5 dB |
| Peaking | 416 Hz   | 0.98 | 9.7 dB  |
| Peaking | 3541 Hz  | 4.17 | -5.6 dB |
| Peaking | 18686 Hz | 1.57 | -2.8 dB |
| Peaking | 19250 Hz | 0.1  | -0.9 dB |
| Peaking | 1007 Hz  | 3.44 | -1.2 dB |
| Peaking | 2015 Hz  | 3.59 | 2.0 dB  |
| Peaking | 4907 Hz  | 8.59 | 3.3 dB  |
| Peaking | 6954 Hz  | 4.66 | -5.8 dB |
| Peaking | 9315 Hz  | 1.46 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E45BT/JBL%20E45BT.png)