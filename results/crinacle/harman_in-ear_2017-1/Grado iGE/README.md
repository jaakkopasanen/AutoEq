# Grado iGE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.8; 25 -11.8; 28 -11.9; 31 -11.8; 34 -11.8; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.8; 54 -11.7; 60 -11.6; 66 -11.6; 72 -11.7; 79 -11.7; 87 -11.8; 96 -11.8; 106 -11.9; 116 -11.8; 128 -11.7; 141 -11.7; 155 -11.5; 170 -11.3; 187 -11.1; 206 -10.8; 227 -10.5; 249 -10.2; 274 -10.0; 302 -9.8; 332 -9.4; 365 -9.0; 402 -8.8; 442 -8.6; 486 -8.4; 535 -8.2; 588 -8.1; 647 -8.0; 712 -7.9; 783 -7.9; 861 -7.9; 947 -8.2; 1042 -8.6; 1146 -9.1; 1261 -9.8; 1387 -10.1; 1526 -9.8; 1678 -8.9; 1846 -7.4; 2031 -5.0; 2234 -2.6; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -4.5; 7711 -7.4; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.5; 15026 -16.0; 16529 -17.6; 18182 -19.5; 20000 -19.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.16 | -5.5 dB  |
| Peaking | 1519 Hz  | 1.47 | -5.2 dB  |
| Peaking | 2515 Hz  | 1.96 | 4.9 dB   |
| Peaking | 4684 Hz  | 0.83 | 6.5 dB   |
| Peaking | 18771 Hz | 0.55 | -14.6 dB |
| Peaking | 6162 Hz  | 5.61 | 1.9 dB   |
| Peaking | 7654 Hz  | 4.23 | -3.3 dB  |
| Peaking | 12570 Hz | 2.04 | 5.3 dB   |
| Peaking | 14567 Hz | 1.98 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -14.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Grado%20iGE/Grado%20iGE.png)