# Lime Ears LE2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.2; 25 -5.3; 28 -5.5; 31 -5.6; 34 -5.7; 37 -5.9; 41 -6.1; 45 -6.4; 49 -6.6; 54 -6.8; 60 -7.0; 66 -7.3; 72 -7.6; 79 -8.0; 87 -8.3; 96 -8.9; 106 -9.4; 116 -9.7; 128 -10.0; 141 -10.4; 155 -10.6; 170 -10.9; 187 -11.0; 206 -11.1; 227 -11.1; 249 -11.1; 274 -11.0; 302 -10.9; 332 -10.6; 365 -10.4; 402 -10.2; 442 -10.0; 486 -9.7; 535 -9.2; 588 -8.8; 647 -8.4; 712 -7.9; 783 -7.5; 861 -7.1; 947 -7.0; 1042 -7.3; 1146 -7.9; 1261 -8.4; 1387 -8.6; 1526 -8.6; 1678 -8.6; 1846 -8.9; 2031 -8.9; 2234 -7.5; 2457 -4.5; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.8; 5793 -2.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.8; 15026 -22.6; 16529 -28.8; 18182 -28.3; 20000 -21.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears LE2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears LE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 326 Hz   | 0.38 | -6.0 dB  |
| Peaking | 1876 Hz  | 0.83 | -14.2 dB |
| Peaking | 3206 Hz  | 0.34 | 19.5 dB  |
| Peaking | 12588 Hz | 1.03 | 16.9 dB  |
| Peaking | 16383 Hz | 0.33 | -31.5 dB |
| Peaking | 26 Hz    | 0.88 | 1.5 dB   |
| Peaking | 2214 Hz  | 7.59 | -1.5 dB  |
| Peaking | 2725 Hz  | 8.78 | 1.7 dB   |
| Peaking | 5376 Hz  | 8.73 | -3.7 dB  |
| Peaking | 6275 Hz  | 7.75 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | -0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 16000 Hz | 1.41 | -24.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20LE2/Lime%20Ears%20LE2.png)