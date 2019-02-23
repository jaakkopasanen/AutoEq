# LucidSound LS31
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.6; 28 -2.8; 31 -4.0; 34 -4.8; 37 -5.5; 41 -6.3; 45 -7.1; 49 -8.0; 54 -8.8; 60 -9.6; 66 -10.2; 72 -10.6; 79 -10.9; 87 -11.2; 96 -11.4; 106 -11.6; 116 -11.8; 128 -11.9; 141 -12.0; 155 -12.0; 170 -11.9; 187 -11.7; 206 -11.5; 227 -11.3; 249 -11.3; 274 -11.1; 302 -10.9; 332 -10.6; 365 -10.1; 402 -9.5; 442 -8.4; 486 -7.2; 535 -6.4; 588 -6.0; 647 -5.6; 712 -5.0; 783 -4.9; 861 -5.7; 947 -6.2; 1042 -6.1; 1146 -5.6; 1261 -5.2; 1387 -5.1; 1526 -5.1; 1678 -4.7; 1846 -4.1; 2031 -3.3; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.5; 3957 -2.6; 4353 -1.8; 4788 -3.0; 5267 -3.9; 5793 -6.1; 6373 -2.6; 7010 -4.0; 7711 -6.6; 8482 -11.0; 9330 -10.3; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`LucidSound LS31 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LucidSound LS31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.21 | 6.5 dB  |
| Peaking | 114 Hz  | 0.58 | -5.6 dB |
| Peaking | 289 Hz  | 1.74 | -2.8 dB |
| Peaking | 3053 Hz | 0.86 | 6.0 dB  |
| Peaking | 8871 Hz | 5.59 | -6.6 dB |
| Peaking | 397 Hz  | 5.45 | -1.0 dB |
| Peaking | 672 Hz  | 1.67 | 2.2 dB  |
| Peaking | 1934 Hz | 0.3  | -0.9 dB |
| Peaking | 2513 Hz | 2.91 | 1.7 dB  |
| Peaking | 6648 Hz | 9.8  | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/LucidSound%20LS31/LucidSound%20LS31.png)