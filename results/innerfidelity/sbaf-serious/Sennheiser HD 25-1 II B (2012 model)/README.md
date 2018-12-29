# Sennheiser HD 25-1 II B (2012 model)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.2; 28 0.6; 31 0.2; 34 -0.2; 37 -0.5; 41 -0.7; 45 -0.9; 49 -1.0; 54 -1.0; 60 -1.1; 66 -1.3; 72 -1.8; 79 -2.1; 87 -2.0; 96 -1.8; 106 -1.5; 116 -1.8; 128 -3.1; 141 -3.7; 155 -3.2; 170 -2.8; 187 -2.7; 206 -1.9; 227 -1.0; 249 -0.3; 274 0.4; 302 0.6; 332 0.8; 365 1.0; 402 1.0; 442 1.0; 486 0.7; 535 0.6; 588 0.9; 647 0.7; 712 0.6; 783 0.6; 861 0.4; 947 0.2; 1042 0.0; 1146 -0.1; 1261 -0.4; 1387 -1.0; 1526 -1.5; 1678 -2.0; 1846 -2.2; 2031 -2.3; 2234 -1.3; 2457 0.5; 2703 2.0; 2973 3.2; 3270 2.6; 3597 2.9; 3957 3.4; 4353 4.5; 4788 4.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.9; 9330 -4.0; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II B (2012 model) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II B (2012 model) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.89 | 2.0 dB  |
| Peaking | 140 Hz  | 1.48 | -3.5 dB |
| Peaking | 3066 Hz | 5.57 | 2.2 dB  |
| Peaking | 5532 Hz | 1.77 | 6.7 dB  |
| Peaking | 8947 Hz | 4.43 | -6.0 dB |
| Peaking | 67 Hz   | 1.86 | -1.1 dB |
| Peaking | 356 Hz  | 2.14 | 1.2 dB  |
| Peaking | 669 Hz  | 1.19 | 0.8 dB  |
| Peaking | 1991 Hz | 1.65 | -4.5 dB |
| Peaking | 2545 Hz | 1.42 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model)/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model).png)