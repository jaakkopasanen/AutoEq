# Focal Elear sn1BEBG004809
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.1; 25 -3.4; 28 -3.7; 31 -4.0; 34 -4.2; 37 -4.4; 41 -4.6; 45 -4.8; 49 -5.0; 54 -5.3; 60 -5.7; 66 -6.0; 72 -6.3; 79 -6.6; 87 -7.0; 96 -7.3; 106 -7.6; 116 -7.7; 128 -8.0; 141 -8.0; 155 -8.1; 170 -8.0; 187 -8.1; 206 -8.1; 227 -8.0; 249 -7.9; 274 -7.7; 302 -7.6; 332 -7.5; 365 -7.3; 402 -7.2; 442 -7.0; 486 -7.0; 535 -6.9; 588 -6.5; 647 -6.3; 712 -6.4; 783 -6.2; 861 -6.4; 947 -6.6; 1042 -6.8; 1146 -7.3; 1261 -7.5; 1387 -7.8; 1526 -8.4; 1678 -9.2; 1846 -9.0; 2031 -9.1; 2234 -8.8; 2457 -8.7; 2703 -8.2; 2973 -7.1; 3270 -6.1; 3597 -5.5; 3957 -2.1; 4353 -1.4; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -9.0; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear sn1BEBG004809 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear sn1BEBG004809 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.35 | 4.0 dB  |
| Peaking | 156 Hz  |  0.72 | -2.0 dB |
| Peaking | 2328 Hz |  1.1  | -4.1 dB |
| Peaking | 5344 Hz |  1.07 | 7.8 dB  |
| Peaking | 8481 Hz |  2.65 | -5.5 dB |
| Peaking | 776 Hz  |  2.4  | 0.7 dB  |
| Peaking | 1666 Hz |  7.8  | -0.8 dB |
| Peaking | 3662 Hz |  6.12 | -1.2 dB |
| Peaking | 4053 Hz | 10.61 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20sn1BEBG004809/Focal%20Elear%20sn1BEBG004809.png)