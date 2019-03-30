# Fischer Audio Oberon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.3; 72 -2.7; 79 -4.0; 87 -5.0; 96 -5.8; 106 -6.3; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.1; 170 -5.9; 187 -5.7; 206 -5.5; 227 -5.1; 249 -4.8; 274 -4.7; 302 -4.8; 332 -4.7; 365 -4.5; 402 -4.3; 442 -4.0; 486 -3.6; 535 -3.5; 588 -4.6; 647 -6.9; 712 -8.5; 783 -8.7; 861 -8.3; 947 -8.0; 1042 -8.0; 1146 -8.0; 1261 -8.0; 1387 -8.0; 1526 -7.7; 1678 -6.7; 1846 -5.8; 2031 -5.1; 2234 -4.5; 2457 -4.9; 2703 -5.9; 2973 -5.4; 3270 -3.2; 3597 -3.7; 3957 -5.9; 4353 -5.9; 4788 -3.6; 5267 -3.5; 5793 -6.0; 6373 -8.1; 7010 -9.4; 7711 -11.9; 8482 -15.3; 9330 -17.4; 10263 -16.5; 11289 -12.9; 12418 -9.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Oberon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Oberon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 0.72 | 7.0 dB   |
| Peaking | 426 Hz  | 2.24 | 2.9 dB   |
| Peaking | 3364 Hz | 4.54 | 3.7 dB   |
| Peaking | 5145 Hz | 4.42 | 4.6 dB   |
| Peaking | 9481 Hz | 2.05 | -11.9 dB |
| Peaking | 62 Hz   | 4.18 | 2.2 dB   |
| Peaking | 107 Hz  | 2.52 | -1.6 dB  |
| Peaking | 774 Hz  | 4.82 | -2.5 dB  |
| Peaking | 1246 Hz | 1.97 | -1.8 dB  |
| Peaking | 2176 Hz | 3.96 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Oberon/Fischer%20Audio%20Oberon.png)