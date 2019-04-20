# Hifiman Edition X V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.7; 25 -2.7; 28 -2.8; 31 -2.8; 34 -2.9; 37 -2.9; 41 -2.9; 45 -2.9; 49 -2.8; 54 -3.0; 60 -3.6; 66 -4.1; 72 -4.5; 79 -4.9; 87 -5.0; 96 -5.3; 106 -5.5; 116 -5.7; 128 -6.1; 141 -6.5; 155 -7.0; 170 -7.2; 187 -7.5; 206 -8.0; 227 -8.2; 249 -8.6; 274 -8.6; 302 -7.9; 332 -6.6; 365 -5.1; 402 -6.5; 442 -7.4; 486 -7.5; 535 -7.7; 588 -8.9; 647 -6.7; 712 -3.5; 783 -6.3; 861 -7.3; 947 -6.1; 1042 -3.7; 1146 -4.7; 1261 -4.2; 1387 -2.4; 1526 -2.5; 1678 -1.3; 1846 -0.5; 2031 -0.5; 2234 -1.5; 2457 -3.4; 2703 -4.8; 2973 -5.5; 3270 -5.4; 3597 -4.9; 3957 -4.4; 4353 -4.0; 4788 -3.8; 5267 -1.4; 5793 -2.5; 6373 -4.3; 7010 -4.0; 7711 -6.0; 8482 -5.1; 9330 -5.0; 10263 -5.0; 11289 -5.1; 12418 -6.8; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.65 | 2.6 dB  |
| Peaking | 226 Hz   | 1.04 | -3.4 dB |
| Peaking | 570 Hz   | 4.63 | -3.4 dB |
| Peaking | 1863 Hz  | 2.5  | 5.0 dB  |
| Peaking | 5410 Hz  | 5.86 | 4.0 dB  |
| Peaking | 361 Hz   | 2.36 | -1.9 dB |
| Peaking | 362 Hz   | 5.93 | 3.9 dB  |
| Peaking | 2558 Hz  | 1.76 | 1.1 dB  |
| Peaking | 2910 Hz  | 3.25 | -2.3 dB |
| Peaking | 20215 Hz | 1.42 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X%20V2/Hifiman%20Edition%20X%20V2.png)