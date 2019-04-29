# Clear Tune CT-500E sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.7; 28 -4.9; 31 -5.0; 34 -5.2; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.1; 128 -9.5; 141 -9.8; 155 -10.0; 170 -10.2; 187 -10.4; 206 -10.5; 227 -10.4; 249 -10.4; 274 -10.3; 302 -10.1; 332 -9.7; 365 -9.4; 402 -9.1; 442 -8.8; 486 -8.3; 535 -7.7; 588 -7.0; 647 -6.3; 712 -5.4; 783 -4.5; 861 -3.6; 947 -3.1; 1042 -3.3; 1146 -4.4; 1261 -6.3; 1387 -8.3; 1526 -9.2; 1678 -9.4; 1846 -9.3; 2031 -8.6; 2234 -7.2; 2457 -5.7; 2703 -4.7; 2973 -4.2; 3270 -3.7; 3597 -4.4; 3957 -5.3; 4353 -6.6; 4788 -7.1; 5267 -3.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -7.4; 15026 -11.9; 16529 -8.1; 18182 -6.4; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-500E sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-500E sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 362 Hz   | 0.4  | -6.0 dB  |
| Peaking | 1153 Hz  | 0.56 | 9.7 dB   |
| Peaking | 1607 Hz  | 1.47 | -10.4 dB |
| Peaking | 6093 Hz  | 5.04 | 6.2 dB   |
| Peaking | 15087 Hz | 3.45 | -6.1 dB  |
| Peaking | 24 Hz    | 1.22 | 2.1 dB   |
| Peaking | 49 Hz    | 2.11 | 0.9 dB   |
| Peaking | 2124 Hz  | 4.34 | -1.6 dB  |
| Peaking | 3077 Hz  | 1.38 | 1.5 dB   |
| Peaking | 4519 Hz  | 5.78 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Clear%20Tune%20CT-500E%20sample%202/Clear%20Tune%20CT-500E%20sample%202.png)