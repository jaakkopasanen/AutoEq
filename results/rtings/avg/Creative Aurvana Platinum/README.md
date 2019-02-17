# Creative Aurvana Platinum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -8.3; 25 -9.3; 28 -10.6; 31 -11.5; 34 -12.3; 37 -12.8; 41 -13.4; 45 -13.8; 49 -14.1; 54 -14.4; 60 -14.8; 66 -15.2; 72 -15.6; 79 -16.1; 87 -16.6; 96 -17.0; 106 -17.5; 116 -17.9; 128 -18.2; 141 -18.5; 155 -18.7; 170 -18.7; 187 -18.7; 206 -18.5; 227 -18.3; 249 -18.2; 274 -18.1; 302 -17.9; 332 -17.8; 365 -17.7; 402 -17.7; 442 -17.7; 486 -17.2; 535 -15.6; 588 -13.3; 647 -10.5; 712 -8.8; 783 -8.4; 861 -7.7; 947 -5.2; 1042 -5.5; 1146 -7.0; 1261 -8.6; 1387 -9.2; 1526 -8.1; 1678 -6.6; 1846 -5.1; 2031 -3.4; 2234 -1.9; 2457 -0.5; 2703 -0.8; 2973 -2.4; 3270 -4.4; 3597 -6.7; 3957 -9.0; 4353 -8.4; 4788 -7.1; 5267 -7.6; 5793 -9.1; 6373 -7.9; 7010 -6.4; 7711 -8.0; 8482 -11.4; 9330 -12.6; 10263 -11.6; 11289 -11.4; 12418 -11.8; 13660 -10.9; 15026 -9.3; 16529 -8.1; 18182 -9.0; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 80 Hz    | 0.36 | -9.1 dB |
| Peaking | 231 Hz   | 0.67 | -7.8 dB |
| Peaking | 458 Hz   | 1.99 | -6.9 dB |
| Peaking | 2589 Hz  | 2.6  | 7.7 dB  |
| Peaking | 17081 Hz | 0.09 | -5.2 dB |
| Peaking | 982 Hz   | 4.63 | 3.0 dB  |
| Peaking | 1371 Hz  | 4.37 | -3.3 dB |
| Peaking | 7307 Hz  | 2.87 | 5.7 dB  |
| Peaking | 8761 Hz  | 1.47 | -4.2 dB |
| Peaking | 16727 Hz | 2.13 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -7.5 dB  |
| Peaking | 125 Hz   | 1.41 | -10.2 dB |
| Peaking | 250 Hz   | 1.41 | -10.7 dB |
| Peaking | 500 Hz   | 1.41 | -9.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB  |
| Peaking | 16000 Hz | 1.41 | -6.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Aurvana%20Platinum/Creative%20Aurvana%20Platinum.png)