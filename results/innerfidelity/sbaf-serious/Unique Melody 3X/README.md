# Unique Melody 3X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -12.7; 25 -12.6; 28 -12.6; 31 -12.4; 34 -12.3; 37 -12.2; 41 -12.0; 45 -11.8; 49 -11.7; 54 -11.6; 60 -11.4; 66 -11.3; 72 -11.2; 79 -11.1; 87 -11.1; 96 -11.0; 106 -10.8; 116 -10.5; 128 -10.4; 141 -10.2; 155 -9.9; 170 -9.6; 187 -9.3; 206 -9.0; 227 -8.5; 249 -8.2; 274 -7.8; 302 -7.5; 332 -7.1; 365 -6.7; 402 -6.3; 442 -5.8; 486 -5.6; 535 -5.2; 588 -4.6; 647 -4.3; 712 -4.1; 783 -3.8; 861 -3.8; 947 -3.9; 1042 -4.2; 1146 -4.3; 1261 -4.4; 1387 -4.8; 1526 -5.0; 1678 -5.2; 1846 -5.0; 2031 -4.6; 2234 -4.4; 2457 -3.8; 2703 -3.2; 2973 -1.7; 3270 -0.5; 3597 -2.0; 3957 -5.9; 4353 -10.3; 4788 -12.8; 5267 -13.6; 5793 -12.5; 6373 -9.8; 7010 -7.3; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.5  | -5.6 dB |
| Peaking | 103 Hz  | 0.41 | -3.8 dB |
| Peaking | 797 Hz  | 0.75 | 2.7 dB  |
| Peaking | 3307 Hz | 2.41 | 7.3 dB  |
| Peaking | 5047 Hz | 2.41 | -9.4 dB |
| Peaking | 1656 Hz | 4.38 | -0.4 dB |
| Peaking | 2118 Hz | 3.85 | 0.4 dB  |
| Peaking | 6064 Hz | 5.75 | -1.7 dB |
| Peaking | 7543 Hz | 2.92 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Unique%20Melody%203X/Unique%20Melody%203X.png)