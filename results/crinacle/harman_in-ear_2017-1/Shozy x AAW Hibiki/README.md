# Shozy x AAW Hibiki
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.6; 25 -5.0; 28 -5.6; 31 -6.1; 34 -6.5; 37 -6.8; 41 -7.2; 45 -7.5; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.9; 79 -9.2; 87 -9.5; 96 -9.8; 106 -10.0; 116 -10.2; 128 -10.4; 141 -10.6; 155 -10.7; 170 -10.7; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.5; 274 -10.3; 302 -10.1; 332 -9.7; 365 -9.4; 402 -9.0; 442 -8.7; 486 -8.2; 535 -7.7; 588 -7.2; 647 -6.5; 712 -5.8; 783 -5.2; 861 -4.6; 947 -4.1; 1042 -4.2; 1146 -4.6; 1261 -4.9; 1387 -5.0; 1526 -4.8; 1678 -4.6; 1846 -4.6; 2031 -4.7; 2234 -5.1; 2457 -5.8; 2703 -6.0; 2973 -5.2; 3270 -4.4; 3597 -4.8; 3957 -7.0; 4353 -10.6; 4788 -8.3; 5267 -2.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -13.0; 16529 -21.2; 18182 -24.2; 20000 -19.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy x AAW Hibiki GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy x AAW Hibiki ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 2.02 | 2.6 dB   |
| Peaking | 167 Hz   | 0.54 | -4.6 dB  |
| Peaking | 4379 Hz  | 5.2  | -8.8 dB  |
| Peaking | 9858 Hz  | 0.24 | 6.5 dB   |
| Peaking | 18159 Hz | 0.62 | -22.8 dB |
| Peaking | 957 Hz   | 2.32 | 2.3 dB   |
| Peaking | 2660 Hz  | 4.14 | -2.2 dB  |
| Peaking | 6112 Hz  | 3.27 | 5.7 dB   |
| Peaking | 7519 Hz  | 1.41 | -3.7 dB  |
| Peaking | 13534 Hz | 3.74 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -14.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20x%20AAW%20Hibiki/Shozy%20x%20AAW%20Hibiki.png)