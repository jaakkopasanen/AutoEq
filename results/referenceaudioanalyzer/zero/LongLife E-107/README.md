# LongLife E-107
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.0; 25 -13.0; 28 -13.0; 31 -13.0; 34 -13.0; 37 -13.0; 41 -13.1; 45 -13.2; 49 -13.3; 54 -13.3; 60 -13.2; 66 -13.3; 72 -13.3; 79 -13.3; 87 -13.3; 96 -13.3; 106 -13.3; 116 -13.4; 128 -13.6; 141 -13.6; 155 -13.6; 170 -13.8; 187 -14.0; 206 -14.2; 227 -14.4; 249 -14.7; 274 -15.1; 302 -15.5; 332 -16.1; 365 -16.9; 402 -17.8; 442 -19.0; 486 -20.4; 535 -21.9; 588 -22.7; 647 -22.2; 712 -20.1; 783 -16.9; 861 -13.5; 947 -10.3; 1042 -7.4; 1146 -5.0; 1261 -2.6; 1387 -0.6; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -3.1; 5793 -5.7; 6373 -9.0; 7010 -7.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`LongLife E-107 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LongLife E-107 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 61 Hz    | 0.11 | -6.7 dB  |
| Peaking | 567 Hz   | 0.85 | -5.9 dB  |
| Peaking | 653 Hz   | 1.15 | -13.5 dB |
| Peaking | 1460 Hz  | 0.47 | 10.7 dB  |
| Peaking | 20683 Hz | 1.73 | -0.7 dB  |
| Peaking | 13 Hz    | 1.69 | -1.0 dB  |
| Peaking | 1379 Hz  | 3.64 | 2.2 dB   |
| Peaking | 1679 Hz  | 1.04 | -1.4 dB  |
| Peaking | 4429 Hz  | 1.77 | 3.1 dB   |
| Peaking | 6522 Hz  | 3.6  | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -17.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/LongLife%20E-107/LongLife%20E-107.png)