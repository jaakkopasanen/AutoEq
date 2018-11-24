# Sennheiser HD 820

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.8; 28 4.8; 31 4.9; 34 5.0; 37 5.1; 41 5.2; 45 5.1; 49 5.1; 54 5.1; 60 4.9; 66 4.6; 72 4.2; 79 3.7; 87 3.1; 96 2.5; 106 1.9; 116 1.5; 128 1.1; 141 0.9; 155 0.9; 170 1.1; 187 1.8; 206 3.2; 227 5.4; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 4.8; 442 3.8; 486 3.0; 535 2.5; 588 2.0; 647 1.2; 712 0.5; 783 -0.0; 861 -0.2; 947 -0.2; 1042 0.1; 1146 0.4; 1261 1.0; 1387 1.5; 1526 2.2; 1678 2.9; 1846 2.9; 2031 2.2; 2234 2.4; 2457 3.4; 2703 3.7; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 4.8; 5267 3.6; 5793 2.2; 6373 0.7; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.62 | 5.7 dB  |
| Peaking | 313 Hz  | 1.44 | 6.5 dB  |
| Peaking | 1716 Hz | 4.07 | 2.0 dB  |
| Peaking | 3716 Hz | 1.37 | 6.5 dB  |
| Peaking | 70 Hz   | 3.25 | 0.9 dB  |
| Peaking | 147 Hz  | 2.34 | -1.7 dB |
| Peaking | 479 Hz  | 0.29 | 0.5 dB  |
| Peaking | 877 Hz  | 2.13 | -1.6 dB |
| Peaking | 8952 Hz | 2.64 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)