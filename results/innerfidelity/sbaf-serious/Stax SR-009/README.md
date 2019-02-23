# Stax SR-009
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -0.8; 25 -0.8; 28 -0.7; 31 -0.6; 34 -0.6; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.3; 54 -2.0; 60 -3.0; 66 -4.2; 72 -4.2; 79 -4.0; 87 -4.2; 96 -4.4; 106 -4.6; 116 -4.7; 128 -5.0; 141 -5.1; 155 -5.3; 170 -5.6; 187 -5.7; 206 -5.8; 227 -5.8; 249 -5.9; 274 -5.9; 302 -6.0; 332 -6.2; 365 -6.2; 402 -6.3; 442 -6.4; 486 -6.8; 535 -6.9; 588 -6.8; 647 -7.0; 712 -7.2; 783 -6.8; 861 -7.4; 947 -8.2; 1042 -8.8; 1146 -9.3; 1261 -9.2; 1387 -8.7; 1526 -8.9; 1678 -8.8; 1846 -7.0; 2031 -5.7; 2234 -5.1; 2457 -3.8; 2703 -4.7; 2973 -4.6; 3270 -5.1; 3597 -5.0; 3957 -6.8; 4353 -8.0; 4788 -9.9; 5267 -8.3; 5793 -1.5; 6373 -0.8; 7010 -4.7; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.7; 15026 -7.1; 16529 -6.1; 18182 -6.1; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.58 | 5.9 dB  |
| Peaking | 1502 Hz  | 0.95 | -4.6 dB |
| Peaking | 2401 Hz  | 1.24 | 4.3 dB  |
| Peaking | 4961 Hz  | 3.45 | -5.9 dB |
| Peaking | 6044 Hz  | 4.74 | 8.0 dB  |
| Peaking | 128 Hz   | 3.12 | 0.2 dB  |
| Peaking | 804 Hz   | 4.77 | 1.3 dB  |
| Peaking | 835 Hz   | 1.88 | -0.7 dB |
| Peaking | 14558 Hz | 4.11 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009/Stax%20SR-009.png)