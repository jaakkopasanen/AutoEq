# Audeze LCD-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.6; 25 -7.0; 28 -7.6; 31 -8.0; 34 -8.3; 37 -8.5; 41 -8.6; 45 -8.6; 49 -8.6; 54 -8.6; 60 -8.6; 66 -8.6; 72 -8.6; 79 -8.7; 87 -8.6; 96 -8.6; 106 -8.6; 116 -8.5; 128 -8.3; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.6; 206 -7.7; 227 -7.9; 249 -7.9; 274 -7.9; 302 -7.9; 332 -7.9; 365 -8.0; 402 -8.3; 442 -8.3; 486 -8.3; 535 -8.4; 588 -8.5; 647 -8.6; 712 -8.8; 783 -8.9; 861 -8.6; 947 -7.3; 1042 -5.9; 1146 -4.7; 1261 -4.0; 1387 -3.7; 1526 -3.6; 1678 -3.3; 1846 -2.8; 2031 -2.3; 2234 -1.9; 2457 -1.7; 2703 -1.2; 2973 -0.5; 3270 -1.1; 3597 -3.4; 3957 -4.5; 4353 -4.9; 4788 -5.7; 5267 -6.9; 5793 -8.0; 6373 -8.3; 7010 -8.7; 7711 -9.7; 8482 -10.0; 9330 -9.0; 10263 -7.7; 11289 -7.6; 12418 -8.7; 13660 -9.8; 15026 -10.4; 16529 -10.2; 18182 -9.0; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 73 Hz    | 0.4  | -2.1 dB |
| Peaking | 704 Hz   | 0.99 | -3.6 dB |
| Peaking | 2912 Hz  | 0.52 | 6.9 dB  |
| Peaking | 6364 Hz  | 0.81 | -5.5 dB |
| Peaking | 16176 Hz | 0.95 | -4.0 dB |
| Peaking | 1224 Hz  | 3.66 | 1.5 dB  |
| Peaking | 1819 Hz  | 0.62 | -0.7 dB |
| Peaking | 3025 Hz  | 6.35 | 1.8 dB  |
| Peaking | 8389 Hz  | 6.66 | -1.2 dB |
| Peaking | 10611 Hz | 4.5  | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20LCD-3/Audeze%20LCD-3.png)