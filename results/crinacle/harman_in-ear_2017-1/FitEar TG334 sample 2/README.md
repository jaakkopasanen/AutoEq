# FitEar TG334 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.4; 28 -6.8; 31 -7.1; 34 -7.4; 37 -7.6; 41 -7.9; 45 -8.1; 49 -8.2; 54 -8.5; 60 -8.8; 66 -9.1; 72 -9.5; 79 -9.9; 87 -10.3; 96 -10.8; 106 -11.1; 116 -11.4; 128 -11.7; 141 -12.0; 155 -12.2; 170 -12.3; 187 -12.4; 206 -12.4; 227 -12.3; 249 -12.2; 274 -12.0; 302 -11.7; 332 -11.3; 365 -10.9; 402 -10.6; 442 -10.2; 486 -9.8; 535 -9.3; 588 -8.8; 647 -8.3; 712 -7.7; 783 -7.1; 861 -6.7; 947 -6.4; 1042 -6.6; 1146 -7.0; 1261 -7.3; 1387 -7.3; 1526 -6.8; 1678 -6.0; 1846 -4.8; 2031 -3.2; 2234 -2.0; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -2.2; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.8; 15026 -15.8; 16529 -9.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar TG334 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar TG334 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 1.52 | 1.4 dB   |
| Peaking | 104 Hz   | 0.43 | -0.7 dB  |
| Peaking | 209 Hz   | 0.44 | -5.5 dB  |
| Peaking | 3636 Hz  | 0.86 | 6.9 dB   |
| Peaking | 14848 Hz | 2.88 | -10.5 dB |
| Peaking | 1475 Hz  | 3.43 | -1.9 dB  |
| Peaking | 2382 Hz  | 4.34 | 1.5 dB   |
| Peaking | 5270 Hz  | 5.82 | 1.5 dB   |
| Peaking | 8234 Hz  | 3.96 | -1.6 dB  |
| Peaking | 12658 Hz | 6.19 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20TG334%20sample%202/FitEar%20TG334%20sample%202.png)