# Hifiman Edition X V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.8; 25 -2.8; 28 -2.9; 31 -2.9; 34 -2.9; 37 -3.0; 41 -3.0; 45 -3.0; 49 -2.9; 54 -3.0; 60 -3.7; 66 -4.2; 72 -4.6; 79 -4.9; 87 -5.1; 96 -5.3; 106 -5.6; 116 -5.8; 128 -6.2; 141 -6.6; 155 -7.1; 170 -7.3; 187 -7.5; 206 -8.0; 227 -8.3; 249 -8.6; 274 -8.8; 302 -7.8; 332 -6.8; 365 -5.1; 402 -6.6; 442 -7.5; 486 -7.5; 535 -7.8; 588 -8.8; 647 -7.2; 712 -3.5; 783 -6.3; 861 -7.3; 947 -6.5; 1042 -3.6; 1146 -4.7; 1261 -4.6; 1387 -2.3; 1526 -2.6; 1678 -1.5; 1846 -0.6; 2031 -0.5; 2234 -1.6; 2457 -3.5; 2703 -4.9; 2973 -5.5; 3270 -5.5; 3597 -5.0; 3957 -4.5; 4353 -4.1; 4788 -3.9; 5267 -1.4; 5793 -2.7; 6373 -4.5; 7010 -4.1; 7711 -6.1; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -6.9; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.65 | 2.5 dB  |
| Peaking | 226 Hz   | 1.03 | -3.4 dB |
| Peaking | 574 Hz   | 4.62 | -3.4 dB |
| Peaking | 1863 Hz  | 2.5  | 5.0 dB  |
| Peaking | 5426 Hz  | 6.32 | 4.2 dB  |
| Peaking | 356 Hz   | 6.9  | 3.8 dB  |
| Peaking | 357 Hz   | 2.36 | -1.7 dB |
| Peaking | 2925 Hz  | 1.02 | 1.1 dB  |
| Peaking | 3095 Hz  | 3.29 | -2.3 dB |
| Peaking | 16352 Hz | 0.12 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
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