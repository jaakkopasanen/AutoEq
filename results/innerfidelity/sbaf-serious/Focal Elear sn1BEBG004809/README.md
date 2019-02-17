# Focal Elear sn1BEBG004809
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.1; 28 -3.5; 31 -3.7; 34 -4.0; 37 -4.1; 41 -4.3; 45 -4.5; 49 -4.7; 54 -5.0; 60 -5.4; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.3; 116 -7.4; 128 -7.7; 141 -7.7; 155 -7.8; 170 -7.8; 187 -7.8; 206 -7.8; 227 -7.7; 249 -7.6; 274 -7.4; 302 -7.3; 332 -7.2; 365 -7.0; 402 -6.9; 442 -6.7; 486 -6.7; 535 -6.6; 588 -6.2; 647 -6.0; 712 -6.1; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -7.0; 1261 -7.2; 1387 -7.5; 1526 -8.1; 1678 -8.9; 1846 -8.7; 2031 -8.8; 2234 -8.5; 2457 -8.4; 2703 -7.9; 2973 -6.8; 3270 -5.8; 3597 -5.2; 3957 -1.8; 4353 -1.1; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -8.7; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear sn1BEBG004809 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear sn1BEBG004809 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.34 | 4.2 dB  |
| Peaking | 152 Hz  |  0.83 | -1.7 dB |
| Peaking | 2354 Hz |  1.19 | -3.9 dB |
| Peaking | 5304 Hz |  1.04 | 7.7 dB  |
| Peaking | 8464 Hz |  2.52 | -5.2 dB |
| Peaking | 769 Hz  |  2.09 | 0.9 dB  |
| Peaking | 1654 Hz |  7.52 | -0.9 dB |
| Peaking | 3998 Hz |  3.05 | -1.6 dB |
| Peaking | 4076 Hz |  8.16 | 3.3 dB  |
| Peaking | 6396 Hz | 11.7  | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20sn1BEBG004809/Focal%20Elear%20sn1BEBG004809.png)