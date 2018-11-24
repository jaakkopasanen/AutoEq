# House of Marley Stir It Up

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.0; 23 -1.2; 25 -1.5; 28 -1.8; 31 -2.0; 34 -2.2; 37 -2.3; 41 -2.4; 45 -2.3; 49 -2.1; 54 -1.9; 60 -2.2; 66 -2.7; 72 -3.0; 79 -3.2; 87 -3.6; 96 -4.1; 106 -4.1; 116 -4.0; 128 -4.2; 141 -4.0; 155 -3.6; 170 -3.3; 187 -3.0; 206 -2.6; 227 -1.9; 249 -1.4; 274 -1.0; 302 -0.8; 332 -0.9; 365 -1.1; 402 -1.6; 442 -2.7; 486 -3.5; 535 -3.5; 588 -3.3; 647 -3.1; 712 -2.8; 783 -2.1; 861 -1.5; 947 -0.7; 1042 0.4; 1146 1.4; 1261 2.0; 1387 2.9; 1526 3.6; 1678 4.3; 1846 5.4; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.2; 4788 3.0; 5267 4.8; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Stir It Up GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Stir It Up ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.92 | -1.7 dB |
| Peaking | 118 Hz  | 0.92 | -4.1 dB |
| Peaking | 630 Hz  | 1.29 | -4.2 dB |
| Peaking | 2555 Hz | 0.74 | 6.7 dB  |
| Peaking | 5995 Hz | 4.85 | 4.3 dB  |
| Peaking | 324 Hz  | 3.04 | 0.8 dB  |
| Peaking | 477 Hz  | 7.14 | -1.0 dB |
| Peaking | 2636 Hz | 5.47 | -0.7 dB |
| Peaking | 3895 Hz | 6.87 | 1.6 dB  |
| Peaking | 8640 Hz | 2.67 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Stir%20It%20Up/House%20of%20Marley%20Stir%20It%20Up.png)