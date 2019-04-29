# Jomo Flamenco Bass Treble sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.7; 28 -5.3; 31 -5.7; 34 -6.1; 37 -6.4; 41 -6.7; 45 -7.1; 49 -7.4; 54 -7.7; 60 -8.1; 66 -8.4; 72 -8.8; 79 -9.2; 87 -9.6; 96 -10.1; 106 -10.5; 116 -10.8; 128 -11.0; 141 -11.3; 155 -11.4; 170 -11.5; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.2; 274 -11.0; 302 -10.7; 332 -10.2; 365 -9.7; 402 -9.3; 442 -8.8; 486 -8.2; 535 -7.5; 588 -6.8; 647 -6.0; 712 -5.2; 783 -4.3; 861 -3.4; 947 -2.9; 1042 -2.8; 1146 -3.1; 1261 -3.5; 1387 -3.7; 1526 -3.7; 1678 -3.8; 1846 -4.2; 2031 -4.6; 2234 -4.2; 2457 -2.8; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -2.9; 4353 -4.4; 4788 -6.0; 5267 -8.3; 5793 -8.1; 6373 -6.3; 7010 -6.1; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -18.8; 16529 -21.5; 18182 -17.7; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass Treble sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass Treble sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.81 | 4.2 dB   |
| Peaking | 197 Hz   | 0.42 | -5.3 dB  |
| Peaking | 993 Hz   | 0.99 | 4.5 dB   |
| Peaking | 3136 Hz  | 2.21 | 6.4 dB   |
| Peaking | 16916 Hz | 1.4  | -16.6 dB |
| Peaking | 2135 Hz  | 7.37 | -0.7 dB  |
| Peaking | 5470 Hz  | 4.37 | -3.9 dB  |
| Peaking | 8173 Hz  | 0.63 | 2.3 dB   |
| Peaking | 12671 Hz | 3.18 | 5.0 dB   |
| Peaking | 17341 Hz | 0.21 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -15.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20Bass%20Treble%20sample%202/Jomo%20Flamenco%20Bass%20Treble%20sample%202.png)