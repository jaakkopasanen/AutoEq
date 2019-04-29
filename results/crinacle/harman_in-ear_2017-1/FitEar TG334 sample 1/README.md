# FitEar TG334 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.0; 25 -7.0; 28 -7.1; 31 -7.2; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.5; 72 -8.9; 79 -9.2; 87 -9.6; 96 -10.1; 106 -10.6; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.6; 170 -11.7; 187 -11.9; 206 -11.9; 227 -11.7; 249 -11.7; 274 -11.5; 302 -11.2; 332 -10.8; 365 -10.5; 402 -10.1; 442 -9.8; 486 -9.4; 535 -8.9; 588 -8.4; 647 -8.0; 712 -7.4; 783 -6.9; 861 -6.5; 947 -6.3; 1042 -6.5; 1146 -7.0; 1261 -7.3; 1387 -7.3; 1526 -6.9; 1678 -6.2; 1846 -4.9; 2031 -3.3; 2234 -2.2; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -3.9; 6373 -5.4; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.2; 15026 -18.4; 16529 -11.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 134 Hz   | 0.63 | -3.4 dB  |
| Peaking | 289 Hz   | 0.7  | -3.4 dB  |
| Peaking | 1497 Hz  | 2.42 | -2.9 dB  |
| Peaking | 3283 Hz  | 0.78 | 6.9 dB   |
| Peaking | 15125 Hz | 3    | -13.5 dB |
| Peaking | 3375 Hz  | 6.5  | -0.6 dB  |
| Peaking | 4923 Hz  | 4.9  | 2.3 dB   |
| Peaking | 7080 Hz  | 1.08 | -1.0 dB  |
| Peaking | 12643 Hz | 6.03 | 2.6 dB   |
| Peaking | 17742 Hz | 5.4  | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -8.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20TG334%20sample%201/FitEar%20TG334%20sample%201.png)