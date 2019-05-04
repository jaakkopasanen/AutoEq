# LucidSound LS31
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.5; 28 -2.7; 31 -3.8; 34 -4.6; 37 -5.4; 41 -6.2; 45 -7.0; 49 -7.8; 54 -8.7; 60 -9.5; 66 -10.1; 72 -10.4; 79 -10.7; 87 -11.0; 96 -11.2; 106 -11.4; 116 -11.5; 128 -11.7; 141 -11.8; 155 -11.8; 170 -11.7; 187 -11.6; 206 -11.3; 227 -11.2; 249 -11.2; 274 -11.1; 302 -10.8; 332 -10.6; 365 -10.1; 402 -9.4; 442 -8.4; 486 -7.2; 535 -6.5; 588 -6.0; 647 -5.7; 712 -5.1; 783 -5.1; 861 -5.8; 947 -6.4; 1042 -6.2; 1146 -5.7; 1261 -5.4; 1387 -5.3; 1526 -5.3; 1678 -4.9; 1846 -4.4; 2031 -3.7; 2234 -2.3; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -2.4; 4353 -1.4; 4788 -3.3; 5267 -4.5; 5793 -5.9; 6373 -1.8; 7010 -4.0; 7711 -7.2; 8482 -10.6; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -7.4; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`LucidSound LS31 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LucidSound LS31 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.22 | 6.5 dB  |
| Peaking | 113 Hz   | 0.6  | -5.4 dB |
| Peaking | 286 Hz   | 1.75 | -2.8 dB |
| Peaking | 2867 Hz  | 1.31 | 6.2 dB  |
| Peaking | 4398 Hz  | 3.66 | 2.1 dB  |
| Peaking | 390 Hz   | 5.29 | -1.1 dB |
| Peaking | 675 Hz   | 2.36 | 1.7 dB  |
| Peaking | 6636 Hz  | 7.99 | 4.6 dB  |
| Peaking | 8594 Hz  | 5    | -5.1 dB |
| Peaking | 19823 Hz | 2.22 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/LucidSound%20LS31/LucidSound%20LS31.png)