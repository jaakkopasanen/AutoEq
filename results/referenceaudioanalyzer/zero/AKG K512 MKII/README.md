# AKG K512 MKII
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.2; 60 -2.0; 66 -2.7; 72 -3.2; 79 -3.5; 87 -3.8; 96 -4.0; 106 -4.2; 116 -4.4; 128 -4.4; 141 -4.3; 155 -4.0; 170 -3.8; 187 -3.6; 206 -3.1; 227 -2.7; 249 -2.4; 274 -2.1; 302 -1.8; 332 -1.8; 365 -1.6; 402 -1.3; 442 -0.8; 486 -0.5; 535 -0.5; 588 -0.5; 647 -1.0; 712 -4.1; 783 -5.6; 861 -6.1; 947 -6.5; 1042 -6.9; 1146 -7.4; 1261 -7.7; 1387 -7.9; 1526 -8.1; 1678 -8.0; 1846 -7.5; 2031 -6.7; 2234 -5.7; 2457 -4.9; 2703 -4.2; 2973 -4.1; 3270 -4.7; 3597 -4.7; 3957 -6.4; 4353 -11.3; 4788 -14.5; 5267 -14.3; 5793 -12.9; 6373 -15.9; 7010 -19.4; 7711 -20.8; 8482 -20.1; 9330 -18.8; 10263 -18.2; 11289 -18.0; 12418 -16.4; 13660 -12.5; 15026 -8.6; 16529 -7.2; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K512 MKII GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K512 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.55 | 6.4 dB   |
| Peaking | 503 Hz   | 0.64 | 9.8 dB   |
| Peaking | 2253 Hz  | 0.2  | -7.5 dB  |
| Peaking | 3023 Hz  | 1.04 | 11.5 dB  |
| Peaking | 8703 Hz  | 0.79 | -11.0 dB |
| Peaking | 3850 Hz  | 5.39 | 4.3 dB   |
| Peaking | 5667 Hz  | 1.01 | -10.0 dB |
| Peaking | 5859 Hz  | 4    | 8.3 dB   |
| Peaking | 9209 Hz  | 0.36 | 5.5 dB   |
| Peaking | 12205 Hz | 2.15 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB   |
| Peaking | 62 Hz    | 1.41 | 3.0 dB   |
| Peaking | 125 Hz   | 1.41 | 0.7 dB   |
| Peaking | 250 Hz   | 1.41 | 2.9 dB   |
| Peaking | 500 Hz   | 1.41 | 6.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -18.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K512%20MKII/AKG%20K512%20MKII.png)