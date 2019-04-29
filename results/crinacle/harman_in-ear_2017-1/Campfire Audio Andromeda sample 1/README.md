# Campfire Audio Andromeda sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.8; 28 -8.0; 31 -8.1; 34 -8.2; 37 -8.3; 41 -8.4; 45 -8.5; 49 -8.6; 54 -8.8; 60 -9.0; 66 -9.3; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.8; 106 -11.1; 116 -11.4; 128 -11.7; 141 -12.0; 155 -12.2; 170 -12.3; 187 -12.4; 206 -12.3; 227 -12.3; 249 -12.1; 274 -12.0; 302 -11.7; 332 -11.3; 365 -10.9; 402 -10.6; 442 -10.2; 486 -9.7; 535 -9.2; 588 -8.6; 647 -8.0; 712 -7.3; 783 -6.6; 861 -6.0; 947 -5.7; 1042 -5.7; 1146 -6.0; 1261 -6.3; 1387 -6.2; 1526 -5.8; 1678 -5.3; 1846 -4.6; 2031 -3.4; 2234 -1.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -2.1; 7010 -5.5; 7711 -6.2; 8482 -8.3; 9330 -9.9; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -16.1; 15026 -27.1; 16529 -30.2; 18182 -27.2; 20000 -19.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Andromeda sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Andromeda sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.13 | -0.8 dB  |
| Peaking | 214 Hz   | 0.42 | -5.6 dB  |
| Peaking | 10103 Hz | 0.19 | 10.5 dB  |
| Peaking | 16108 Hz | 0.78 | -29.3 dB |
| Peaking | 18720 Hz | 0.91 | -11.7 dB |
| Peaking | 1626 Hz  | 1.4  | -5.4 dB  |
| Peaking | 2194 Hz  | 0.59 | 4.4 dB   |
| Peaking | 5787 Hz  | 2.28 | 4.5 dB   |
| Peaking | 9143 Hz  | 0.52 | -6.8 dB  |
| Peaking | 12045 Hz | 2.18 | 11.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -27.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Andromeda%20sample%201/Campfire%20Audio%20Andromeda%20sample%201.png)