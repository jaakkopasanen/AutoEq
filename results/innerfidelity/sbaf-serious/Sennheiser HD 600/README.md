# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.2; 45 -1.9; 49 -2.4; 54 -3.1; 60 -3.7; 66 -4.3; 72 -4.7; 79 -5.4; 87 -6.4; 96 -7.2; 106 -7.6; 116 -7.9; 128 -8.3; 141 -8.5; 155 -8.6; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.2; 249 -8.1; 274 -7.8; 302 -7.6; 332 -7.4; 365 -7.1; 402 -7.0; 442 -6.7; 486 -6.7; 535 -6.4; 588 -5.9; 647 -6.0; 712 -6.0; 783 -5.9; 861 -6.1; 947 -6.0; 1042 -5.6; 1146 -6.0; 1261 -6.5; 1387 -6.8; 1526 -7.3; 1678 -7.8; 1846 -7.4; 2031 -6.8; 2234 -6.9; 2457 -6.3; 2703 -6.7; 2973 -6.5; 3270 -7.0; 3597 -7.1; 3957 -6.1; 4353 -6.8; 4788 -7.0; 5267 -3.3; 5793 -1.4; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.4  | 6.7 dB  |
| Peaking | 128 Hz  |  0.59 | -3.7 dB |
| Peaking | 792 Hz  |  0.94 | 1.5 dB  |
| Peaking | 2634 Hz |  0.24 | -0.9 dB |
| Peaking | 6033 Hz |  3.22 | 6.3 dB  |
| Peaking | 1049 Hz |  8.77 | 0.7 dB  |
| Peaking | 1694 Hz |  5.2  | -1.0 dB |
| Peaking | 2504 Hz |  3.6  | 0.8 dB  |
| Peaking | 4648 Hz | 12.02 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)