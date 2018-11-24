# AKG K272HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.6; 54 4.8; 60 3.3; 66 2.0; 72 1.3; 79 1.4; 87 2.1; 96 3.0; 106 2.1; 116 0.3; 128 -0.8; 141 -1.5; 155 -2.0; 170 -1.4; 187 -0.9; 206 -0.5; 227 -0.7; 249 -0.7; 274 -0.9; 302 -0.8; 332 -0.8; 365 -1.1; 402 -1.4; 442 -1.5; 486 -1.5; 535 -1.7; 588 -2.2; 647 -3.4; 712 -0.9; 783 0.2; 861 0.6; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -2.3; 1526 -3.5; 1678 -4.1; 1846 -3.4; 2031 0.3; 2234 3.2; 2457 3.7; 2703 2.9; 2973 2.8; 3270 2.8; 3597 4.2; 3957 4.8; 4353 4.0; 4788 4.7; 5267 6.0; 5793 6.0; 6373 3.3; 7010 2.4; 7711 0.3; 8482 -2.7; 9330 -6.8; 10263 -3.8; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K272HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.86 | 6.9 dB  |
| Peaking | 1822 Hz | 1.79 | -8.4 dB |
| Peaking | 2209 Hz | 2.36 | 7.5 dB  |
| Peaking | 5170 Hz | 1    | 5.9 dB  |
| Peaking | 9303 Hz | 3.73 | -9.1 dB |
| Peaking | 100 Hz  | 5.13 | 2.6 dB  |
| Peaking | 147 Hz  | 2.22 | -2.3 dB |
| Peaking | 505 Hz  | 1.02 | -1.9 dB |
| Peaking | 663 Hz  | 4.8  | -4.2 dB |
| Peaking | 747 Hz  | 1.76 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)