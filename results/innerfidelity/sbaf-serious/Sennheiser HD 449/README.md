# Sennheiser HD 449
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.2; 28 -0.3; 31 -0.7; 34 -1.1; 37 -1.4; 41 -1.6; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.2; 66 -2.3; 72 -2.3; 79 -2.1; 87 -1.8; 96 -1.0; 106 0.3; 116 0.1; 128 -2.3; 141 -3.4; 155 -2.3; 170 -1.5; 187 -3.0; 206 -2.7; 227 -2.1; 249 -1.6; 274 -0.9; 302 -0.4; 332 0.3; 365 1.0; 402 0.9; 442 1.0; 486 0.9; 535 0.7; 588 0.5; 647 0.0; 712 -0.3; 783 0.1; 861 0.0; 947 -0.2; 1042 -0.0; 1146 0.0; 1261 -0.8; 1387 -1.7; 1526 -2.1; 1678 -2.1; 1846 -1.6; 2031 -0.3; 2234 1.3; 2457 2.9; 2703 3.1; 2973 3.7; 3270 3.9; 3597 4.1; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 449 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 1.37 | -2.4 dB |
| Peaking | 181 Hz  | 1.89 | -2.7 dB |
| Peaking | 1623 Hz | 2.99 | -3.3 dB |
| Peaking | 4482 Hz | 1.14 | 6.6 dB  |
| Peaking | 109 Hz  | 7.32 | 2.1 dB  |
| Peaking | 136 Hz  | 8.14 | -2.3 dB |
| Peaking | 421 Hz  | 2.5  | 1.4 dB  |
| Peaking | 6342 Hz | 3.39 | 4.4 dB  |
| Peaking | 7371 Hz | 1.59 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)