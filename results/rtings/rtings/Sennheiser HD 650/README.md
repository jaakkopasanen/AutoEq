# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 5.0; 41 4.4; 45 4.0; 49 3.6; 54 3.1; 60 2.5; 66 2.0; 72 1.5; 79 1.0; 87 0.4; 96 -0.1; 106 -0.6; 116 -1.1; 128 -1.5; 141 -1.8; 155 -2.0; 170 -2.1; 187 -2.2; 206 -2.0; 227 -1.9; 249 -1.7; 274 -1.7; 302 -1.6; 332 -1.6; 365 -1.5; 402 -1.5; 442 -1.5; 486 -1.4; 535 -1.4; 588 -1.2; 647 -1.1; 712 -0.9; 783 -0.9; 861 -0.8; 947 -0.2; 1042 -0.4; 1146 -0.7; 1261 -1.1; 1387 -1.4; 1526 -1.6; 1678 -1.8; 1846 -2.0; 2031 -2.2; 2234 -1.5; 2457 -1.1; 2703 -1.0; 2973 -1.2; 3270 -1.2; 3597 -0.6; 3957 0.4; 4353 1.2; 4788 1.5; 5267 2.6; 5793 3.7; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 6.6 dB  |
| Peaking | 144 Hz  | 0.38 | -3.1 dB |
| Peaking | 1866 Hz | 1.67 | -2.1 dB |
| Peaking | 3196 Hz | 5.03 | -1.2 dB |
| Peaking | 5947 Hz | 2.68 | 4.1 dB  |
| Peaking | 560 Hz  | 4.18 | -0.3 dB |
| Peaking | 3750 Hz | 4.06 | -0.4 dB |
| Peaking | 4173 Hz | 4.59 | 0.8 dB  |
| Peaking | 8275 Hz | 4.96 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)