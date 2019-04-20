# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.4; 28 -5.4; 31 -5.5; 34 -5.5; 37 -5.6; 41 -5.6; 45 -5.7; 49 -5.8; 54 -6.0; 60 -6.2; 66 -6.4; 72 -6.7; 79 -7.1; 87 -7.4; 96 -7.8; 106 -8.2; 116 -8.5; 128 -8.7; 141 -8.9; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.4; 227 -9.4; 249 -9.3; 274 -9.2; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.4; 442 -8.2; 486 -8.0; 535 -7.6; 588 -7.3; 647 -6.9; 712 -6.4; 783 -6.0; 861 -5.7; 947 -5.5; 1042 -5.6; 1146 -5.8; 1261 -5.9; 1387 -5.7; 1526 -5.2; 1678 -4.5; 1846 -3.9; 2031 -3.6; 2234 -3.8; 2457 -4.7; 2703 -6.2; 2973 -7.2; 3270 -6.1; 3597 -4.3; 3957 -3.7; 4353 -3.3; 4788 -2.3; 5267 -1.1; 5793 -0.5; 6373 -0.6; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.2; 15026 -7.3; 16529 -6.5; 18182 -7.2; 20000 -16.4
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.55 | 1.1 dB   |
| Peaking | 203 Hz   | 0.51 | -3.5 dB  |
| Peaking | 2698 Hz  | 0.96 | 4.2 dB   |
| Peaking | 2971 Hz  | 3.15 | -5.6 dB  |
| Peaking | 5815 Hz  | 3.01 | 5.4 dB   |
| Peaking | 878 Hz   | 3.52 | 0.8 dB   |
| Peaking | 1342 Hz  | 4.04 | -0.7 dB  |
| Peaking | 6636 Hz  | 7.02 | 1.8 dB   |
| Peaking | 7830 Hz  | 2.86 | -1.4 dB  |
| Peaking | 19922 Hz | 1.76 | -10.1 dB |

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
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)