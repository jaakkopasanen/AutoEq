# AKG Y50BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.5; 25 -9.1; 28 -9.7; 31 -10.2; 34 -10.6; 37 -10.9; 41 -11.2; 45 -11.2; 49 -11.1; 54 -10.8; 60 -10.3; 66 -9.7; 72 -9.2; 79 -9.0; 87 -8.7; 96 -8.3; 106 -7.7; 116 -6.8; 128 -5.4; 141 -3.6; 155 -1.9; 170 -0.8; 187 -0.5; 206 -0.9; 227 -2.4; 249 -4.6; 274 -6.7; 302 -8.1; 332 -8.8; 365 -9.0; 402 -8.7; 442 -8.6; 486 -8.8; 535 -8.9; 588 -9.1; 647 -9.4; 712 -9.6; 783 -9.9; 861 -10.1; 947 -10.3; 1042 -10.5; 1146 -10.3; 1261 -9.8; 1387 -9.3; 1526 -8.7; 1678 -7.9; 1846 -6.9; 2031 -5.8; 2234 -4.6; 2457 -3.6; 2703 -3.1; 2973 -3.2; 3270 -3.7; 3597 -4.6; 3957 -5.6; 4353 -6.0; 4788 -5.9; 5267 -7.2; 5793 -9.1; 6373 -9.9; 7010 -9.0; 7711 -6.7; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.64 | -4.7 dB |
| Peaking | 184 Hz  | 1.79 | 8.7 dB  |
| Peaking | 933 Hz  | 0.29 | -4.2 dB |
| Peaking | 2706 Hz | 1.31 | 6.2 dB  |
| Peaking | 6281 Hz | 4.16 | -3.9 dB |
| Peaking | 234 Hz  | 5.52 | 1.4 dB  |
| Peaking | 331 Hz  | 1.59 | -2.1 dB |
| Peaking | 428 Hz  | 2.09 | 0.9 dB  |
| Peaking | 749 Hz  | 0.62 | 1.2 dB  |
| Peaking | 1049 Hz | 1.41 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | 2.7 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -4.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20Y50BT/AKG%20Y50BT.png)