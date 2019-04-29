# Unique Melody Maestro V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.2; 25 -5.5; 28 -5.8; 31 -6.2; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.7; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.3; 96 -9.7; 106 -9.9; 116 -10.1; 128 -10.3; 141 -10.4; 155 -10.5; 170 -10.5; 187 -10.4; 206 -10.3; 227 -10.1; 249 -9.9; 274 -9.7; 302 -9.5; 332 -9.1; 365 -8.8; 402 -8.6; 442 -8.4; 486 -8.2; 535 -8.0; 588 -7.8; 647 -7.5; 712 -7.3; 783 -7.0; 861 -6.9; 947 -6.9; 1042 -7.3; 1146 -7.8; 1261 -8.2; 1387 -8.1; 1526 -7.6; 1678 -6.7; 1846 -5.7; 2031 -4.5; 2234 -3.2; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.4; 5267 -5.0; 5793 -8.0; 6373 -8.8; 7010 -6.7; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.2; 15026 -18.6; 16529 -24.4; 18182 -26.1; 20000 -19.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Maestro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Maestro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.76 | 3.3 dB   |
| Peaking | 255 Hz   | 0.08 | -3.4 dB  |
| Peaking | 6421 Hz  | 1.71 | -11.7 dB |
| Peaking | 6503 Hz  | 0.35 | 13.4 dB  |
| Peaking | 17613 Hz | 0.56 | -24.0 dB |
| Peaking | 825 Hz   | 1.02 | 2.5 dB   |
| Peaking | 1449 Hz  | 1.09 | -3.6 dB  |
| Peaking | 2720 Hz  | 1.54 | 2.2 dB   |
| Peaking | 9090 Hz  | 4.34 | -1.8 dB  |
| Peaking | 12659 Hz | 4.84 | 4.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -19.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%20Maestro%20V2/Unique%20Melody%20Maestro%20V2.png)