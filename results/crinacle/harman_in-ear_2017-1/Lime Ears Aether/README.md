# Lime Ears Aether
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.8; 25 -5.9; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.7; 41 -6.8; 45 -6.9; 49 -7.0; 54 -7.2; 60 -7.3; 66 -7.6; 72 -7.8; 79 -8.1; 87 -8.4; 96 -8.8; 106 -9.1; 116 -9.3; 128 -9.5; 141 -9.7; 155 -9.9; 170 -10.0; 187 -10.0; 206 -10.1; 227 -10.0; 249 -9.9; 274 -9.8; 302 -9.6; 332 -9.3; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.8; 647 -7.7; 712 -7.6; 783 -7.6; 861 -7.6; 947 -7.8; 1042 -8.2; 1146 -8.8; 1261 -9.2; 1387 -9.0; 1526 -8.4; 1678 -7.5; 1846 -6.5; 2031 -5.5; 2234 -4.6; 2457 -4.0; 2703 -3.5; 2973 -2.5; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -3.8; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -9.7; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -13.4; 16529 -15.6; 18182 -16.0; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lime Ears Aether GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lime Ears Aether ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 197 Hz   | 0.55 | -3.7 dB  |
| Peaking | 1325 Hz  | 2.02 | -3.1 dB  |
| Peaking | 3777 Hz  | 1.31 | 6.6 dB   |
| Peaking | 6287 Hz  | 5.86 | 4.6 dB   |
| Peaking | 19232 Hz | 0.54 | -11.7 dB |
| Peaking | 19 Hz    | 1.29 | 1.0 dB   |
| Peaking | 2259 Hz  | 7.66 | 0.5 dB   |
| Peaking | 9272 Hz  | 4.74 | -3.8 dB  |
| Peaking | 13684 Hz | 1.38 | 5.1 dB   |
| Peaking | 15485 Hz | 2.2  | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -9.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lime%20Ears%20Aether/Lime%20Ears%20Aether.png)