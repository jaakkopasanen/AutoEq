# Jays s-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.4; 25 -12.4; 28 -12.4; 31 -12.5; 34 -12.6; 37 -12.7; 41 -12.7; 45 -12.7; 49 -12.7; 54 -12.7; 60 -12.7; 66 -12.7; 72 -12.7; 79 -12.7; 87 -12.7; 96 -12.7; 106 -12.7; 116 -12.5; 128 -12.4; 141 -12.4; 155 -12.1; 170 -12.1; 187 -12.4; 206 -12.7; 227 -12.8; 249 -12.8; 274 -12.7; 302 -12.4; 332 -12.1; 365 -11.8; 402 -11.5; 442 -11.2; 486 -10.8; 535 -10.5; 588 -10.1; 647 -9.7; 712 -9.3; 783 -8.8; 861 -8.5; 947 -8.0; 1042 -7.6; 1146 -7.3; 1261 -7.0; 1387 -6.9; 1526 -6.9; 1678 -6.9; 1846 -7.6; 2031 -8.9; 2234 -10.4; 2457 -11.8; 2703 -12.0; 2973 -10.0; 3270 -6.0; 3597 -2.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays s-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays s-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.48 | -4.3 dB |
| Peaking | 75 Hz   | 0.43 | -4.6 dB |
| Peaking | 322 Hz  | 0.6  | -4.7 dB |
| Peaking | 2664 Hz | 2.48 | -9.0 dB |
| Peaking | 4370 Hz | 1.22 | 8.2 dB  |
| Peaking | 1232 Hz | 0.88 | -0.8 dB |
| Peaking | 1338 Hz | 1.61 | 1.5 dB  |
| Peaking | 6372 Hz | 3.66 | 4.0 dB  |
| Peaking | 7428 Hz | 2.56 | -1.8 dB |
| Peaking | 7782 Hz | 0.95 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Jays%20s-Jays/Jays%20s-Jays.png)