# Vision Ears VE6X2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.2; 31 -5.4; 34 -5.6; 37 -5.7; 41 -5.9; 45 -5.9; 49 -6.0; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.0; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.2; 128 -9.5; 141 -9.8; 155 -10.1; 170 -10.3; 187 -10.5; 206 -10.6; 227 -10.6; 249 -10.7; 274 -10.7; 302 -10.5; 332 -10.3; 365 -10.1; 402 -9.9; 442 -9.8; 486 -9.5; 535 -9.2; 588 -8.8; 647 -8.3; 712 -7.7; 783 -7.0; 861 -6.4; 947 -5.8; 1042 -5.6; 1146 -5.6; 1261 -5.6; 1387 -5.5; 1526 -5.0; 1678 -4.5; 1846 -4.0; 2031 -3.6; 2234 -3.4; 2457 -3.6; 2703 -3.4; 2973 -2.1; 3270 -1.5; 3597 -2.8; 3957 -4.9; 4353 -6.2; 4788 -5.2; 5267 -3.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -17.7; 16529 -20.6; 18182 -18.3; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE6X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE6X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 258 Hz   | 0.54 | -4.5 dB  |
| Peaking | 1950 Hz  | 0.87 | 2.7 dB   |
| Peaking | 3203 Hz  | 4.28 | 3.7 dB   |
| Peaking | 6114 Hz  | 3.27 | 6.5 dB   |
| Peaking | 17661 Hz | 0.95 | -15.0 dB |
| Peaking | 23 Hz    | 1.19 | 1.8 dB   |
| Peaking | 52 Hz    | 2.6  | 0.8 dB   |
| Peaking | 4405 Hz  | 7.18 | -1.8 dB  |
| Peaking | 13242 Hz | 1.85 | 5.8 dB   |
| Peaking | 15269 Hz | 2.88 | -7.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | 0.3 dB   |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -15.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vision%20Ears%20VE6X2/Vision%20Ears%20VE6X2.png)