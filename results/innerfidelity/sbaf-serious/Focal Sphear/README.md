# Focal Sphear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.6; 28 -5.2; 31 -5.6; 34 -6.0; 37 -6.3; 41 -6.7; 45 -7.1; 49 -7.4; 54 -7.7; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.1; 87 -9.6; 96 -9.8; 106 -10.1; 116 -10.1; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.1; 187 -9.9; 206 -9.8; 227 -9.4; 249 -9.0; 274 -8.6; 302 -8.1; 332 -7.6; 365 -7.1; 402 -6.6; 442 -5.9; 486 -5.6; 535 -5.1; 588 -4.3; 647 -3.9; 712 -3.7; 783 -3.3; 861 -3.4; 947 -3.7; 1042 -4.0; 1146 -4.4; 1261 -4.8; 1387 -5.4; 1526 -6.2; 1678 -6.7; 1846 -6.8; 2031 -6.7; 2234 -6.8; 2457 -6.0; 2703 -5.0; 2973 -2.9; 3270 -1.0; 3597 -0.5; 3957 -1.9; 4353 -5.2; 4788 -8.1; 5267 -9.6; 5793 -7.2; 6373 -4.2; 7010 -2.5; 7711 -3.6; 8482 -5.3; 9330 -7.0; 10263 -4.5; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Sphear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Sphear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 101 Hz  | 0.57 | -5.5 dB |
| Peaking | 229 Hz  | 1.08 | -3.0 dB |
| Peaking | 2042 Hz | 1.79 | -3.5 dB |
| Peaking | 3519 Hz | 3.19 | 5.1 dB  |
| Peaking | 5126 Hz | 4.04 | -6.5 dB |
| Peaking | 18 Hz   | 2.4  | 1.2 dB  |
| Peaking | 781 Hz  | 0.69 | -1.8 dB |
| Peaking | 788 Hz  | 1.26 | 3.2 dB  |
| Peaking | 6976 Hz | 5.72 | 2.3 dB  |
| Peaking | 9174 Hz | 5.77 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Sphear/Focal%20Sphear.png)