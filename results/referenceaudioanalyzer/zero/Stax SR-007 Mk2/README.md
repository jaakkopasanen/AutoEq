# Stax SR-007 Mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -2.3; 60 -5.6; 66 -8.6; 72 -10.9; 79 -12.5; 87 -13.2; 96 -12.9; 106 -12.2; 116 -11.3; 128 -10.4; 141 -9.5; 155 -8.7; 170 -8.3; 187 -7.9; 206 -7.6; 227 -7.4; 249 -7.4; 274 -7.2; 302 -7.1; 332 -7.1; 365 -7.3; 402 -7.6; 442 -7.8; 486 -7.6; 535 -6.9; 588 -6.5; 647 -7.2; 712 -8.1; 783 -8.7; 861 -9.0; 947 -9.3; 1042 -9.7; 1146 -9.2; 1261 -6.6; 1387 -4.1; 1526 -5.1; 1678 -5.9; 1846 -4.4; 2031 -2.5; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.8; 3270 -1.2; 3597 -1.9; 3957 -2.7; 4353 -3.7; 4788 -5.5; 5267 -7.0; 5793 -7.1; 6373 -6.9; 7010 -7.2; 7711 -6.9; 8482 -6.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 Mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 49 Hz   | 0.51 | 13.3 dB  |
| Peaking | 83 Hz   | 0.91 | -16.2 dB |
| Peaking | 963 Hz  | 2.35 | -3.7 dB  |
| Peaking | 2466 Hz | 1.82 | 5.9 dB   |
| Peaking | 3527 Hz | 3.08 | 3.1 dB   |
| Peaking | 1170 Hz | 4.98 | -2.5 dB  |
| Peaking | 1381 Hz | 3.02 | 3.4 dB   |
| Peaking | 1643 Hz | 4.89 | -2.4 dB  |
| Peaking | 6148 Hz | 2.49 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 9.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Stax%20SR-007%20Mk2/Stax%20SR-007%20Mk2.png)