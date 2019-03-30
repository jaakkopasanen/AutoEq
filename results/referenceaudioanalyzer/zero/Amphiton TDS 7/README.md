# Amphiton TDS 7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -2.3; 45 -3.6; 49 -4.8; 54 -6.0; 60 -7.2; 66 -8.2; 72 -8.7; 79 -9.0; 87 -8.9; 96 -8.4; 106 -7.8; 116 -7.4; 128 -7.2; 141 -7.0; 155 -6.9; 170 -6.7; 187 -6.7; 206 -6.8; 227 -7.1; 249 -7.4; 274 -7.6; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.3; 442 -7.1; 486 -7.0; 535 -7.3; 588 -7.3; 647 -7.0; 712 -6.5; 783 -6.3; 861 -6.5; 947 -7.1; 1042 -7.9; 1146 -8.6; 1261 -9.2; 1387 -9.8; 1526 -9.9; 1678 -9.3; 1846 -8.7; 2031 -7.9; 2234 -7.1; 2457 -6.7; 2703 -6.9; 2973 -7.9; 3270 -9.0; 3597 -9.3; 3957 -8.5; 4353 -7.0; 4788 -5.3; 5267 -3.3; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Amphiton TDS 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Amphiton TDS 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.61 | 7.9 dB  |
| Peaking | 67 Hz   | 0.92 | -5.7 dB |
| Peaking | 1456 Hz | 2.07 | -3.6 dB |
| Peaking | 3602 Hz | 3.51 | -3.3 dB |
| Peaking | 6015 Hz | 3.42 | 6.3 dB  |
| Peaking | 304 Hz  | 2.9  | -1.0 dB |
| Peaking | 612 Hz  | 1.51 | -0.8 dB |
| Peaking | 778 Hz  | 3.25 | 1.2 dB  |
| Peaking | 8021 Hz | 5.36 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Amphiton%20TDS%207/Amphiton%20TDS%207.png)