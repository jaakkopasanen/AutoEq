# Sennheiser RS 175

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.4; 28 -9.2; 31 -8.9; 34 -8.6; 37 -8.2; 41 -7.7; 45 -7.2; 49 -6.7; 54 -6.1; 60 -5.8; 66 -5.7; 72 -5.8; 79 -5.9; 87 -6.0; 96 -6.1; 106 -6.0; 116 -5.6; 128 -4.9; 141 -3.9; 155 -2.6; 170 -1.1; 187 0.4; 206 1.8; 227 2.9; 249 3.5; 274 3.6; 302 3.5; 332 3.3; 365 3.8; 402 5.1; 442 5.7; 486 5.3; 535 4.7; 588 3.9; 647 3.2; 712 2.5; 783 1.5; 861 0.8; 947 0.2; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -0.8; 1526 -0.6; 1678 -0.1; 1846 1.0; 2031 0.1; 2234 -3.2; 2457 -5.8; 2703 -6.6; 2973 -5.6; 3270 -2.9; 3597 0.3; 3957 0.2; 4353 -1.0; 4788 0.2; 5267 1.8; 5793 1.9; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 175 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 175 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.43 | -9.3 dB |
| Peaking | 112 Hz  | 1.36 | -4.9 dB |
| Peaking | 371 Hz  | 0.76 | 5.5 dB  |
| Peaking | 2686 Hz | 3.46 | -7.6 dB |
| Peaking | 6432 Hz | 5.08 | 5.4 dB  |
| Peaking | 232 Hz  | 3.89 | 1.2 dB  |
| Peaking | 347 Hz  | 3.26 | -2.5 dB |
| Peaking | 465 Hz  | 1.48 | 1.8 dB  |
| Peaking | 1121 Hz | 1.03 | -1.4 dB |
| Peaking | 1923 Hz | 6.82 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20RS%20175/Sennheiser%20RS%20175.png)