# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.9; 25 -6.9; 28 -6.9; 31 -7.0; 34 -7.0; 37 -7.1; 41 -7.1; 45 -7.2; 49 -7.3; 54 -7.5; 60 -7.7; 66 -8.0; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.2; 141 -10.5; 155 -10.6; 170 -10.7; 187 -10.8; 206 -10.9; 227 -10.9; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.2; 365 -9.9; 402 -9.6; 442 -9.4; 486 -9.1; 535 -8.7; 588 -8.3; 647 -7.9; 712 -7.4; 783 -7.0; 861 -6.7; 947 -6.7; 1042 -6.8; 1146 -6.9; 1261 -6.7; 1387 -6.2; 1526 -5.5; 1678 -4.7; 1846 -4.0; 2031 -3.4; 2234 -3.0; 2457 -3.4; 2703 -4.4; 2973 -5.3; 3270 -4.2; 3597 -2.7; 3957 -2.4; 4353 -2.5; 4788 -1.8; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.5; 13660 -15.3; 15026 -24.0; 16529 -25.7; 18182 -24.0; 20000 -28.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 123 Hz   | 1.16 | -0.6 dB  |
| Peaking | 232 Hz   | 0.44 | -4.2 dB  |
| Peaking | 785 Hz   | 2.74 | 0.8 dB   |
| Peaking | 2187 Hz  | 1.66 | 3.3 dB   |
| Peaking | 5373 Hz  | 2.22 | 6.3 dB   |
| Peaking | 7291 Hz  | 0.61 | 4.5 dB   |
| Peaking | 12089 Hz | 1.71 | 9.6 dB   |
| Peaking | 15414 Hz | 1.57 | -9.5 dB  |
| Peaking | 18301 Hz | 0.17 | -10.6 dB |
| Peaking | 20246 Hz | 0.45 | -10.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 16000 Hz | 1.41 | -24.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)