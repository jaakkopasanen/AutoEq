# AKG K240 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.5; 49 4.7; 54 3.8; 60 2.9; 66 2.0; 72 1.3; 79 0.6; 87 -0.1; 96 -0.9; 106 -1.7; 116 -2.3; 128 -2.8; 141 -3.3; 155 -3.5; 170 -3.5; 187 -3.4; 206 -3.0; 227 -2.9; 249 -2.8; 274 -2.8; 302 -2.8; 332 -2.7; 365 -2.5; 402 -2.4; 442 -2.2; 486 -1.1; 535 -0.3; 588 -0.7; 647 -0.6; 712 -0.4; 783 -0.4; 861 -0.3; 947 -0.1; 1042 0.3; 1146 0.9; 1261 1.2; 1387 1.5; 1526 1.8; 1678 1.4; 1846 0.9; 2031 0.1; 2234 -0.7; 2457 -1.0; 2703 -0.9; 2973 0.6; 3270 3.3; 3597 6.0; 3957 2.6; 4353 1.9; 4788 2.9; 5267 5.9; 5793 6.0; 6373 4.7; 7010 2.4; 7711 -0.4; 8482 -4.4; 9330 -6.3; 10263 -2.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.43 | 7.4 dB  |
| Peaking | 140 Hz  | 0.49 | -5.2 dB |
| Peaking | 5646 Hz | 0.66 | 3.2 dB  |
| Peaking | 5842 Hz | 3.33 | 3.9 dB  |
| Peaking | 9080 Hz | 3.19 | -8.9 dB |
| Peaking | 393 Hz  | 4.65 | -0.8 dB |
| Peaking | 1505 Hz | 1.89 | 1.9 dB  |
| Peaking | 2583 Hz | 2.2  | -3.1 dB |
| Peaking | 3561 Hz | 5.33 | 5.3 dB  |
| Peaking | 4222 Hz | 5.35 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/AKG%20K240%20MKII/AKG%20K240%20MKII.png)