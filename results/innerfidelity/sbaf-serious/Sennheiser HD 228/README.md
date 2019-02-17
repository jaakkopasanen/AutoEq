# Sennheiser HD 228
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.3; 25 -3.0; 28 -3.9; 31 -4.7; 34 -5.4; 37 -5.9; 41 -6.5; 45 -7.1; 49 -7.6; 54 -8.2; 60 -8.9; 66 -9.5; 72 -10.0; 79 -10.6; 87 -11.0; 96 -11.6; 106 -11.6; 116 -11.2; 128 -11.3; 141 -12.5; 155 -13.3; 170 -13.1; 187 -13.4; 206 -13.0; 227 -12.5; 249 -12.7; 274 -11.1; 302 -9.8; 332 -9.9; 365 -9.3; 402 -8.3; 442 -7.7; 486 -7.2; 535 -6.5; 588 -5.9; 647 -5.7; 712 -5.8; 783 -5.8; 861 -6.2; 947 -6.4; 1042 -6.4; 1146 -6.1; 1261 -5.6; 1387 -5.1; 1526 -5.2; 1678 -6.4; 1846 -5.5; 2031 -5.0; 2234 -4.3; 2457 -3.1; 2703 -2.8; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -7.5; 5267 -8.8; 5793 -5.2; 6373 -4.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -10.8; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 228 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.03 | 5.5 dB  |
| Peaking | 91 Hz    | 0.85 | -3.8 dB |
| Peaking | 203 Hz   | 1.22 | -5.9 dB |
| Peaking | 3345 Hz  | 1.8  | 6.6 dB  |
| Peaking | 18695 Hz | 1.73 | -4.9 dB |
| Peaking | 656 Hz   | 2.62 | 1.4 dB  |
| Peaking | 4299 Hz  | 6.63 | 4.0 dB  |
| Peaking | 5048 Hz  | 4.81 | -6.2 dB |
| Peaking | 6721 Hz  | 3.03 | 3.7 dB  |
| Peaking | 7621 Hz  | 3.13 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)