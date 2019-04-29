# Jomo Flamenco sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.8; 25 -3.2; 28 -3.6; 31 -4.0; 34 -4.3; 37 -4.6; 41 -5.0; 45 -5.2; 49 -5.5; 54 -5.8; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.4; 87 -7.8; 96 -8.3; 106 -8.7; 116 -9.1; 128 -9.5; 141 -9.8; 155 -10.1; 170 -10.2; 187 -10.3; 206 -10.4; 227 -10.4; 249 -10.3; 274 -10.2; 302 -10.0; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.5; 588 -6.9; 647 -6.2; 712 -5.4; 783 -4.5; 861 -3.8; 947 -3.4; 1042 -3.5; 1146 -4.0; 1261 -4.5; 1387 -4.8; 1526 -4.8; 1678 -4.8; 1846 -5.1; 2031 -5.7; 2234 -6.1; 2457 -5.6; 2703 -4.3; 2973 -3.8; 3270 -4.5; 3597 -5.2; 3957 -3.1; 4353 -0.5; 4788 -1.6; 5267 -6.3; 5793 -5.8; 6373 -5.9; 7010 -6.3; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -13.2; 15026 -26.1; 16529 -30.7; 18182 -25.8; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 214 Hz   | 0.48 | -4.3 dB  |
| Peaking | 931 Hz   | 1.43 | 3.4 dB   |
| Peaking | 11026 Hz | 0.3  | 20.1 dB  |
| Peaking | 16387 Hz | 0.5  | -40.3 dB |
| Peaking | 11 Hz    | 0.29 | 4.6 dB   |
| Peaking | 4445 Hz  | 4.94 | 6.0 dB   |
| Peaking | 6994 Hz  | 0.81 | -2.4 dB  |
| Peaking | 12817 Hz | 3.3  | 5.9 dB   |
| Peaking | 14869 Hz | 4.25 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB   |
| Peaking | 62 Hz    | 1.41 | 0.1 dB   |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 16000 Hz | 1.41 | -26.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20sample%201/Jomo%20Flamenco%20sample%201.png)