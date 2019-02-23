# Sennheiser HD 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.7; 31 -3.4; 34 -4.1; 37 -4.6; 41 -5.1; 45 -5.5; 49 -5.9; 54 -6.3; 60 -6.7; 66 -7.1; 72 -7.3; 79 -7.7; 87 -8.1; 96 -8.3; 106 -8.7; 116 -8.8; 128 -8.8; 141 -9.1; 155 -9.7; 170 -8.8; 187 -9.3; 206 -9.6; 227 -9.4; 249 -9.1; 274 -8.8; 302 -8.4; 332 -7.9; 365 -7.5; 402 -7.3; 442 -7.5; 486 -8.0; 535 -8.0; 588 -7.7; 647 -7.8; 712 -7.9; 783 -7.8; 861 -8.0; 947 -8.1; 1042 -8.3; 1146 -8.4; 1261 -8.7; 1387 -9.2; 1526 -9.6; 1678 -10.3; 1846 -10.0; 2031 -9.4; 2234 -8.9; 2457 -7.4; 2703 -5.7; 2973 -4.0; 3270 -2.2; 3597 -0.9; 3957 -0.9; 4353 -0.9; 4788 -6.6; 5267 -7.2; 5793 -4.6; 6373 -2.2; 7010 -4.3; 7711 -6.6; 8482 -6.8; 9330 -6.9; 10263 -6.9; 11289 -6.9; 12418 -6.9; 13660 -6.9; 15026 -6.9; 16529 -6.9; 18182 -6.9; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.84 | 7.0 dB  |
| Peaking | 161 Hz  | 0.64 | -2.7 dB |
| Peaking | 1847 Hz | 1.08 | -5.0 dB |
| Peaking | 3239 Hz | 0.57 | 2.1 dB  |
| Peaking | 3658 Hz | 2.42 | 5.9 dB  |
| Peaking | 128 Hz  | 4.52 | 0.2 dB  |
| Peaking | 4467 Hz | 7.77 | 3.9 dB  |
| Peaking | 4959 Hz | 6.51 | -5.6 dB |
| Peaking | 6497 Hz | 4.48 | 5.1 dB  |
| Peaking | 7434 Hz | 1.65 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%204/Sennheiser%20HD%204.png)