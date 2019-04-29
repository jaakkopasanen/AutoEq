# Campfire Audio Solaris sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.0; 25 -7.1; 28 -7.3; 31 -7.4; 34 -7.5; 37 -7.7; 41 -7.8; 45 -7.9; 49 -8.1; 54 -8.2; 60 -8.4; 66 -8.6; 72 -8.9; 79 -9.2; 87 -9.5; 96 -9.9; 106 -10.2; 116 -10.5; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.1; 187 -11.1; 206 -11.2; 227 -11.1; 249 -10.9; 274 -10.8; 302 -10.6; 332 -10.2; 365 -9.9; 402 -9.6; 442 -9.3; 486 -8.9; 535 -8.6; 588 -8.2; 647 -7.8; 712 -7.4; 783 -7.4; 861 -7.5; 947 -7.5; 1042 -7.4; 1146 -7.4; 1261 -7.5; 1387 -7.5; 1526 -7.6; 1678 -8.0; 1846 -9.0; 2031 -9.1; 2234 -7.1; 2457 -3.9; 2703 -1.6; 2973 -1.3; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -8.8; 11289 -7.2; 12418 -8.2; 13660 -16.6; 15026 -24.7; 16529 -26.1; 18182 -23.7; 20000 -20.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 171 Hz   | 0.97 | -1.1 dB  |
| Peaking | 365 Hz   | 0.19 | -4.3 dB  |
| Peaking | 1865 Hz  | 1.59 | -7.8 dB  |
| Peaking | 7251 Hz  | 0.18 | 15.5 dB  |
| Peaking | 16469 Hz | 0.4  | -30.5 dB |
| Peaking | 2751 Hz  | 5.78 | 1.9 dB   |
| Peaking | 6318 Hz  | 1.94 | 3.5 dB   |
| Peaking | 7534 Hz  | 2.45 | -3.6 dB  |
| Peaking | 12071 Hz | 4.29 | 6.6 dB   |
| Peaking | 16652 Hz | 0.09 | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -25.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Solaris%20sample%201/Campfire%20Audio%20Solaris%20sample%201.png)