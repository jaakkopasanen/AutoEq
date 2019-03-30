# Jays v-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.4; 49 -2.4; 54 -3.3; 60 -4.1; 66 -4.6; 72 -4.7; 79 -4.4; 87 -4.2; 96 -3.9; 106 -3.6; 116 -3.1; 128 -2.6; 141 -2.2; 155 -1.8; 170 -1.2; 187 -0.6; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.9; 332 -1.3; 365 -0.7; 402 -0.5; 442 -0.5; 486 -0.5; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -1.1; 1387 -2.2; 1526 -3.4; 1678 -4.7; 1846 -6.8; 2031 -9.2; 2234 -11.0; 2457 -11.5; 2703 -12.7; 2973 -15.2; 3270 -17.6; 3597 -19.5; 3957 -20.1; 4353 -19.4; 4788 -19.0; 5267 -21.4; 5793 -23.2; 6373 -23.1; 7010 -21.0; 7711 -17.1; 8482 -13.5; 9330 -12.8; 10263 -14.5; 11289 -15.6; 12418 -15.1; 13660 -12.8; 15026 -8.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays v-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays v-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 1    | 6.5 dB   |
| Peaking | 688 Hz   | 0.2  | 7.1 dB   |
| Peaking | 3507 Hz  | 0.99 | -13.6 dB |
| Peaking | 6226 Hz  | 1.8  | -13.2 dB |
| Peaking | 12057 Hz | 1.96 | -7.8 dB  |
| Peaking | 43 Hz    | 2.41 | 2.7 dB   |
| Peaking | 51 Hz    | 0.83 | -1.5 dB  |
| Peaking | 184 Hz   | 3.19 | 1.2 dB   |
| Peaking | 1238 Hz  | 3.19 | 1.7 dB   |
| Peaking | 2119 Hz  | 6.19 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | 2.6 dB   |
| Peaking | 250 Hz   | 1.41 | 5.2 dB   |
| Peaking | 500 Hz   | 1.41 | 4.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -14.8 dB |
| Peaking | 8000 Hz  | 1.41 | -10.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Jays%20v-Jays/Jays%20v-Jays.png)