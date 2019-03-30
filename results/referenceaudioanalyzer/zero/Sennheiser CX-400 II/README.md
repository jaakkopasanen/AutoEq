# Sennheiser CX-400 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.8; 25 -15.9; 28 -16.1; 31 -16.1; 34 -16.1; 37 -16.1; 41 -16.1; 45 -16.1; 49 -16.1; 54 -16.1; 60 -16.0; 66 -15.8; 72 -15.7; 79 -15.5; 87 -15.2; 96 -15.0; 106 -14.7; 116 -14.4; 128 -14.0; 141 -13.6; 155 -13.1; 170 -12.6; 187 -12.2; 206 -11.6; 227 -11.0; 249 -10.4; 274 -9.8; 302 -9.0; 332 -8.4; 365 -7.6; 402 -7.0; 442 -6.5; 486 -6.0; 535 -5.4; 588 -4.7; 647 -4.0; 712 -3.3; 783 -2.7; 861 -2.0; 947 -1.4; 1042 -0.8; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.8; 2457 -2.0; 2703 -3.5; 2973 -5.1; 3270 -6.5; 3597 -7.3; 3957 -7.3; 4353 -6.8; 4788 -6.1; 5267 -6.1; 5793 -8.2; 6373 -13.4; 7010 -15.4; 7711 -12.2; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX-400 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX-400 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 40 Hz    |  0.16 | -9.7 dB  |
| Peaking | 2101 Hz  |  0.31 | 7.8 dB   |
| Peaking | 3543 Hz  |  1.57 | -7.1 dB  |
| Peaking | 6910 Hz  |  3.23 | -12.4 dB |
| Peaking | 12523 Hz |  2.27 | -0.7 dB  |
| Peaking | 536 Hz   |  4.86 | -0.3 dB  |
| Peaking | 7685 Hz  | 11.25 | -1.7 dB  |
| Peaking | 8474 Hz  |  8.32 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.9 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX-400%20II/Sennheiser%20CX-400%20II.png)