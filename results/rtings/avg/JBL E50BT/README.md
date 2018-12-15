# JBL E50BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.0; 23 -0.7; 25 -1.2; 28 -1.9; 31 -2.4; 34 -2.7; 37 -2.8; 41 -2.8; 45 -2.7; 49 -2.7; 54 -2.8; 60 -2.8; 66 -2.8; 72 -2.7; 79 -2.7; 87 -2.7; 96 -2.7; 106 -2.7; 116 -2.8; 128 -2.8; 141 -2.6; 155 -2.4; 170 -2.0; 187 -1.4; 206 -0.5; 227 0.7; 249 2.2; 274 4.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 5.2; 535 4.4; 588 3.5; 647 2.6; 712 1.8; 783 1.0; 861 0.3; 947 0.0; 1042 0.0; 1146 -0.3; 1261 -1.0; 1387 -1.8; 1526 -2.4; 1678 -3.7; 1846 -3.9; 2031 -3.6; 2234 -2.7; 2457 -1.2; 2703 -1.1; 2973 -1.0; 3270 -0.3; 3597 1.3; 3957 1.8; 4353 -0.4; 4788 -0.9; 5267 0.3; 5793 3.3; 6373 4.3; 7010 2.4; 7711 -0.8; 8482 -4.0; 9330 -5.5; 10263 -4.7; 11289 -3.1; 12418 -1.5; 13660 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 144 Hz  | 0.27 | -4.3 dB |
| Peaking | 369 Hz  | 0.98 | 9.9 dB  |
| Peaking | 1811 Hz | 2.06 | -4.3 dB |
| Peaking | 6400 Hz | 3.53 | 5.9 dB  |
| Peaking | 9450 Hz | 2.22 | -6.3 dB |
| Peaking | 34 Hz   | 3.07 | -0.8 dB |
| Peaking | 188 Hz  | 3.19 | -0.7 dB |
| Peaking | 294 Hz  | 9.71 | 1.5 dB  |
| Peaking | 3857 Hz | 6.17 | 2.7 dB  |
| Peaking | 4641 Hz | 6.22 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E50BT/JBL%20E50BT.png)