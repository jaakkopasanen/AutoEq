# Behringer HPS5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.9; 128 -1.5; 141 -1.8; 155 -2.2; 170 -2.3; 187 -2.4; 206 -2.7; 227 -2.7; 249 -2.7; 274 -2.4; 302 -1.9; 332 -2.0; 365 -2.0; 402 -2.1; 442 -3.1; 486 -3.2; 535 -3.2; 588 -3.0; 647 -3.2; 712 -3.6; 783 -4.1; 861 -5.2; 947 -6.1; 1042 -6.7; 1146 -7.3; 1261 -7.1; 1387 -8.4; 1526 -10.2; 1678 -10.1; 1846 -9.0; 2031 -6.4; 2234 -3.8; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Behringer HPS5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Behringer HPS5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.21 | 6.3 dB  |
| Peaking | 358 Hz  | 1.76 | 2.6 dB  |
| Peaking | 635 Hz  | 2.5  | 2.3 dB  |
| Peaking | 1657 Hz | 1.92 | -7.8 dB |
| Peaking | 3276 Hz | 0.71 | 7.6 dB  |
| Peaking | 1040 Hz | 6.72 | -0.8 dB |
| Peaking | 2514 Hz | 7.14 | 1.7 dB  |
| Peaking | 3478 Hz | 2.57 | -1.0 dB |
| Peaking | 6281 Hz | 2.28 | 5.6 dB  |
| Peaking | 7307 Hz | 1.41 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 3.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Behringer%20HPS5000/Behringer%20HPS5000.png)