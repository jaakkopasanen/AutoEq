# Sennheiser HD 575
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.8; 41 4.1; 45 3.6; 49 3.1; 54 2.8; 60 2.2; 66 1.5; 72 0.8; 79 0.2; 87 -0.7; 96 -1.5; 106 -2.0; 116 -2.3; 128 -2.8; 141 -3.2; 155 -3.4; 170 -3.5; 187 -3.6; 206 -3.7; 227 -3.5; 249 -3.1; 274 -3.0; 302 -2.8; 332 -2.6; 365 -2.3; 402 -2.0; 442 -1.5; 486 -1.4; 535 -1.0; 588 -0.5; 647 -0.4; 712 -0.2; 783 0.2; 861 -0.0; 947 -0.1; 1042 -0.1; 1146 0.1; 1261 -0.2; 1387 -0.3; 1526 -0.6; 1678 -0.2; 1846 1.2; 2031 0.8; 2234 0.0; 2457 -1.4; 2703 -3.6; 2973 -4.4; 3270 -4.5; 3597 -3.3; 3957 -1.4; 4353 -0.7; 4788 -0.1; 5267 1.5; 5793 0.1; 6373 1.7; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 575 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 575 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.48 | 6.4 dB  |
| Peaking | 168 Hz  | 0.59 | -4.3 dB |
| Peaking | 1996 Hz | 4.3  | 2.0 dB  |
| Peaking | 3079 Hz | 2.85 | -5.2 dB |
| Peaking | 6768 Hz | 6.45 | 3.5 dB  |
| Peaking | 362 Hz  | 2.97 | -0.4 dB |
| Peaking | 762 Hz  | 2.22 | 0.6 dB  |
| Peaking | 5222 Hz | 9.79 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20575/Sennheiser%20HD%20575.png)