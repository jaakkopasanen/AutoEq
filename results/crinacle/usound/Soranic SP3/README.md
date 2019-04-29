# Soranic SP3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.5; 25 -3.7; 28 -4.0; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.5; 45 -4.6; 49 -4.7; 54 -4.9; 60 -5.0; 66 -5.3; 72 -5.5; 79 -5.8; 87 -6.1; 96 -6.4; 106 -6.7; 116 -7.0; 128 -7.2; 141 -7.4; 155 -7.5; 170 -7.7; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.7; 274 -7.6; 302 -7.4; 332 -7.3; 365 -7.1; 402 -6.8; 442 -6.6; 486 -6.3; 535 -6.0; 588 -5.7; 647 -5.3; 712 -4.9; 783 -4.5; 861 -4.2; 947 -4.2; 1042 -4.6; 1146 -5.5; 1261 -6.5; 1387 -7.3; 1526 -7.8; 1678 -7.8; 1846 -7.2; 2031 -6.2; 2234 -5.4; 2457 -4.1; 2703 -2.3; 2973 -1.0; 3270 -0.5; 3597 -0.7; 3957 -0.8; 4353 -1.5; 4788 -3.3; 5267 -5.8; 5793 -7.4; 6373 -9.0; 7010 -10.4; 7711 -10.6; 8482 -6.3; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -12.5; 15026 -17.1; 16529 -10.5; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soranic SP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soranic SP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.38 | 2.5 dB   |
| Peaking | 1735 Hz  | 2.38 | -3.4 dB  |
| Peaking | 3508 Hz  | 1.29 | 6.1 dB   |
| Peaking | 6915 Hz  | 2.85 | -6.1 dB  |
| Peaking | 15015 Hz | 3.04 | -12.9 dB |
| Peaking | 219 Hz   | 0.79 | -2.2 dB  |
| Peaking | 857 Hz   | 2.59 | 2.0 dB   |
| Peaking | 5500 Hz  | 8.15 | -1.4 dB  |
| Peaking | 12517 Hz | 1.88 | 2.7 dB   |
| Peaking | 13901 Hz | 5.41 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -7.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Soranic%20SP3/Soranic%20SP3.png)