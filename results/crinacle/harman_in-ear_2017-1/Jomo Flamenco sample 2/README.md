# Jomo Flamenco sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.5; 25 -5.0; 28 -5.6; 31 -6.1; 34 -6.4; 37 -6.7; 41 -7.1; 45 -7.5; 49 -7.8; 54 -8.1; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.6; 87 -10.1; 96 -10.5; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.0; 170 -12.1; 187 -12.3; 206 -12.3; 227 -12.3; 249 -12.1; 274 -11.9; 302 -11.7; 332 -11.2; 365 -10.8; 402 -10.4; 442 -9.9; 486 -9.4; 535 -8.8; 588 -8.1; 647 -7.3; 712 -6.5; 783 -5.6; 861 -4.8; 947 -4.2; 1042 -4.1; 1146 -4.4; 1261 -4.7; 1387 -4.8; 1526 -4.5; 1678 -4.4; 1846 -4.5; 2031 -4.6; 2234 -4.3; 2457 -3.1; 2703 -1.5; 2973 -0.8; 3270 -1.2; 3597 -2.2; 3957 -1.0; 4353 -0.5; 4788 -0.6; 5267 -4.3; 5793 -3.8; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.3; 15026 -21.5; 16529 -23.7; 18182 -20.3; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 224 Hz   | 0.44 | -6.7 dB  |
| Peaking | 2936 Hz  | 0.14 | 3.0 dB   |
| Peaking | 4663 Hz  | 0.78 | 6.4 dB   |
| Peaking | 12758 Hz | 0.97 | 16.8 dB  |
| Peaking | 15515 Hz | 0.51 | -27.8 dB |
| Peaking | 21 Hz    | 1.69 | 2.9 dB   |
| Peaking | 943 Hz   | 3.62 | 1.6 dB   |
| Peaking | 2315 Hz  | 1.47 | -2.7 dB  |
| Peaking | 2880 Hz  | 2.08 | 3.4 dB   |
| Peaking | 3573 Hz  | 6.59 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -19.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20sample%202/Jomo%20Flamenco%20sample%202.png)