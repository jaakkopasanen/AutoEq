# Sennheiser PX 90
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -2.1; 54 -3.6; 60 -4.7; 66 -5.2; 72 -5.5; 79 -5.6; 87 -5.5; 96 -5.3; 106 -5.0; 116 -4.6; 128 -4.2; 141 -3.7; 155 -3.3; 170 -3.0; 187 -2.7; 206 -2.5; 227 -2.5; 249 -2.5; 274 -2.1; 302 -1.7; 332 -1.4; 365 -1.2; 402 -1.2; 442 -1.2; 486 -1.2; 535 -1.2; 588 -1.3; 647 -1.6; 712 -1.9; 783 -2.2; 861 -2.5; 947 -2.8; 1042 -3.2; 1146 -3.8; 1261 -4.4; 1387 -5.1; 1526 -5.8; 1678 -6.8; 1846 -7.8; 2031 -9.1; 2234 -10.6; 2457 -12.3; 2703 -14.7; 2973 -17.5; 3270 -18.7; 3597 -17.5; 3957 -14.3; 4353 -10.9; 4788 -7.9; 5267 -6.5; 5793 -7.3; 6373 -9.0; 7010 -11.1; 7711 -13.7; 8482 -16.2; 9330 -17.7; 10263 -17.5; 11289 -15.2; 12418 -11.7; 13660 -9.3; 15026 -8.6; 16529 -6.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PX 90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.02 | 6.8 dB   |
| Peaking | 461 Hz   | 0.44 | 5.6 dB   |
| Peaking | 3147 Hz  | 2.24 | -13.2 dB |
| Peaking | 9858 Hz  | 1.78 | -12.2 dB |
| Peaking | 78 Hz    | 3.5  | -1.2 dB  |
| Peaking | 3797 Hz  | 5.52 | -2.7 dB  |
| Peaking | 5282 Hz  | 3.04 | 3.9 dB   |
| Peaking | 7947 Hz  | 4.5  | -2.2 dB  |
| Peaking | 17516 Hz | 3.58 | 0.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20PX%2090/Sennheiser%20PX%2090.png)