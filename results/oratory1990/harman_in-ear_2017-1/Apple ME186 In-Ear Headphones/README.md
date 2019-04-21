# Apple ME186 In-Ear Headphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.8; 25 -6.9; 28 -6.9; 31 -6.9; 34 -7.0; 37 -7.0; 41 -7.1; 45 -7.2; 49 -7.3; 54 -7.5; 60 -7.7; 66 -7.9; 72 -8.2; 79 -8.5; 87 -8.9; 96 -9.3; 106 -9.6; 116 -9.9; 128 -10.2; 141 -10.4; 155 -10.6; 170 -10.7; 187 -10.8; 206 -10.9; 227 -10.9; 249 -10.8; 274 -10.7; 302 -10.5; 332 -10.2; 365 -9.9; 402 -9.7; 442 -9.4; 486 -9.1; 535 -8.7; 588 -8.3; 647 -7.9; 712 -7.4; 783 -7.0; 861 -6.7; 947 -6.7; 1042 -6.8; 1146 -6.9; 1261 -6.8; 1387 -6.3; 1526 -5.5; 1678 -4.7; 1846 -4.0; 2031 -3.4; 2234 -3.1; 2457 -3.5; 2703 -4.5; 2973 -5.3; 3270 -4.1; 3597 -2.6; 3957 -2.4; 4353 -2.5; 4788 -1.8; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.5; 13660 -15.3; 15026 -24.1; 16529 -25.8; 18182 -24.2; 20000 -28.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple ME186 In-Ear Headphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple ME186 In-Ear Headphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 137 Hz   | 0.93 | -0.8 dB  |
| Peaking | 241 Hz   | 0.43 | -4.0 dB  |
| Peaking | 785 Hz   | 2.75 | 0.9 dB   |
| Peaking | 2174 Hz  | 1.65 | 3.2 dB   |
| Peaking | 5353 Hz  | 2.19 | 6.4 dB   |
| Peaking | 7547 Hz  | 0.61 | 4.1 dB   |
| Peaking | 12199 Hz | 1.71 | 9.5 dB   |
| Peaking | 15426 Hz | 1.59 | -9.4 dB  |
| Peaking | 17976 Hz | 0.2  | -10.1 dB |
| Peaking | 20501 Hz | 0.39 | -10.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 16000 Hz | 1.41 | -25.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Apple%20ME186%20In-Ear%20Headphones/Apple%20ME186%20In-Ear%20Headphones.png)