# Kennerton Jimo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.6; 28 -11.8; 31 -12.0; 34 -12.1; 37 -12.2; 41 -12.4; 45 -12.6; 49 -12.7; 54 -12.9; 60 -13.2; 66 -13.4; 72 -13.6; 79 -13.9; 87 -14.1; 96 -14.4; 106 -14.6; 116 -14.8; 128 -14.8; 141 -14.9; 155 -14.9; 170 -14.7; 187 -14.5; 206 -14.2; 227 -13.8; 249 -13.4; 274 -12.9; 302 -12.4; 332 -11.8; 365 -11.2; 402 -10.6; 442 -10.0; 486 -9.2; 535 -8.4; 588 -7.6; 647 -6.6; 712 -5.6; 783 -4.5; 861 -3.4; 947 -2.4; 1042 -1.4; 1146 -1.0; 1261 -1.8; 1387 -1.6; 1526 -0.9; 1678 -0.5; 1846 -0.6; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -1.0; 4353 -1.1; 4788 -1.8; 5267 -3.8; 5793 -7.6; 6373 -9.0; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.4; 18182 -9.0; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Jimo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Jimo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.21 | -3.9 dB |
| Peaking | 201 Hz  | 0.35 | -6.7 dB |
| Peaking | 1313 Hz | 0.61 | 6.6 dB  |
| Peaking | 3474 Hz | 1.63 | 4.4 dB  |
| Peaking | 1055 Hz | 2.47 | 2.5 dB  |
| Peaking | 1315 Hz | 1.3  | -2.8 dB |
| Peaking | 1808 Hz | 1.71 | 1.7 dB  |
| Peaking | 4772 Hz | 5.17 | 2.3 dB  |
| Peaking | 6155 Hz | 6.16 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kennerton%20Jimo/Kennerton%20Jimo.png)