# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.4; 25 -5.4; 28 -5.5; 31 -5.5; 34 -5.6; 37 -5.6; 41 -5.7; 45 -5.7; 49 -5.8; 54 -6.0; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.1; 87 -7.5; 96 -7.9; 106 -8.2; 116 -8.5; 128 -8.8; 141 -9.0; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.4; 227 -9.4; 249 -9.4; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.2; 486 -8.0; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.5; 783 -6.0; 861 -5.7; 947 -5.6; 1042 -5.7; 1146 -5.9; 1261 -5.9; 1387 -5.7; 1526 -5.3; 1678 -4.6; 1846 -3.9; 2031 -3.6; 2234 -3.8; 2457 -4.8; 2703 -6.2; 2973 -7.3; 3270 -6.1; 3597 -4.4; 3957 -3.7; 4353 -3.4; 4788 -2.4; 5267 -1.2; 5793 -0.6; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -6.1; 15026 -7.4; 16529 -6.5; 18182 -7.3; 20000 -16.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 219 Hz   | 0.53 | -4.0 dB  |
| Peaking | 2096 Hz  | 1.86 | 2.2 dB   |
| Peaking | 2917 Hz  | 5.09 | -3.0 dB  |
| Peaking | 5699 Hz  | 2.29 | 5.5 dB   |
| Peaking | 20118 Hz | 1.34 | -10.7 dB |
| Peaking | 878 Hz   | 4.59 | 0.8 dB   |
| Peaking | 4111 Hz  | 1.93 | 1.5 dB   |
| Peaking | 6612 Hz  | 6.91 | 2.6 dB   |
| Peaking | 7743 Hz  | 0.52 | -1.6 dB  |
| Peaking | 10824 Hz | 1.6  | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)