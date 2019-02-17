# Stax SR-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -2.5; 106 -4.7; 116 -6.3; 128 -7.6; 141 -8.6; 155 -8.9; 170 -8.9; 187 -8.9; 206 -8.6; 227 -8.1; 249 -7.5; 274 -6.9; 302 -6.6; 332 -6.1; 365 -5.7; 402 -5.4; 442 -5.3; 486 -5.3; 535 -5.1; 588 -5.8; 647 -7.7; 712 -5.9; 783 -4.7; 861 -5.4; 947 -5.9; 1042 -6.9; 1146 -7.1; 1261 -6.3; 1387 -6.8; 1526 -6.9; 1678 -6.0; 1846 -6.5; 2031 -7.1; 2234 -6.9; 2457 -7.3; 2703 -7.5; 2973 -8.2; 3270 -7.6; 3597 -7.6; 3957 -6.5; 4353 -6.2; 4788 -3.0; 5267 -1.6; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.3  | 8.0 dB  |
| Peaking | 159 Hz  | 1.01 | -8.5 dB |
| Peaking | 454 Hz  | 2.55 | 1.0 dB  |
| Peaking | 3271 Hz | 1.65 | -2.0 dB |
| Peaking | 5716 Hz | 2.73 | 6.9 dB  |
| Peaking | 19 Hz   | 1.24 | 2.2 dB  |
| Peaking | 42 Hz   | 0.49 | -1.1 dB |
| Peaking | 87 Hz   | 4.76 | 2.3 dB  |
| Peaking | 799 Hz  | 9.13 | 1.6 dB  |
| Peaking | 8705 Hz | 3.26 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-3/Stax%20SR-3.png)