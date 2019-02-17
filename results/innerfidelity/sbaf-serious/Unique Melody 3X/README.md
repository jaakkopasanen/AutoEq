# Unique Melody 3X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.7; 25 -12.6; 28 -12.6; 31 -12.4; 34 -12.3; 37 -12.2; 41 -12.0; 45 -11.8; 49 -11.7; 54 -11.6; 60 -11.4; 66 -11.3; 72 -11.2; 79 -11.1; 87 -11.1; 96 -11.0; 106 -10.8; 116 -10.5; 128 -10.4; 141 -10.2; 155 -9.9; 170 -9.6; 187 -9.3; 206 -9.0; 227 -8.5; 249 -8.2; 274 -7.8; 302 -7.5; 332 -7.1; 365 -6.7; 402 -6.3; 442 -5.8; 486 -5.6; 535 -5.2; 588 -4.6; 647 -4.3; 712 -4.1; 783 -3.8; 861 -3.8; 947 -3.9; 1042 -4.2; 1146 -4.3; 1261 -4.4; 1387 -4.8; 1526 -5.0; 1678 -5.2; 1846 -5.0; 2031 -4.6; 2234 -4.4; 2457 -3.8; 2703 -3.2; 2973 -1.7; 3270 -0.5; 3597 -2.0; 3957 -5.9; 4353 -10.3; 4788 -12.8; 5267 -13.6; 5793 -12.5; 6373 -9.8; 7010 -7.3; 7711 -4.5; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.18 | -8.3 dB  |
| Peaking | 176 Hz  | 0.67 | -3.0 dB  |
| Peaking | 1696 Hz | 4.42 | -1.0 dB  |
| Peaking | 3332 Hz | 3.32 | 6.2 dB   |
| Peaking | 5136 Hz | 2.24 | -10.9 dB |
| Peaking | 365 Hz  | 2.42 | -0.4 dB  |
| Peaking | 781 Hz  | 2.28 | 1.0 dB   |
| Peaking | 6434 Hz | 3.42 | -2.1 dB  |
| Peaking | 7886 Hz | 2.01 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Unique%20Melody%203X/Unique%20Melody%203X.png)