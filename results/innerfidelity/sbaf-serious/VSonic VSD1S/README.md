# VSonic VSD1S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.6; 25 -4.9; 28 -5.3; 31 -5.6; 34 -5.9; 37 -6.2; 41 -6.5; 45 -6.7; 49 -7.0; 54 -7.2; 60 -7.6; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.1; 96 -9.3; 106 -9.6; 116 -9.7; 128 -9.9; 141 -10.1; 155 -10.1; 170 -10.1; 187 -10.0; 206 -9.8; 227 -9.5; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.8; 402 -7.4; 442 -7.0; 486 -6.7; 535 -6.4; 588 -5.9; 647 -5.7; 712 -5.7; 783 -5.6; 861 -6.0; 947 -6.4; 1042 -6.3; 1146 -6.8; 1261 -7.2; 1387 -7.8; 1526 -8.2; 1678 -8.3; 1846 -7.9; 2031 -7.1; 2234 -6.2; 2457 -4.4; 2703 -2.6; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -5.6; 5267 -4.8; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD1S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.22 | 2.5 dB  |
| Peaking | 146 Hz  | 0.72 | -3.9 dB |
| Peaking | 1753 Hz | 2.43 | -2.8 dB |
| Peaking | 3326 Hz | 1.92 | 6.9 dB  |
| Peaking | 6220 Hz | 5.75 | 5.6 dB  |
| Peaking | 275 Hz  | 2.58 | -0.6 dB |
| Peaking | 672 Hz  | 2.03 | 1.3 dB  |
| Peaking | 4058 Hz | 9.73 | 1.8 dB  |
| Peaking | 4843 Hz | 8.18 | -2.0 dB |
| Peaking | 8351 Hz | 4.83 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1S/VSonic%20VSD1S.png)