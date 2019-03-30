# JVC Esnsy HA-FX45
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -12.1; 25 -12.4; 28 -12.8; 31 -13.1; 34 -13.3; 37 -13.5; 41 -13.6; 45 -13.7; 49 -13.7; 54 -13.7; 60 -13.6; 66 -13.5; 72 -13.3; 79 -13.1; 87 -12.9; 96 -12.6; 106 -12.4; 116 -12.0; 128 -11.7; 141 -11.2; 155 -10.6; 170 -10.0; 187 -9.4; 206 -8.9; 227 -8.8; 249 -8.7; 274 -8.5; 302 -7.9; 332 -7.3; 365 -6.6; 402 -5.9; 442 -5.3; 486 -4.6; 535 -3.9; 588 -3.2; 647 -2.4; 712 -1.8; 783 -1.2; 861 -0.7; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.6; 1846 -1.3; 2031 -2.3; 2234 -3.6; 2457 -5.2; 2703 -7.5; 2973 -10.4; 3270 -13.7; 3597 -15.7; 3957 -15.6; 4353 -13.7; 4788 -11.7; 5267 -10.8; 5793 -10.8; 6373 -10.6; 7010 -9.0; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC Esnsy HA-FX45 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC Esnsy HA-FX45 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 51 Hz   | 0.46 | -3.6 dB  |
| Peaking | 59 Hz   | 0.14 | -3.8 dB  |
| Peaking | 1870 Hz | 0.35 | 10.7 dB  |
| Peaking | 3703 Hz | 1.07 | -17.4 dB |
| Peaking | 197 Hz  | 6.66 | 0.6 dB   |
| Peaking | 1267 Hz | 1.09 | 1.0 dB   |
| Peaking | 1270 Hz | 2.25 | -1.7 dB  |
| Peaking | 6475 Hz | 3.82 | -3.4 dB  |
| Peaking | 7454 Hz | 1.92 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20Esnsy%20HA-FX45/JVC%20Esnsy%20HA-FX45.png)