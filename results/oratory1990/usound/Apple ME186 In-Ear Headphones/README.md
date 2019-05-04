# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.3; 25 -5.4; 28 -5.4; 31 -5.4; 34 -5.5; 37 -5.5; 41 -5.6; 45 -5.7; 49 -5.8; 54 -6.0; 60 -6.2; 66 -6.4; 72 -6.7; 79 -7.0; 87 -7.4; 96 -7.8; 106 -8.1; 116 -8.5; 128 -8.7; 141 -9.0; 155 -9.1; 170 -9.3; 187 -9.3; 206 -9.4; 227 -9.4; 249 -9.3; 274 -9.2; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.5; 442 -8.3; 486 -8.0; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.4; 783 -6.0; 861 -5.7; 947 -5.5; 1042 -5.7; 1146 -5.9; 1261 -5.9; 1387 -5.7; 1526 -5.3; 1678 -4.6; 1846 -3.9; 2031 -3.6; 2234 -3.9; 2457 -4.9; 2703 -6.3; 2973 -7.2; 3270 -6.0; 3597 -4.3; 3957 -3.6; 4353 -3.3; 4788 -2.3; 5267 -1.1; 5793 -0.5; 6373 -0.7; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.3; 15026 -7.4; 16529 -6.6; 18182 -7.4; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.5  | 1.1 dB  |
| Peaking | 205 Hz   | 0.52 | -3.5 dB |
| Peaking | 2752 Hz  | 0.97 | 4.3 dB  |
| Peaking | 2916 Hz  | 3.07 | -5.7 dB |
| Peaking | 5792 Hz  | 3    | 5.4 dB  |
| Peaking | 875 Hz   | 3.5  | 0.8 dB  |
| Peaking | 1333 Hz  | 4.73 | -0.7 dB |
| Peaking | 19987 Hz | 1.62 | -5.6 dB |
| Peaking | 20347 Hz | 1.4  | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)