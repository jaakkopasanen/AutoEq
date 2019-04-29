# Warbler Prelude sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.6; 31 -2.4; 34 -3.0; 37 -3.5; 41 -4.2; 45 -4.9; 49 -5.5; 54 -6.1; 60 -6.6; 66 -7.2; 72 -7.9; 79 -8.5; 87 -9.0; 96 -9.5; 106 -10.1; 116 -10.6; 128 -11.1; 141 -11.4; 155 -11.6; 170 -11.9; 187 -12.2; 206 -12.3; 227 -12.4; 249 -12.3; 274 -12.3; 302 -12.3; 332 -12.0; 365 -11.7; 402 -11.5; 442 -11.2; 486 -11.0; 535 -10.6; 588 -10.2; 647 -9.7; 712 -9.1; 783 -8.6; 861 -8.1; 947 -7.8; 1042 -7.8; 1146 -8.1; 1261 -8.3; 1387 -8.0; 1526 -7.2; 1678 -6.3; 1846 -5.4; 2031 -4.4; 2234 -3.4; 2457 -3.0; 2703 -3.2; 2973 -4.0; 3270 -4.2; 3597 -2.7; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Warbler Prelude sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Warbler Prelude sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.62 | 6.5 dB  |
| Peaking | 222 Hz  | 0.47 | -4.9 dB |
| Peaking | 944 Hz  | 0.05 | -1.3 dB |
| Peaking | 2313 Hz | 2.25 | 3.6 dB  |
| Peaking | 4938 Hz | 1.3  | 7.9 dB  |
| Peaking | 910 Hz  | 2.01 | 2.7 dB  |
| Peaking | 969 Hz  | 1.08 | -1.9 dB |
| Peaking | 6410 Hz | 3.91 | 4.7 dB  |
| Peaking | 6824 Hz | 1.41 | -4.1 dB |
| Peaking | 6947 Hz | 0.38 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Warbler%20Prelude%20sample%202/Warbler%20Prelude%20sample%202.png)