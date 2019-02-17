# Sennheiser HD 380 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.2; 23 -14.4; 25 -14.4; 28 -14.5; 31 -14.5; 34 -14.4; 37 -14.2; 41 -14.0; 45 -13.6; 49 -13.2; 54 -12.5; 60 -11.7; 66 -10.6; 72 -9.7; 79 -8.0; 87 -5.4; 96 -3.6; 106 -6.6; 116 -7.7; 128 -7.4; 141 -9.1; 155 -7.3; 170 -5.9; 187 -5.8; 206 -4.1; 227 -3.0; 249 -2.8; 274 -3.1; 302 -3.9; 332 -5.0; 365 -6.0; 402 -6.6; 442 -6.8; 486 -7.0; 535 -6.9; 588 -6.2; 647 -5.8; 712 -5.6; 783 -5.0; 861 -4.9; 947 -4.7; 1042 -4.5; 1146 -4.2; 1261 -4.2; 1387 -4.2; 1526 -4.5; 1678 -5.4; 1846 -7.5; 2031 -8.7; 2234 -8.8; 2457 -8.4; 2703 -6.4; 2973 -3.9; 3270 -2.6; 3597 -4.9; 3957 -6.5; 4353 -7.1; 4788 -3.9; 5267 -0.5; 5793 -0.6; 6373 -1.8; 7010 -3.9; 7711 -4.3; 8482 -4.5; 9330 -4.7; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 380 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 380 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.64 | -9.9 dB |
| Peaking | 52 Hz   | 1.93 | -3.5 dB |
| Peaking | 494 Hz  | 2.8  | -2.6 dB |
| Peaking | 2179 Hz | 3.52 | -5.0 dB |
| Peaking | 5657 Hz | 5.1  | 5.0 dB  |
| Peaking | 94 Hz   | 4.86 | 5.5 dB  |
| Peaking | 130 Hz  | 1.19 | -3.1 dB |
| Peaking | 238 Hz  | 2.66 | 3.5 dB  |
| Peaking | 3255 Hz | 7.76 | 3.0 dB  |
| Peaking | 4206 Hz | 6.45 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB   |
| Peaking | 500 Hz   | 1.41 | -3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20380%20Pro/Sennheiser%20HD%20380%20Pro.png)