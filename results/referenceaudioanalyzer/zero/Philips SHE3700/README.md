# Philips SHE3700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.4; 25 -7.6; 28 -7.8; 31 -8.0; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.3; 49 -8.3; 54 -8.2; 60 -8.1; 66 -8.0; 72 -8.0; 79 -7.9; 87 -7.7; 96 -7.6; 106 -7.3; 116 -7.1; 128 -6.9; 141 -6.6; 155 -6.3; 170 -6.0; 187 -5.7; 206 -5.3; 227 -4.9; 249 -4.5; 274 -4.1; 302 -3.6; 332 -3.2; 365 -2.7; 402 -2.3; 442 -2.1; 486 -1.8; 535 -1.5; 588 -1.2; 647 -0.9; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.8; 1526 -1.3; 1678 -1.9; 1846 -3.0; 2031 -4.6; 2234 -6.7; 2457 -9.1; 2703 -11.0; 2973 -11.4; 3270 -9.8; 3597 -7.2; 3957 -5.4; 4353 -5.0; 4788 -4.6; 5267 -4.6; 5793 -5.8; 6373 -7.0; 7010 -5.9; 7711 -3.5; 8482 -3.7; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE3700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE3700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.49 | -3.7 dB |
| Peaking | 109 Hz   | 0.57 | -2.6 dB |
| Peaking | 1075 Hz  | 0.48 | 4.2 dB  |
| Peaking | 2823 Hz  | 1.87 | -9.7 dB |
| Peaking | 21265 Hz | 2.17 | -0.8 dB |
| Peaking | 4313 Hz  | 3.13 | 0.9 dB  |
| Peaking | 6590 Hz  | 4.27 | -3.7 dB |
| Peaking | 6705 Hz  | 3.01 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHE3700/Philips%20SHE3700.png)