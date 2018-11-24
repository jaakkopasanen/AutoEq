# Skullcandy Crusher

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.2; 34 4.6; 37 4.0; 41 3.6; 45 3.3; 49 3.1; 54 2.7; 60 2.5; 66 2.9; 72 3.4; 79 3.9; 87 4.2; 96 4.2; 106 3.9; 116 3.6; 128 3.5; 141 3.7; 155 3.9; 170 4.3; 187 4.5; 206 4.7; 227 5.0; 249 5.3; 274 5.5; 302 5.2; 332 4.9; 365 4.3; 402 3.2; 442 2.0; 486 1.0; 535 0.2; 588 -0.4; 647 -0.7; 712 -0.3; 783 0.8; 861 0.5; 947 -0.1; 1042 0.4; 1146 1.5; 1261 2.9; 1387 4.0; 1526 4.1; 1678 4.2; 1846 4.3; 2031 4.8; 2234 5.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 5.7; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.24 | 2.2 dB  |
| Peaking | 26 Hz   | 1.08 | 4.9 dB  |
| Peaking | 109 Hz  | 0.72 | 3.4 dB  |
| Peaking | 275 Hz  | 1.68 | 4.8 dB  |
| Peaking | 3319 Hz | 0.68 | 6.7 dB  |
| Peaking | 623 Hz  | 3.8  | -2.1 dB |
| Peaking | 1030 Hz | 3.28 | -2.4 dB |
| Peaking | 1349 Hz | 1.74 | 1.9 dB  |
| Peaking | 6050 Hz | 2.18 | 6.9 dB  |
| Peaking | 6735 Hz | 1.04 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Skullcandy%20Crusher/Skullcandy%20Crusher.png)