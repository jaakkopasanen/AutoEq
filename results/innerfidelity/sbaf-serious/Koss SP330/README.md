# Koss SP330
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.5; 31 -9.7; 34 -9.8; 37 -9.8; 41 -9.8; 45 -9.8; 49 -9.8; 54 -9.8; 60 -9.6; 66 -9.5; 72 -9.6; 79 -9.9; 87 -10.1; 96 -10.2; 106 -10.1; 116 -10.0; 128 -9.9; 141 -9.5; 155 -9.2; 170 -8.8; 187 -7.9; 206 -7.5; 227 -7.2; 249 -6.4; 274 -5.6; 302 -5.1; 332 -5.6; 365 -6.4; 402 -7.0; 442 -7.3; 486 -7.5; 535 -7.5; 588 -7.1; 647 -6.9; 712 -6.6; 783 -5.5; 861 -6.0; 947 -5.6; 1042 -5.2; 1146 -4.7; 1261 -4.3; 1387 -4.3; 1526 -4.5; 1678 -4.6; 1846 -4.5; 2031 -4.1; 2234 -4.3; 2457 -4.2; 2703 -4.5; 2973 -4.8; 3270 -4.5; 3597 -5.0; 3957 -5.7; 4353 -7.5; 4788 -7.2; 5267 -4.2; 5793 -1.7; 6373 -0.5; 7010 -3.3; 7711 -5.6; 8482 -5.9; 9330 -6.5; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss SP330 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP330 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.47 | -3.8 dB |
| Peaking | 118 Hz  | 1.24 | -3.1 dB |
| Peaking | 534 Hz  | 2.72 | -1.8 dB |
| Peaking | 1791 Hz | 1.01 | 1.8 dB  |
| Peaking | 6259 Hz | 5.51 | 5.9 dB  |
| Peaking | 291 Hz  | 1.11 | -1.3 dB |
| Peaking | 296 Hz  | 2.77 | 2.8 dB  |
| Peaking | 4540 Hz | 4.11 | -4.7 dB |
| Peaking | 4768 Hz | 1.36 | 2.1 dB  |
| Peaking | 8592 Hz | 2.01 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP330/Koss%20SP330.png)