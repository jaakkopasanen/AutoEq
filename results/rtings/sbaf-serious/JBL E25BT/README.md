# JBL E25BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -2.7; 23 -3.1; 25 -3.5; 28 -3.9; 31 -4.2; 34 -4.5; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.4; 54 -5.7; 60 -6.1; 66 -6.4; 72 -6.5; 79 -6.7; 87 -6.9; 96 -7.3; 106 -7.7; 116 -8.0; 128 -8.4; 141 -8.6; 155 -8.7; 170 -8.6; 187 -8.5; 206 -8.4; 227 -8.1; 249 -7.5; 274 -6.8; 302 -6.0; 332 -5.3; 365 -4.8; 402 -4.1; 442 -3.3; 486 -2.4; 535 -1.6; 588 -0.8; 647 0.1; 712 0.9; 783 1.5; 861 1.6; 947 0.7; 1042 -0.5; 1146 -1.2; 1261 -1.6; 1387 -2.0; 1526 -2.0; 1678 -1.8; 1846 -1.4; 2031 -1.2; 2234 -0.6; 2457 -0.2; 2703 -0.4; 2973 -1.2; 3270 -1.6; 3597 -1.6; 3957 -2.4; 4353 -3.7; 4788 -3.5; 5267 -2.9; 5793 -4.0; 6373 -6.6; 7010 -4.6; 7711 -1.6; 8482 -2.7; 9330 -6.9; 10263 -5.6; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 -1.6; 16529 -5.0; 18182 -3.4; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E25BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E25BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.37 | -5.6 dB |
| Peaking | 203 Hz   | 0.87 | -5.9 dB |
| Peaking | 6687 Hz  | 0.84 | -4.6 dB |
| Peaking | 16887 Hz | 3.36 | -4.7 dB |
| Peaking | 20614 Hz | 1.59 | -4.0 dB |
| Peaking | 802 Hz   | 2.79 | 3.0 dB  |
| Peaking | 1409 Hz  | 2.47 | -1.9 dB |
| Peaking | 8059 Hz  | 6.5  | 4.4 dB  |
| Peaking | 9827 Hz  | 3.38 | -7.2 dB |
| Peaking | 11295 Hz | 2.31 | 4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20E25BT/JBL%20E25BT.png)