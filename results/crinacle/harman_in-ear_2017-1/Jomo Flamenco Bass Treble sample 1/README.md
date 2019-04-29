# Jomo Flamenco Bass Treble sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.2; 25 -2.5; 28 -3.0; 31 -3.3; 34 -3.6; 37 -3.9; 41 -4.2; 45 -4.4; 49 -4.7; 54 -4.9; 60 -5.3; 66 -5.7; 72 -6.1; 79 -6.5; 87 -6.9; 96 -7.3; 106 -7.7; 116 -8.1; 128 -8.4; 141 -8.7; 155 -8.9; 170 -9.0; 187 -9.1; 206 -9.1; 227 -8.9; 249 -8.8; 274 -8.6; 302 -8.3; 332 -7.9; 365 -7.4; 402 -7.0; 442 -6.6; 486 -6.0; 535 -5.3; 588 -4.6; 647 -3.8; 712 -2.9; 783 -2.0; 861 -1.1; 947 -0.6; 1042 -0.5; 1146 -0.8; 1261 -1.3; 1387 -1.5; 1526 -1.6; 1678 -1.8; 1846 -2.4; 2031 -3.1; 2234 -3.3; 2457 -2.6; 2703 -1.3; 2973 -0.7; 3270 -1.5; 3597 -2.3; 3957 -1.6; 4353 -2.2; 4788 -4.8; 5267 -7.3; 5793 -7.3; 6373 -7.2; 7010 -7.8; 7711 -5.9; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -8.3; 15026 -20.8; 16529 -25.4; 18182 -20.6; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass Treble sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass Treble sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.33 | 3.6 dB   |
| Peaking | 206 Hz   | 0.45 | -4.7 dB  |
| Peaking | 1011 Hz  | 0.97 | 5.1 dB   |
| Peaking | 3152 Hz  | 2.22 | 3.7 dB   |
| Peaking | 17009 Hz | 1.45 | -22.8 dB |
| Peaking | 875 Hz   | 3.93 | 0.1 dB   |
| Peaking | 4267 Hz  | 5.09 | 3.3 dB   |
| Peaking | 5704 Hz  | 1.76 | -3.5 dB  |
| Peaking | 13083 Hz | 1.31 | 8.6 dB   |
| Peaking | 15152 Hz | 2.37 | -11.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -20.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20Bass%20Treble%20sample%201/Jomo%20Flamenco%20Bass%20Treble%20sample%201.png)