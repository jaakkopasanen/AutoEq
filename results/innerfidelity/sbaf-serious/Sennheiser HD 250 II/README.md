# Sennheiser HD 250 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 -0.6; 25 -1.1; 28 -1.8; 31 -2.3; 34 -2.7; 37 -3.0; 41 -3.2; 45 -3.4; 49 -3.5; 54 -3.5; 60 -3.2; 66 -2.8; 72 -2.5; 79 -1.7; 87 -1.5; 96 -2.8; 106 -4.8; 116 -5.4; 128 -4.4; 141 -4.2; 155 -3.4; 170 -2.6; 187 -1.8; 206 -0.7; 227 -0.6; 249 -0.4; 274 0.0; 302 0.3; 332 0.9; 365 1.2; 402 1.3; 442 1.2; 486 1.0; 535 0.9; 588 1.1; 647 0.9; 712 0.7; 783 0.8; 861 0.5; 947 0.2; 1042 0.0; 1146 -0.1; 1261 0.6; 1387 -0.2; 1526 -1.0; 1678 -0.8; 1846 -0.3; 2031 -0.5; 2234 -0.9; 2457 -0.3; 2703 0.4; 2973 1.6; 3270 2.0; 3597 2.3; 3957 2.1; 4353 0.3; 4788 -0.2; 5267 0.8; 5793 3.4; 6373 1.8; 7010 -0.6; 7711 -0.7; 8482 -2.6; 9330 -3.1; 10263 -0.1; 11289 -0.0; 12418 -0.9; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 250 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 1.27 | -3.6 dB |
| Peaking | 123 Hz   | 2.13 | -5.0 dB |
| Peaking | 3526 Hz  | 4.07 | 2.7 dB  |
| Peaking | 5959 Hz  | 8.52 | 4.2 dB  |
| Peaking | 8908 Hz  | 4.61 | -3.7 dB |
| Peaking | 83 Hz    | 7.44 | 1.0 dB  |
| Peaking | 174 Hz   | 3.61 | -1.0 dB |
| Peaking | 463 Hz   | 0.93 | 1.4 dB  |
| Peaking | 1762 Hz  | 1.86 | -0.9 dB |
| Peaking | 10478 Hz | 8.69 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20250%20II/Sennheiser%20HD%20250%20II.png)