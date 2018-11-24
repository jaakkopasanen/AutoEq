# Sennheiser HD 820

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.2; 25 5.1; 28 5.0; 31 5.0; 34 5.0; 37 5.0; 41 4.9; 45 4.8; 49 4.8; 54 4.7; 60 4.6; 66 4.4; 72 4.2; 79 3.9; 87 3.4; 96 2.9; 106 2.4; 116 2.0; 128 1.6; 141 1.4; 155 1.5; 170 1.8; 187 2.4; 206 3.7; 227 5.7; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 5.8; 442 4.9; 486 4.2; 535 3.7; 588 3.1; 647 2.3; 712 1.4; 783 0.5; 861 -0.0; 947 -0.2; 1042 0.2; 1146 0.6; 1261 1.2; 1387 1.4; 1526 1.8; 1678 2.5; 1846 3.0; 2031 2.6; 2234 2.9; 2457 3.9; 2703 4.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.8; 6373 4.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.65 | 5.1 dB  |
| Peaking | 65 Hz   | 1.44 | 2.8 dB  |
| Peaking | 323 Hz  | 1.1  | 6.5 dB  |
| Peaking | 3318 Hz | 1.21 | 5.8 dB  |
| Peaking | 5457 Hz | 2.67 | 4.3 dB  |
| Peaking | 154 Hz  | 2.92 | -1.3 dB |
| Peaking | 329 Hz  | 0.26 | 0.4 dB  |
| Peaking | 910 Hz  | 2.98 | -1.9 dB |
| Peaking | 1756 Hz | 6.32 | 1.1 dB  |
| Peaking | 8509 Hz | 3.63 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)