# FLC Technologies FLC8 GGBl
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.4; 25 -8.5; 28 -8.6; 31 -8.7; 34 -8.7; 37 -8.6; 41 -8.6; 45 -8.6; 49 -8.6; 54 -8.6; 60 -8.7; 66 -8.8; 72 -8.8; 79 -9.0; 87 -9.1; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.2; 141 -9.3; 155 -9.3; 170 -9.2; 187 -9.0; 206 -8.9; 227 -8.7; 249 -8.5; 274 -8.3; 302 -8.1; 332 -7.8; 365 -7.5; 402 -7.2; 442 -6.7; 486 -6.6; 535 -6.3; 588 -5.8; 647 -5.6; 712 -5.7; 783 -5.4; 861 -5.5; 947 -6.1; 1042 -6.8; 1146 -7.2; 1261 -7.3; 1387 -7.0; 1526 -6.3; 1678 -5.4; 1846 -3.9; 2031 -2.4; 2234 -1.5; 2457 -0.6; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 GGBl GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 GGBl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.23 | -2.0 dB |
| Peaking | 180 Hz  | 0.7  | -1.9 dB |
| Peaking | 1462 Hz | 1.34 | -6.8 dB |
| Peaking | 2169 Hz | 0.61 | 8.0 dB  |
| Peaking | 5313 Hz | 2.24 | 3.9 dB  |
| Peaking | 875 Hz  | 1.57 | 0.7 dB  |
| Peaking | 1052 Hz | 4.04 | -1.2 dB |
| Peaking | 3975 Hz | 2.64 | 1.3 dB  |
| Peaking | 6401 Hz | 3.98 | 4.4 dB  |
| Peaking | 6886 Hz | 1.24 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20GGBl/FLC%20Technologies%20FLC8%20GGBl.png)