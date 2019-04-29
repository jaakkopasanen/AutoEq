# Delta Air complimentary earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.7; 128 -2.7; 141 -3.9; 155 -5.3; 170 -6.4; 187 -8.9; 206 -9.9; 227 -11.6; 249 -12.2; 274 -14.4; 302 -16.6; 332 -18.9; 365 -20.8; 402 -22.3; 442 -23.5; 486 -24.9; 535 -26.5; 588 -27.1; 647 -26.1; 712 -24.1; 783 -20.6; 861 -17.1; 947 -15.3; 1042 -11.9; 1146 -9.7; 1261 -7.5; 1387 -4.8; 1526 -1.1; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -2.7; 2973 -5.0; 3270 -3.6; 3597 -2.7; 3957 -2.4; 4353 -4.9; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Delta Air complimentary earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Delta Air complimentary earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 111 Hz  | 0.29 | 17.8 dB  |
| Peaking | 576 Hz  | 0.32 | -33.6 dB |
| Peaking | 1645 Hz | 0.81 | 13.7 dB  |
| Peaking | 2112 Hz | 0.41 | 9.7 dB   |
| Peaking | 5763 Hz | 2.32 | 7.0 dB   |
| Peaking | 22 Hz   | 2.36 | 2.2 dB   |
| Peaking | 495 Hz  | 8.02 | 0.7 dB   |
| Peaking | 2543 Hz | 5.51 | 2.6 dB   |
| Peaking | 2893 Hz | 3.61 | -3.0 dB  |
| Peaking | 3601 Hz | 5.41 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 5.1 dB   |
| Peaking | 125 Hz   | 1.41 | 6.0 dB   |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -23.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 9.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Delta%20Air%20complimentary%20earphones/Delta%20Air%20complimentary%20earphones.png)