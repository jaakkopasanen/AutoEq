# Spiral Ears SE5U sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -6.1; 25 -6.6; 28 -7.3; 31 -7.8; 34 -8.2; 37 -8.5; 41 -8.9; 45 -9.2; 49 -9.6; 54 -9.9; 60 -10.3; 66 -10.7; 72 -11.0; 79 -11.4; 87 -11.9; 96 -12.2; 106 -12.6; 116 -12.9; 128 -13.1; 141 -13.3; 155 -13.3; 170 -13.4; 187 -13.3; 206 -13.3; 227 -13.0; 249 -12.8; 274 -12.5; 302 -12.1; 332 -11.6; 365 -11.1; 402 -10.6; 442 -10.2; 486 -9.7; 535 -9.1; 588 -8.6; 647 -8.2; 712 -7.7; 783 -7.3; 861 -7.1; 947 -7.2; 1042 -7.9; 1146 -9.0; 1261 -10.2; 1387 -11.5; 1526 -12.9; 1678 -14.4; 1846 -13.3; 2031 -11.5; 2234 -9.2; 2457 -6.3; 2703 -5.3; 2973 -5.9; 3270 -0.8; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.9; 13660 -16.2; 15026 -25.5; 16529 -28.0; 18182 -21.7; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spiral Ears SE5U sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spiral Ears SE5U sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 108 Hz   | 0.52 | -4.1 dB  |
| Peaking | 272 Hz   | 0.51 | -4.7 dB  |
| Peaking | 1748 Hz  | 1.19 | -15.7 dB |
| Peaking | 5714 Hz  | 0.17 | 12.0 dB  |
| Peaking | 16183 Hz | 0.74 | -30.2 dB |
| Peaking | 20 Hz    | 2.64 | 1.8 dB   |
| Peaking | 6618 Hz  | 1.83 | 3.0 dB   |
| Peaking | 7561 Hz  | 2.23 | -5.3 dB  |
| Peaking | 11935 Hz | 2.5  | 4.3 dB   |
| Peaking | 14540 Hz | 4.29 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 16000 Hz | 1.41 | -24.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Spiral%20Ears%20SE5U%20sample%202/Spiral%20Ears%20SE5U%20sample%202.png)