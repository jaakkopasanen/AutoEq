# Havi B3 Pro1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.5; 34 -1.9; 37 -2.3; 41 -2.7; 45 -3.1; 49 -3.5; 54 -3.9; 60 -4.5; 66 -4.8; 72 -5.3; 79 -5.8; 87 -6.2; 96 -6.7; 106 -7.1; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.3; 170 -8.5; 187 -8.6; 206 -8.8; 227 -8.8; 249 -9.1; 274 -9.1; 302 -9.2; 332 -9.3; 365 -9.4; 402 -9.5; 442 -9.5; 486 -9.7; 535 -9.8; 588 -9.6; 647 -9.5; 712 -9.6; 783 -9.4; 861 -9.2; 947 -9.2; 1042 -9.0; 1146 -8.5; 1261 -8.8; 1387 -8.3; 1526 -8.1; 1678 -8.2; 1846 -7.7; 2031 -7.4; 2234 -6.8; 2457 -5.7; 2703 -4.7; 2973 -3.5; 3270 -2.8; 3597 -4.0; 3957 -5.6; 4353 -5.0; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.4; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Havi B3 Pro1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Havi B3 Pro1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.09 | 1.4 dB  |
| Peaking | 26 Hz   | 0.29 | 5.3 dB  |
| Peaking | 291 Hz  | 0.15 | -3.3 dB |
| Peaking | 3067 Hz | 2.91 | 4.1 dB  |
| Peaking | 5640 Hz | 2.78 | 7.0 dB  |
| Peaking | 4124 Hz | 7.83 | -1.6 dB |
| Peaking | 7023 Hz | 0.94 | 1.7 dB  |
| Peaking | 8404 Hz | 1.26 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Havi%20B3%20Pro1/Havi%20B3%20Pro1.png)