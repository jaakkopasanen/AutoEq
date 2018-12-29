# Sennheiser HD 239
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.7; 28 1.1; 31 0.7; 34 0.3; 37 -0.1; 41 -0.5; 45 -0.9; 49 -1.2; 54 -1.4; 60 -1.8; 66 -2.0; 72 -2.3; 79 -2.4; 87 -2.6; 96 -3.0; 106 -3.4; 116 -3.5; 128 -3.8; 141 -3.8; 155 -3.7; 170 -3.6; 187 -3.5; 206 -3.4; 227 -3.0; 249 -2.8; 274 -2.5; 302 -2.3; 332 -2.0; 365 -1.6; 402 -1.4; 442 -1.0; 486 -0.9; 535 -0.7; 588 -0.2; 647 -0.1; 712 -0.1; 783 0.2; 861 0.1; 947 0.0; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -0.7; 1526 -1.2; 1678 -2.1; 1846 -1.7; 2031 -0.1; 2234 1.6; 2457 3.0; 2703 2.3; 2973 0.4; 3270 -2.1; 3597 1.8; 3957 4.5; 4353 -1.4; 4788 -2.0; 5267 -0.4; 5793 0.4; 6373 1.1; 7010 0.7; 7711 0.4; 8482 -2.2; 9330 -5.2; 10263 -3.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 239 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.47 | 3.2 dB  |
| Peaking | 143 Hz  | 0.54 | -3.8 dB |
| Peaking | 2520 Hz | 6.81 | 3.7 dB  |
| Peaking | 6956 Hz | 3.86 | 1.6 dB  |
| Peaking | 9470 Hz | 4.74 | -6.0 dB |
| Peaking | 752 Hz  | 1.93 | 0.6 dB  |
| Peaking | 1708 Hz | 4.71 | -2.5 dB |
| Peaking | 3345 Hz | 6.84 | -4.9 dB |
| Peaking | 3899 Hz | 3.58 | 7.3 dB  |
| Peaking | 4462 Hz | 4.74 | -5.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)