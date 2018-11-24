# Sennheiser HD 518

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.3; 37 4.6; 41 3.6; 45 2.8; 49 2.1; 54 1.4; 60 0.8; 66 0.2; 72 -0.2; 79 -0.6; 87 -1.0; 96 -1.4; 106 -2.0; 116 -2.5; 128 -2.8; 141 -3.0; 155 -3.1; 170 -3.1; 187 -3.1; 206 -3.0; 227 -2.7; 249 -2.4; 274 -2.2; 302 -2.0; 332 -1.7; 365 -1.4; 402 -1.3; 442 -1.1; 486 -0.9; 535 -0.7; 588 -0.5; 647 -0.2; 712 0.4; 783 -0.0; 861 -0.2; 947 -0.1; 1042 0.3; 1146 1.0; 1261 1.7; 1387 2.2; 1526 3.0; 1678 3.5; 1846 3.5; 2031 3.4; 2234 3.1; 2457 2.9; 2703 3.3; 2973 3.1; 3270 2.4; 3597 2.4; 3957 1.4; 4353 -1.0; 4788 0.8; 5267 3.6; 5793 5.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.79 | 6.6 dB  |
| Peaking | 160 Hz  | 0.59 | -3.5 dB |
| Peaking | 1764 Hz | 1.72 | 3.5 dB  |
| Peaking | 2886 Hz | 2.82 | 2.5 dB  |
| Peaking | 6065 Hz | 4.34 | 6.2 dB  |
| Peaking | 3794 Hz | 6.57 | 1.8 dB  |
| Peaking | 4457 Hz | 4.55 | -3.1 dB |
| Peaking | 4898 Hz | 3.15 | 0.3 dB  |
| Peaking | 5185 Hz | 6.04 | 1.7 dB  |
| Peaking | 8238 Hz | 4.45 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)