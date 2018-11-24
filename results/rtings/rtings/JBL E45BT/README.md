# JBL E45BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -1.6; 25 -1.7; 28 -1.8; 31 -1.8; 34 -1.8; 37 -1.8; 41 -1.8; 45 -1.8; 49 -1.7; 54 -1.8; 60 -2.2; 66 -2.6; 72 -3.0; 79 -3.2; 87 -3.3; 96 -3.3; 106 -3.2; 116 -3.1; 128 -2.9; 141 -2.8; 155 -2.7; 170 -2.6; 187 -2.3; 206 -1.9; 227 -1.2; 249 0.3; 274 1.9; 302 3.3; 332 4.4; 365 5.6; 402 6.0; 442 6.0; 486 5.8; 535 5.3; 588 4.8; 647 4.2; 712 2.6; 783 1.7; 861 0.8; 947 0.2; 1042 -0.0; 1146 0.1; 1261 0.3; 1387 0.3; 1526 0.1; 1678 0.5; 1846 1.9; 2031 1.4; 2234 1.1; 2457 0.7; 2703 -0.3; 2973 -2.3; 3270 -3.9; 3597 -4.2; 3957 -3.1; 4353 -0.6; 4788 3.5; 5267 2.7; 5793 1.6; 6373 -2.1; 7010 -4.7; 7711 -2.1; 8482 0.0
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 182 Hz  | 0.3  | -4.7 dB |
| Peaking | 418 Hz  | 0.97 | 10.0 dB |
| Peaking | 3683 Hz | 2.97 | -6.5 dB |
| Peaking | 5076 Hz | 1.85 | 5.1 dB  |
| Peaking | 6890 Hz | 4.54 | -6.7 dB |
| Peaking | 23 Hz   | 1.79 | -0.9 dB |
| Peaking | 213 Hz  | 7.39 | -0.8 dB |
| Peaking | 636 Hz  | 4.25 | 1.4 dB  |
| Peaking | 959 Hz  | 1.34 | -1.0 dB |
| Peaking | 1988 Hz | 3.32 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/JBL%20E45BT/JBL%20E45BT.png)