# Focal Sphear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.2; 25 -3.7; 28 -4.2; 31 -4.7; 34 -5.1; 37 -5.4; 41 -5.8; 45 -6.2; 49 -6.5; 54 -6.8; 60 -7.2; 66 -7.6; 72 -8.0; 79 -8.4; 87 -8.8; 96 -9.2; 106 -9.5; 116 -9.8; 128 -10.0; 141 -10.2; 155 -10.3; 170 -10.3; 187 -10.3; 206 -10.1; 227 -9.8; 249 -9.6; 274 -9.3; 302 -8.8; 332 -8.3; 365 -7.8; 402 -7.3; 442 -6.8; 486 -6.4; 535 -5.8; 588 -5.3; 647 -4.8; 712 -4.2; 783 -3.6; 861 -3.2; 947 -3.1; 1042 -3.2; 1146 -3.8; 1261 -4.3; 1387 -4.5; 1526 -4.4; 1678 -4.1; 1846 -3.8; 2031 -3.3; 2234 -2.9; 2457 -2.7; 2703 -2.4; 2973 -1.8; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -3.2; 5267 -6.7; 5793 -8.6; 6373 -4.4; 7010 -3.2; 7711 -5.3; 8482 -7.4; 9330 -5.8; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -12.9; 15026 -18.2; 16529 -15.2; 18182 -12.1; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Sphear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Sphear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.81 | 3.7 dB   |
| Peaking | 166 Hz   | 0.48 | -4.9 dB  |
| Peaking | 865 Hz   | 1.02 | 2.9 dB   |
| Peaking | 3467 Hz  | 1.6  | 5.3 dB   |
| Peaking | 15896 Hz | 1.44 | -12.8 dB |
| Peaking | 4494 Hz  | 4.18 | 2.0 dB   |
| Peaking | 5654 Hz  | 4.17 | -5.1 dB  |
| Peaking | 6719 Hz  | 6.34 | 4.2 dB   |
| Peaking | 11890 Hz | 3.88 | 3.9 dB   |
| Peaking | 19720 Hz | 1.1  | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB   |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -13.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Focal%20Sphear/Focal%20Sphear.png)