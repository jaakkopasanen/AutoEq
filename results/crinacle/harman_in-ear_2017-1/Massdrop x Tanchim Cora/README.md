# Massdrop x Tanchim Cora
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.7; 25 -9.8; 28 -10.0; 31 -10.0; 34 -10.0; 37 -10.0; 41 -10.0; 45 -10.0; 49 -9.9; 54 -9.9; 60 -9.9; 66 -9.8; 72 -9.8; 79 -9.8; 87 -9.8; 96 -9.8; 106 -9.7; 116 -9.5; 128 -9.4; 141 -9.2; 155 -8.8; 170 -8.4; 187 -8.0; 206 -7.5; 227 -7.2; 249 -7.0; 274 -6.8; 302 -6.5; 332 -6.2; 365 -5.8; 402 -5.7; 442 -5.5; 486 -5.3; 535 -5.3; 588 -5.4; 647 -5.6; 712 -5.9; 783 -6.3; 861 -6.8; 947 -7.7; 1042 -8.6; 1146 -9.4; 1261 -10.5; 1387 -11.1; 1526 -9.9; 1678 -8.4; 1846 -6.9; 2031 -5.7; 2234 -4.8; 2457 -4.7; 2703 -5.0; 2973 -4.2; 3270 -2.4; 3597 -1.0; 3957 -0.5; 4353 -1.8; 4788 -4.5; 5267 -4.1; 5793 -1.2; 6373 -0.8; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -7.4; 13660 -14.6; 15026 -24.8; 16529 -27.0; 18182 -14.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Tanchim Cora GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Tanchim Cora ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.33 | -4.4 dB  |
| Peaking | 1376 Hz  | 2.15 | -6.2 dB  |
| Peaking | 5072 Hz  | 0.58 | 5.1 dB   |
| Peaking | 11927 Hz | 2.66 | 6.6 dB   |
| Peaking | 15895 Hz | 1.37 | -24.9 dB |
| Peaking | 496 Hz   | 1.73 | 1.2 dB   |
| Peaking | 4000 Hz  | 3.06 | 5.7 dB   |
| Peaking | 4880 Hz  | 1.49 | -5.9 dB  |
| Peaking | 6089 Hz  | 3.8  | 5.6 dB   |
| Peaking | 17210 Hz | 6.89 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Massdrop%20x%20Tanchim%20Cora/Massdrop%20x%20Tanchim%20Cora.png)