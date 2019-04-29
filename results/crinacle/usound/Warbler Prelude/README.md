# Warbler Prelude
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.7; 34 -2.3; 37 -2.8; 41 -3.4; 45 -4.0; 49 -4.5; 54 -5.0; 60 -5.5; 66 -6.0; 72 -6.6; 79 -7.2; 87 -7.7; 96 -8.2; 106 -8.8; 116 -9.2; 128 -9.7; 141 -10.1; 155 -10.3; 170 -10.6; 187 -10.8; 206 -11.0; 227 -11.1; 249 -11.0; 274 -11.0; 302 -11.0; 332 -11.0; 365 -10.8; 402 -10.6; 442 -10.5; 486 -10.3; 535 -10.0; 588 -9.6; 647 -9.2; 712 -8.7; 783 -8.2; 861 -7.7; 947 -7.4; 1042 -7.5; 1146 -7.9; 1261 -8.5; 1387 -8.7; 1526 -8.4; 1678 -7.6; 1846 -6.7; 2031 -6.0; 2234 -5.6; 2457 -5.6; 2703 -6.0; 2973 -6.6; 3270 -6.7; 3597 -5.1; 3957 -2.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Warbler Prelude GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Warbler Prelude ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.54 | 6.3 dB  |
| Peaking | 233 Hz  | 0.46 | -4.1 dB |
| Peaking | 1343 Hz | 0.05 | -0.8 dB |
| Peaking | 5150 Hz | 1.63 | 7.7 dB  |
| Peaking | 970 Hz  | 3.43 | 1.2 dB  |
| Peaking | 1416 Hz | 1.95 | -2.0 dB |
| Peaking | 2648 Hz | 0.93 | 2.3 dB  |
| Peaking | 3175 Hz | 3.15 | -3.4 dB |
| Peaking | 7958 Hz | 5.23 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Warbler%20Prelude/Warbler%20Prelude.png)