# Koss UR-20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.1; 28 1.5; 31 1.1; 34 0.9; 37 0.8; 41 0.8; 45 0.7; 49 0.6; 54 0.5; 60 0.2; 66 0.1; 72 0.1; 79 0.1; 87 -0.1; 96 -0.4; 106 -0.9; 116 -1.3; 128 -1.7; 141 -2.0; 155 -2.1; 170 -2.0; 187 -2.2; 206 -2.1; 227 -1.9; 249 -1.4; 274 -1.5; 302 -1.6; 332 -1.9; 365 -2.3; 402 -2.7; 442 -3.1; 486 -3.2; 535 -2.7; 588 -2.2; 647 -1.9; 712 -1.4; 783 -0.5; 861 0.5; 947 -0.4; 1042 0.9; 1146 3.3; 1261 5.7; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.9; 3957 0.6; 4353 -1.9; 4788 0.7; 5267 3.2; 5793 1.1; 6373 -0.1; 7010 0.7; 7711 -4.0; 8482 -7.6; 9330 -3.8; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR-20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR-20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.73 | 4.7 dB  |
| Peaking | 156 Hz  | 1.54 | -1.8 dB |
| Peaking | 598 Hz  | 0.69 | -4.3 dB |
| Peaking | 1819 Hz | 0.67 | 7.7 dB  |
| Peaking | 8475 Hz | 4.98 | -9.0 dB |
| Peaking | 1021 Hz | 4.43 | -3.5 dB |
| Peaking | 1210 Hz | 1.44 | 3.6 dB  |
| Peaking | 1777 Hz | 0.91 | -2.6 dB |
| Peaking | 3797 Hz | 1.67 | 5.4 dB  |
| Peaking | 4207 Hz | 4.66 | -9.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Koss%20UR-20/Koss%20UR-20.png)