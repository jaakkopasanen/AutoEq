# Campfire Audio Andromeda sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.7; 25 -6.1; 28 -6.5; 31 -6.8; 34 -7.1; 37 -7.4; 41 -7.7; 45 -8.0; 49 -8.3; 54 -8.6; 60 -8.9; 66 -9.2; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.7; 106 -11.1; 116 -11.5; 128 -11.8; 141 -12.0; 155 -12.2; 170 -12.3; 187 -12.4; 206 -12.5; 227 -12.4; 249 -12.3; 274 -12.2; 302 -11.9; 332 -11.6; 365 -11.2; 402 -10.9; 442 -10.5; 486 -10.0; 535 -9.6; 588 -9.0; 647 -8.4; 712 -7.8; 783 -7.1; 861 -6.5; 947 -6.2; 1042 -6.3; 1146 -6.6; 1261 -6.9; 1387 -6.7; 1526 -6.3; 1678 -5.6; 1846 -4.7; 2031 -3.1; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.1; 5267 -0.9; 5793 -0.6; 6373 -3.9; 7010 -6.5; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.6; 15026 -20.6; 16529 -23.2; 18182 -18.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.39 | 1.8 dB   |
| Peaking | 103 Hz   | 0.56 | -1.6 dB  |
| Peaking | 237 Hz   | 0.46 | -5.2 dB  |
| Peaking | 3741 Hz  | 0.71 | 7.0 dB   |
| Peaking | 16662 Hz | 1.34 | -18.8 dB |
| Peaking | 1549 Hz  | 3.03 | -1.7 dB  |
| Peaking | 2316 Hz  | 5.28 | 2.1 dB   |
| Peaking | 7041 Hz  | 6.49 | -2.6 dB  |
| Peaking | 12523 Hz | 2.61 | 5.0 dB   |
| Peaking | 14722 Hz | 3.31 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB   |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -17.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda%20sample%202/Campfire%20Audio%20Andromeda%20sample%202.png)