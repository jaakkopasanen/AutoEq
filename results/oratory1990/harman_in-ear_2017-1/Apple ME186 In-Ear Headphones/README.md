# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.6; 25 -6.6; 28 -6.7; 31 -6.7; 34 -6.7; 37 -6.8; 41 -6.9; 45 -6.9; 49 -7.0; 54 -7.2; 60 -7.4; 66 -7.7; 72 -7.9; 79 -8.3; 87 -8.7; 96 -9.0; 106 -9.4; 116 -9.7; 128 -10.0; 141 -10.2; 155 -10.3; 170 -10.4; 187 -10.5; 206 -10.6; 227 -10.6; 249 -10.6; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.4; 442 -9.1; 486 -8.8; 535 -8.4; 588 -8.0; 647 -7.6; 712 -7.1; 783 -6.7; 861 -6.5; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.4; 1387 -5.9; 1526 -5.2; 1678 -4.4; 1846 -3.7; 2031 -3.1; 2234 -2.7; 2457 -3.1; 2703 -4.1; 2973 -5.0; 3270 -3.9; 3597 -2.4; 3957 -2.1; 4353 -2.3; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -15.0; 15026 -23.7; 16529 -25.4; 18182 -23.7; 20000 -28.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 120 Hz   | 1.22 | -0.9 dB  |
| Peaking | 241 Hz   | 0.51 | -3.9 dB  |
| Peaking | 801 Hz   | 2.89 | 0.8 dB   |
| Peaking | 2186 Hz  | 1.59 | 3.5 dB   |
| Peaking | 5300 Hz  | 2.13 | 6.3 dB   |
| Peaking | 7218 Hz  | 0.62 | 4.7 dB   |
| Peaking | 12141 Hz | 1.7  | 9.8 dB   |
| Peaking | 15439 Hz | 1.47 | -10.0 dB |
| Peaking | 18990 Hz | 0.13 | -10.4 dB |
| Peaking | 20396 Hz | 0.48 | -10.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -24.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)