# Sennheiser MM 80i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.8; 25 -8.4; 28 -9.2; 31 -9.8; 34 -10.3; 37 -10.7; 41 -11.1; 45 -11.4; 49 -11.7; 54 -12.0; 60 -12.2; 66 -12.3; 72 -12.3; 79 -12.5; 87 -12.6; 96 -12.4; 106 -12.3; 116 -12.3; 128 -12.0; 141 -11.9; 155 -11.7; 170 -11.4; 187 -11.1; 206 -10.8; 227 -10.5; 249 -10.3; 274 -10.1; 302 -10.0; 332 -9.7; 365 -9.2; 402 -8.6; 442 -7.9; 486 -7.3; 535 -6.6; 588 -5.8; 647 -5.1; 712 -4.4; 783 -3.7; 861 -3.0; 947 -2.4; 1042 -1.7; 1146 -1.1; 1261 -0.6; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.7; 2457 -2.0; 2703 -3.9; 2973 -6.4; 3270 -8.0; 3597 -8.4; 3957 -7.9; 4353 -7.4; 4788 -7.8; 5267 -10.9; 5793 -15.0; 6373 -15.2; 7010 -10.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 80i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 80i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 110 Hz  | 0.25 | -5.9 dB  |
| Peaking | 1958 Hz | 0.41 | 7.8 dB   |
| Peaking | 3337 Hz | 2.14 | -7.0 dB  |
| Peaking | 6148 Hz | 2.52 | -12.5 dB |
| Peaking | 7564 Hz | 4.79 | 3.6 dB   |
| Peaking | 18 Hz   | 1.34 | 2.4 dB   |
| Peaking | 68 Hz   | 0.38 | -0.8 dB  |
| Peaking | 286 Hz  | 0.52 | 1.8 dB   |
| Peaking | 372 Hz  | 1.03 | -1.9 dB  |
| Peaking | 1658 Hz | 5.83 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20MM%2080i/Sennheiser%20MM%2080i.png)