# Cowin E7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.4; 23 -0.8; 25 -0.3; 28 0.2; 31 0.5; 34 0.9; 37 1.1; 41 1.3; 45 1.4; 49 1.4; 54 1.3; 60 1.1; 66 0.8; 72 0.4; 79 0.1; 87 -0.2; 96 -0.7; 106 -1.1; 116 -1.5; 128 -1.9; 141 -2.3; 155 -2.6; 170 -2.9; 187 -3.1; 206 -3.2; 227 -3.4; 249 -3.4; 274 -3.4; 302 -3.7; 332 -3.8; 365 -3.5; 402 -3.4; 442 -3.2; 486 -2.9; 535 -2.6; 588 -2.3; 647 -2.1; 712 -1.9; 783 -1.6; 861 -0.1; 947 0.4; 1042 -0.5; 1146 -0.0; 1261 2.1; 1387 4.1; 1526 5.8; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.0; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.19 | -2.7 dB |
| Peaking | 54 Hz   | 0.59 | 3.0 dB  |
| Peaking | 362 Hz  | 0.21 | -4.2 dB |
| Peaking | 2005 Hz | 0.76 | 8.0 dB  |
| Peaking | 4988 Hz | 1.69 | 4.7 dB  |
| Peaking | 1119 Hz | 8.01 | -1.9 dB |
| Peaking | 1506 Hz | 6.16 | 1.4 dB  |
| Peaking | 6215 Hz | 5.31 | 2.8 dB  |
| Peaking | 8116 Hz | 1.57 | -2.1 dB |
| Peaking | 9023 Hz | 2.61 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Cowin%20E7/Cowin%20E7.png)