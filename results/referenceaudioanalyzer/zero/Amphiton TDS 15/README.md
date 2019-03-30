# Amphiton TDS 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.7; 34 -3.1; 37 -3.4; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.5; 60 -4.6; 66 -4.8; 72 -4.9; 79 -4.9; 87 -5.0; 96 -5.2; 106 -5.2; 116 -5.2; 128 -5.5; 141 -5.7; 155 -5.9; 170 -5.9; 187 -5.9; 206 -5.9; 227 -5.9; 249 -5.9; 274 -5.9; 302 -5.9; 332 -6.0; 365 -6.2; 402 -6.5; 442 -6.5; 486 -6.6; 535 -7.0; 588 -7.3; 647 -7.5; 712 -7.7; 783 -8.1; 861 -8.2; 947 -8.5; 1042 -8.8; 1146 -8.5; 1261 -8.1; 1387 -8.2; 1526 -8.0; 1678 -7.5; 1846 -6.6; 2031 -5.4; 2234 -4.7; 2457 -4.2; 2703 -3.5; 2973 -3.2; 3270 -3.4; 3597 -4.5; 3957 -6.3; 4353 -7.6; 4788 -7.8; 5267 -7.5; 5793 -7.5; 6373 -7.7; 7010 -7.0; 7711 -5.9; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Amphiton TDS 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Amphiton TDS 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.59 | 6.4 dB  |
| Peaking | 81 Hz   | 0.09 | 0.5 dB  |
| Peaking | 1221 Hz | 0.67 | -3.4 dB |
| Peaking | 3117 Hz | 1.04 | 6.0 dB  |
| Peaking | 4522 Hz | 1.39 | -4.6 dB |
| Peaking | 13 Hz   | 0.25 | 0.1 dB  |
| Peaking | 6628 Hz | 5.39 | -1.7 dB |
| Peaking | 7096 Hz | 2.59 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Amphiton%20TDS%2015/Amphiton%20TDS%2015.png)