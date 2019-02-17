# LucidSound LS31
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.1; 25 -1.8; 28 -3.1; 31 -4.2; 34 -5.1; 37 -5.8; 41 -6.6; 45 -7.4; 49 -8.2; 54 -9.1; 60 -9.9; 66 -10.5; 72 -10.9; 79 -11.2; 87 -11.5; 96 -11.7; 106 -11.8; 116 -12.0; 128 -12.2; 141 -12.3; 155 -12.3; 170 -12.2; 187 -12.0; 206 -11.7; 227 -11.5; 249 -11.6; 274 -11.4; 302 -11.2; 332 -10.9; 365 -10.4; 402 -9.8; 442 -8.7; 486 -7.5; 535 -6.7; 588 -6.2; 647 -5.8; 712 -5.3; 783 -5.2; 861 -6.0; 947 -6.5; 1042 -6.4; 1146 -5.9; 1261 -5.5; 1387 -5.3; 1526 -5.3; 1678 -5.0; 1846 -4.4; 2031 -3.5; 2234 -1.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.7; 3957 -2.9; 4353 -2.0; 4788 -3.3; 5267 -4.2; 5793 -6.3; 6373 -2.9; 7010 -4.0; 7711 -6.8; 8482 -11.2; 9330 -10.5; 10263 -6.6; 11289 -6.5; 12418 -7.5; 13660 -7.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`LucidSound LS31 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LucidSound LS31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  1.21 | 6.5 dB  |
| Peaking | 114 Hz   |  0.56 | -5.8 dB |
| Peaking | 292 Hz   |  1.69 | -2.8 dB |
| Peaking | 3029 Hz  |  0.97 | 6.1 dB  |
| Peaking | 8823 Hz  |  5.73 | -6.7 dB |
| Peaking | 392 Hz   |  5.57 | -1.0 dB |
| Peaking | 666 Hz   |  2.54 | 1.6 dB  |
| Peaking | 1656 Hz  |  3.62 | -0.9 dB |
| Peaking | 6668 Hz  | 10.46 | 3.9 dB  |
| Peaking | 20638 Hz |  0.06 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/LucidSound%20LS31/LucidSound%20LS31.png)