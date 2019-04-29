# Kinera SEED
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.5; 49 -2.3; 54 -3.2; 60 -4.2; 66 -5.1; 72 -5.9; 79 -6.8; 87 -7.6; 96 -8.4; 106 -9.2; 116 -9.8; 128 -10.4; 141 -10.8; 155 -11.1; 170 -11.3; 187 -11.4; 206 -11.4; 227 -11.3; 249 -11.1; 274 -10.8; 302 -10.4; 332 -9.9; 365 -9.4; 402 -8.9; 442 -8.4; 486 -7.8; 535 -7.2; 588 -6.7; 647 -6.1; 712 -5.6; 783 -5.2; 861 -5.0; 947 -5.1; 1042 -5.7; 1146 -6.4; 1261 -7.1; 1387 -7.7; 1526 -7.8; 1678 -7.7; 1846 -7.0; 2031 -5.4; 2234 -3.1; 2457 -1.0; 2703 -0.5; 2973 -2.0; 3270 -6.4; 3597 -6.7; 3957 -6.7; 4353 -7.6; 4788 -7.1; 5267 -5.8; 5793 -3.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.5; 15026 -18.9; 16529 -17.4; 18182 -8.9; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera SEED GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera SEED ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.65 | 6.9 dB   |
| Peaking | 173 Hz   | 0.69 | -5.8 dB  |
| Peaking | 2608 Hz  | 4.57 | 6.7 dB   |
| Peaking | 12966 Hz | 0.46 | 3.6 dB   |
| Peaking | 15722 Hz | 1.78 | -17.7 dB |
| Peaking | 839 Hz   | 2.19 | 2.2 dB   |
| Peaking | 1513 Hz  | 3.25 | -2.0 dB  |
| Peaking | 4508 Hz  | 2.81 | -2.4 dB  |
| Peaking | 6283 Hz  | 4.29 | 5.7 dB   |
| Peaking | 8193 Hz  | 2.4  | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.6 dB   |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -11.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kinera%20SEED/Kinera%20SEED.png)