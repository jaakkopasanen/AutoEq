# Axelvox HD 271
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.4; 45 -1.8; 49 -2.1; 54 -2.4; 60 -2.7; 66 -2.8; 72 -2.5; 79 -2.1; 87 -1.7; 96 -1.5; 106 -1.1; 116 -0.5; 128 -0.5; 141 -0.6; 155 -0.6; 170 -0.9; 187 -1.3; 206 -1.9; 227 -2.8; 249 -3.9; 274 -4.8; 302 -5.6; 332 -6.3; 365 -6.9; 402 -7.3; 442 -7.4; 486 -6.5; 535 -5.8; 588 -6.3; 647 -6.9; 712 -7.1; 783 -7.3; 861 -7.6; 947 -7.7; 1042 -7.7; 1146 -8.0; 1261 -8.1; 1387 -8.1; 1526 -7.9; 1678 -7.2; 1846 -6.4; 2031 -7.0; 2234 -8.1; 2457 -8.2; 2703 -7.2; 2973 -5.7; 3270 -3.8; 3597 -1.9; 3957 -0.6; 4353 -4.7; 4788 -10.1; 5267 -11.8; 5793 -11.2; 6373 -11.7; 7010 -14.0; 7711 -15.9; 8482 -15.5; 9330 -12.8; 10263 -10.9; 11289 -12.3; 12418 -14.5; 13660 -14.1; 15026 -10.7; 16529 -6.7; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Axelvox HD 271 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Axelvox HD 271 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.4  | 6.0 dB  |
| Peaking | 144 Hz   | 1.14 | 5.6 dB  |
| Peaking | 3822 Hz  | 1.97 | 13.8 dB |
| Peaking | 5835 Hz  | 0.5  | -9.8 dB |
| Peaking | 13293 Hz | 2.96 | -5.5 dB |
| Peaking | 1152 Hz  | 0.35 | -0.7 dB |
| Peaking | 1861 Hz  | 4.74 | 2.3 dB  |
| Peaking | 6212 Hz  | 6.58 | 2.8 dB  |
| Peaking | 7985 Hz  | 6.24 | -2.7 dB |
| Peaking | 17054 Hz | 2.65 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.5 dB   |
| Peaking | 125 Hz   | 1.41 | 6.1 dB   |
| Peaking | 250 Hz   | 1.41 | 1.7 dB   |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Axelvox%20HD%20271/Axelvox%20HD%20271.png)