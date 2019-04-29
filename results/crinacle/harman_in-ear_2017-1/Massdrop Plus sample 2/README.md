# Massdrop Plus sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.5; 28 -6.8; 31 -7.1; 34 -7.2; 37 -7.4; 41 -7.6; 45 -7.8; 49 -8.1; 54 -8.3; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.4; 87 -9.8; 96 -10.1; 106 -10.4; 116 -10.8; 128 -11.0; 141 -11.2; 155 -11.2; 170 -11.3; 187 -11.3; 206 -11.3; 227 -11.1; 249 -10.8; 274 -10.6; 302 -10.3; 332 -9.8; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.6; 588 -7.1; 647 -6.6; 712 -6.0; 783 -5.5; 861 -5.2; 947 -5.1; 1042 -5.5; 1146 -6.2; 1261 -7.0; 1387 -7.6; 1526 -7.7; 1678 -7.7; 1846 -7.7; 2031 -7.3; 2234 -6.5; 2457 -5.4; 2703 -4.2; 2973 -3.1; 3270 -2.3; 3597 -1.9; 3957 -1.7; 4353 -1.5; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -12.4; 16529 -12.4; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 92 Hz    | 0.72 | -0.6 dB |
| Peaking | 185 Hz   | 0.51 | -4.6 dB |
| Peaking | 818 Hz   | 2.73 | 2.2 dB  |
| Peaking | 4847 Hz  | 1.32 | 6.5 dB  |
| Peaking | 15963 Hz | 2.28 | -7.6 dB |
| Peaking | 19 Hz    | 2.01 | 1.1 dB  |
| Peaking | 1792 Hz  | 2.25 | -2.0 dB |
| Peaking | 3120 Hz  | 3.17 | 2.1 dB  |
| Peaking | 6345 Hz  | 3.6  | 5.5 dB  |
| Peaking | 6690 Hz  | 1.62 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -5.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Massdrop%20Plus%20sample%202/Massdrop%20Plus%20sample%202.png)