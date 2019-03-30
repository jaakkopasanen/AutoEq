# Sennheiser CX 300-II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.7; 23 -16.7; 25 -16.7; 28 -16.7; 31 -16.7; 34 -16.7; 37 -16.7; 41 -16.6; 45 -16.5; 49 -16.4; 54 -16.3; 60 -16.1; 66 -15.9; 72 -15.8; 79 -15.5; 87 -15.3; 96 -15.0; 106 -14.7; 116 -14.4; 128 -14.0; 141 -13.6; 155 -13.1; 170 -12.6; 187 -12.1; 206 -11.5; 227 -10.9; 249 -10.2; 274 -9.5; 302 -8.9; 332 -8.4; 365 -8.0; 402 -7.5; 442 -6.8; 486 -6.2; 535 -5.6; 588 -4.9; 647 -4.3; 712 -3.7; 783 -3.0; 861 -2.5; 947 -1.9; 1042 -1.5; 1146 -1.1; 1261 -0.7; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.7; 2031 -1.1; 2234 -1.8; 2457 -2.6; 2703 -3.9; 2973 -5.3; 3270 -6.3; 3597 -6.7; 3957 -6.6; 4353 -6.3; 4788 -6.1; 5267 -6.0; 5793 -7.7; 6373 -12.2; 7010 -13.7; 7711 -10.3; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 300-II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 300-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.05 | -10.1 dB |
| Peaking | 784 Hz  | 0.31 | 8.5 dB   |
| Peaking | 7110 Hz | 2.55 | -10.2 dB |
| Peaking | 8200 Hz | 2.95 | 4.3 dB   |
| Peaking | 32 Hz   | 1.33 | -0.5 dB  |
| Peaking | 625 Hz  | 1.52 | -1.1 dB  |
| Peaking | 1939 Hz | 1.04 | 1.7 dB   |
| Peaking | 3326 Hz | 1.92 | -3.2 dB  |
| Peaking | 5367 Hz | 5.87 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.8 dB |
| Peaking | 62 Hz    | 1.41 | -7.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX%20300-II/Sennheiser%20CX%20300-II.png)