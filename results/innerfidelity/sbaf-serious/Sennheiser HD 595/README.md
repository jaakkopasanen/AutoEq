# Sennheiser HD 595
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -1.3; 79 -1.8; 87 -2.8; 96 -3.7; 106 -4.3; 116 -4.7; 128 -5.3; 141 -5.7; 155 -6.1; 170 -6.2; 187 -6.4; 206 -6.6; 227 -6.6; 249 -6.6; 274 -6.7; 302 -6.7; 332 -6.7; 365 -6.7; 402 -6.6; 442 -6.5; 486 -6.6; 535 -6.3; 588 -5.8; 647 -5.9; 712 -6.1; 783 -6.0; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.6; 1261 -7.0; 1387 -6.9; 1526 -6.7; 1678 -6.1; 1846 -5.1; 2031 -4.6; 2234 -5.0; 2457 -5.3; 2703 -5.6; 2973 -4.9; 3270 -4.1; 3597 -3.2; 3957 -1.6; 4353 -2.3; 4788 -3.3; 5267 -2.8; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 595 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.58 | 6.9 dB  |
| Peaking | 646 Hz  | 3.39 | 0.4 dB  |
| Peaking | 4017 Hz | 1.86 | 4.1 dB  |
| Peaking | 6252 Hz | 3.3  | 5.6 dB  |
| Peaking | 8164 Hz | 1.69 | -1.6 dB |
| Peaking | 42 Hz   | 2.78 | -1.0 dB |
| Peaking | 71 Hz   | 1.91 | 1.5 dB  |
| Peaking | 181 Hz  | 0.86 | -0.9 dB |
| Peaking | 1396 Hz | 2.76 | -0.8 dB |
| Peaking | 1998 Hz | 4.81 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)