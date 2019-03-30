# Nakamichi NEP-MV5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.2; 34 -2.1; 37 -2.8; 41 -3.6; 45 -4.4; 49 -5.0; 54 -5.6; 60 -6.2; 66 -6.6; 72 -7.0; 79 -7.3; 87 -7.5; 96 -7.8; 106 -8.0; 116 -8.1; 128 -8.1; 141 -8.1; 155 -8.1; 170 -8.1; 187 -8.1; 206 -8.0; 227 -7.8; 249 -7.9; 274 -8.1; 302 -8.1; 332 -8.1; 365 -8.1; 402 -7.9; 442 -7.8; 486 -7.8; 535 -7.6; 588 -7.3; 647 -6.9; 712 -6.4; 783 -5.7; 861 -5.1; 947 -4.3; 1042 -3.5; 1146 -2.5; 1261 -1.7; 1387 -1.3; 1526 -1.4; 1678 -1.8; 1846 -2.5; 2031 -3.3; 2234 -4.1; 2457 -4.9; 2703 -5.7; 2973 -6.5; 3270 -7.3; 3597 -7.4; 3957 -6.5; 4353 -5.4; 4788 -5.2; 5267 -6.2; 5793 -9.1; 6373 -11.5; 7010 -10.9; 7711 -8.0; 8482 -6.9; 9330 -8.4; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nakamichi NEP-MV5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nakamichi NEP-MV5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.85 | 7.4 dB  |
| Peaking | 258 Hz  | 0.09 | -2.0 dB |
| Peaking | 1415 Hz | 1.08 | 7.0 dB  |
| Peaking | 6592 Hz | 4.81 | -5.8 dB |
| Peaking | 9747 Hz | 7.27 | -2.3 dB |
| Peaking | 104 Hz  | 1.22 | -0.8 dB |
| Peaking | 110 Hz  | 0.6  | 0.6 dB  |
| Peaking | 3479 Hz | 3.69 | -2.0 dB |
| Peaking | 4760 Hz | 2.33 | 2.2 dB  |
| Peaking | 5894 Hz | 6.98 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Nakamichi%20NEP-MV5/Nakamichi%20NEP-MV5.png)