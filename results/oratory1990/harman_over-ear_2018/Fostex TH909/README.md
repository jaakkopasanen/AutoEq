# Fostex TH909
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.6; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.0; 37 -9.0; 41 -9.0; 45 -8.9; 49 -8.9; 54 -8.8; 60 -8.7; 66 -8.6; 72 -8.6; 79 -8.6; 87 -8.7; 96 -8.8; 106 -8.8; 116 -8.9; 128 -9.0; 141 -9.1; 155 -9.1; 170 -8.9; 187 -8.8; 206 -8.8; 227 -8.8; 249 -8.9; 274 -8.8; 302 -8.8; 332 -8.8; 365 -8.7; 402 -8.5; 442 -8.2; 486 -7.9; 535 -7.5; 588 -7.0; 647 -6.2; 712 -5.3; 783 -4.8; 861 -4.1; 947 -3.6; 1042 -3.2; 1146 -2.8; 1261 -2.4; 1387 -2.3; 1526 -2.4; 1678 -2.5; 1846 -2.2; 2031 -1.6; 2234 -0.9; 2457 -0.5; 2703 -0.6; 2973 -2.3; 3270 -5.9; 3597 -6.3; 3957 -4.6; 4353 -4.3; 4788 -5.3; 5267 -7.6; 5793 -9.9; 6373 -8.0; 7010 -4.7; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.9; 15026 -9.0; 16529 -12.3; 18182 -13.0; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH909 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH909 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 130 Hz   | 0.09 | -3.4 dB |
| Peaking | 1211 Hz  | 0.87 | 5.1 dB  |
| Peaking | 2453 Hz  | 2.71 | 4.8 dB  |
| Peaking | 5813 Hz  | 7.08 | -4.9 dB |
| Peaking | 18286 Hz | 0.98 | -8.3 dB |
| Peaking | 77 Hz    | 2.37 | 0.5 dB  |
| Peaking | 2892 Hz  | 7.27 | 2.1 dB  |
| Peaking | 3394 Hz  | 4.29 | -2.9 dB |
| Peaking | 4195 Hz  | 5.2  | 1.8 dB  |
| Peaking | 12336 Hz | 2.07 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Fostex%20TH909/Fostex%20TH909.png)