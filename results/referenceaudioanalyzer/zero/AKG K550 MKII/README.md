# AKG K550 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.1; 25 -10.9; 28 -10.5; 31 -10.2; 34 -9.8; 37 -9.5; 41 -8.9; 45 -8.2; 49 -7.4; 54 -6.5; 60 -5.8; 66 -5.9; 72 -6.6; 79 -7.7; 87 -8.8; 96 -9.6; 106 -9.9; 116 -9.9; 128 -9.7; 141 -9.4; 155 -8.8; 170 -7.8; 187 -6.6; 206 -5.4; 227 -4.8; 249 -4.6; 274 -4.4; 302 -4.4; 332 -4.4; 365 -4.4; 402 -4.4; 442 -4.3; 486 -4.1; 535 -4.0; 588 -3.8; 647 -3.6; 712 -3.2; 783 -2.7; 861 -2.2; 947 -1.5; 1042 -1.0; 1146 -0.7; 1261 -0.5; 1387 -0.9; 1526 -1.5; 1678 -1.7; 1846 -1.4; 2031 -1.3; 2234 -2.0; 2457 -3.2; 2703 -4.4; 2973 -4.9; 3270 -4.4; 3597 -3.4; 3957 -2.6; 4353 -2.5; 4788 -4.8; 5267 -9.1; 5793 -12.5; 6373 -13.4; 7010 -10.7; 7711 -5.5; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -5.6; 12418 -6.3; 13660 -5.0; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K550 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K550 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.99 | -6.6 dB  |
| Peaking | 118 Hz   | 1.54 | -5.5 dB  |
| Peaking | 1301 Hz  | 0.89 | 4.1 dB   |
| Peaking | 4299 Hz  | 4.48 | 3.7 dB   |
| Peaking | 6122 Hz  | 3.18 | -10.1 dB |
| Peaking | 61 Hz    | 5.99 | 1.3 dB   |
| Peaking | 2098 Hz  | 5.82 | 1.3 dB   |
| Peaking | 2861 Hz  | 5.38 | -1.5 dB  |
| Peaking | 8258 Hz  | 6.05 | 2.0 dB   |
| Peaking | 12380 Hz | 5.23 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K550%20MKII/AKG%20K550%20MKII.png)