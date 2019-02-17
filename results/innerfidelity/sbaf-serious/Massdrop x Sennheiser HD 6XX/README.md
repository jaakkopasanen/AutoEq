# Massdrop x Sennheiser HD 6XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.5; 49 -2.0; 54 -2.4; 60 -2.7; 66 -3.6; 72 -3.8; 79 -4.6; 87 -5.9; 96 -6.8; 106 -7.4; 116 -7.8; 128 -8.3; 141 -8.6; 155 -8.9; 170 -8.8; 187 -9.0; 206 -9.2; 227 -9.0; 249 -8.8; 274 -8.5; 302 -8.3; 332 -8.3; 365 -8.1; 402 -8.0; 442 -7.7; 486 -7.7; 535 -7.5; 588 -7.2; 647 -7.1; 712 -6.9; 783 -6.6; 861 -6.9; 947 -7.1; 1042 -6.5; 1146 -7.4; 1261 -7.6; 1387 -7.8; 1526 -8.2; 1678 -8.5; 1846 -8.2; 2031 -7.5; 2234 -7.2; 2457 -6.8; 2703 -6.4; 2973 -6.6; 3270 -6.6; 3597 -6.9; 3957 -6.3; 4353 -6.0; 4788 -5.6; 5267 -3.4; 5793 -1.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 6XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 6XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.27 | 6.5 dB  |
| Peaking | 118 Hz  | 0.79 | -4.2 dB |
| Peaking | 235 Hz  | 0.88 | -2.0 dB |
| Peaking | 2932 Hz | 0.25 | -0.9 dB |
| Peaking | 6051 Hz | 2.91 | 6.4 dB  |
| Peaking | 934 Hz  | 1.81 | 0.6 dB  |
| Peaking | 1665 Hz | 2.21 | -1.4 dB |
| Peaking | 2629 Hz | 2.26 | 1.0 dB  |
| Peaking | 7741 Hz | 7.55 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Sennheiser%20HD%206XX/Massdrop%20x%20Sennheiser%20HD%206XX.png)