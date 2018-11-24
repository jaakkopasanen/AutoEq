# Cowin E7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -0.5; 25 -0.1; 28 0.3; 31 0.6; 34 0.8; 37 1.0; 41 1.1; 45 1.1; 49 1.0; 54 0.9; 60 0.8; 66 0.6; 72 0.4; 79 0.3; 87 0.1; 96 -0.2; 106 -0.6; 116 -1.0; 128 -1.4; 141 -1.7; 155 -2.0; 170 -2.2; 187 -2.5; 206 -2.7; 227 -2.9; 249 -2.9; 274 -2.7; 302 -2.9; 332 -2.8; 365 -2.5; 402 -2.3; 442 -2.1; 486 -1.7; 535 -1.4; 588 -1.2; 647 -1.1; 712 -1.1; 783 -1.1; 861 0.1; 947 0.4; 1042 -0.4; 1146 0.2; 1261 2.3; 1387 4.1; 1526 5.6; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.34 | -2.2 dB |
| Peaking | 59 Hz   | 0.51 | 2.2 dB  |
| Peaking | 312 Hz  | 0.29 | -3.7 dB |
| Peaking | 1086 Hz | 4.72 | -3.0 dB |
| Peaking | 2447 Hz | 0.46 | 7.4 dB  |
| Peaking | 772 Hz  | 8.48 | -1.1 dB |
| Peaking | 1587 Hz | 4.79 | 1.3 dB  |
| Peaking | 2626 Hz | 2.26 | -0.9 dB |
| Peaking | 6202 Hz | 1.91 | 6.1 dB  |
| Peaking | 7467 Hz | 1.38 | -5.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Cowin%20E7/Cowin%20E7.png)