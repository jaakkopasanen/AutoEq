# Campfire Audio Dorado
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.9; 25 -12.0; 28 -12.1; 31 -12.1; 34 -12.2; 37 -12.2; 41 -12.3; 45 -12.4; 49 -12.5; 54 -12.6; 60 -12.8; 66 -13.0; 72 -13.2; 79 -13.5; 87 -13.7; 96 -14.0; 106 -14.2; 116 -14.4; 128 -14.5; 141 -14.6; 155 -14.6; 170 -14.5; 187 -14.3; 206 -14.1; 227 -13.7; 249 -13.4; 274 -12.9; 302 -12.4; 332 -11.8; 365 -11.2; 402 -10.7; 442 -10.3; 486 -9.7; 535 -9.2; 588 -8.6; 647 -8.0; 712 -7.5; 783 -7.0; 861 -6.6; 947 -6.6; 1042 -6.8; 1146 -7.3; 1261 -7.8; 1387 -7.3; 1526 -6.6; 1678 -5.9; 1846 -4.5; 2031 -2.5; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -16.7; 16529 -20.7; 18182 -16.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Dorado GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Dorado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 1.54 | -4.7 dB  |
| Peaking | 25 Hz    | 0.43 | -3.9 dB  |
| Peaking | 161 Hz   | 0.41 | -7.6 dB  |
| Peaking | 3817 Hz  | 0.74 | 7.1 dB   |
| Peaking | 16753 Hz | 1.55 | -16.0 dB |
| Peaking | 1447 Hz  | 2.72 | -2.2 dB  |
| Peaking | 2260 Hz  | 4.95 | 2.7 dB   |
| Peaking | 6344 Hz  | 4.05 | 3.3 dB   |
| Peaking | 7558 Hz  | 3.79 | -3.9 dB  |
| Peaking | 12828 Hz | 4.66 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -13.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Dorado/Campfire%20Audio%20Dorado.png)