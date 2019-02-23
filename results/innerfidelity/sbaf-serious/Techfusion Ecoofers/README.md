# Techfusion Ecoofers
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.4; 23 -16.5; 25 -16.5; 28 -16.5; 31 -16.6; 34 -16.5; 37 -16.5; 41 -16.5; 45 -16.4; 49 -16.4; 54 -16.4; 60 -16.4; 66 -16.4; 72 -16.5; 79 -16.5; 87 -16.5; 96 -16.5; 106 -16.3; 116 -16.0; 128 -15.9; 141 -15.5; 155 -15.2; 170 -14.8; 187 -14.3; 206 -13.7; 227 -13.1; 249 -12.5; 274 -11.7; 302 -11.0; 332 -10.2; 365 -9.4; 402 -8.5; 442 -7.6; 486 -6.8; 535 -5.9; 588 -4.8; 647 -3.9; 712 -3.1; 783 -2.1; 861 -1.9; 947 -1.6; 1042 -1.5; 1146 -1.5; 1261 -1.5; 1387 -1.8; 1526 -2.1; 1678 -2.8; 1846 -4.2; 2031 -4.3; 2234 -4.2; 2457 -4.0; 2703 -4.5; 2973 -4.8; 3270 -2.9; 3597 -0.5; 3957 -0.6; 4353 -2.3; 4788 -3.2; 5267 -3.5; 5793 -5.1; 6373 -6.8; 7010 -5.2; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Techfusion Ecoofers GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Techfusion Ecoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 51 Hz   |  0.13 | -10.5 dB |
| Peaking | 776 Hz  |  0.74 | 5.6 dB   |
| Peaking | 1311 Hz |  1.65 | 2.4 dB   |
| Peaking | 3911 Hz |  2.5  | 5.6 dB   |
| Peaking | 9384 Hz |  1.98 | -0.2 dB  |
| Peaking | 47 Hz   |  0.52 | -1.0 dB  |
| Peaking | 49 Hz   |  0.95 | 1.5 dB   |
| Peaking | 3003 Hz | 12.61 | -1.3 dB  |
| Peaking | 5345 Hz |  6.79 | 1.3 dB   |
| Peaking | 6260 Hz | 11.07 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -8.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Techfusion%20Ecoofers/Techfusion%20Ecoofers.png)