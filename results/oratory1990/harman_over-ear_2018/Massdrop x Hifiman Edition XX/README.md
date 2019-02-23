# Massdrop x Hifiman Edition XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.7; 25 -4.7; 28 -4.7; 31 -4.7; 34 -4.6; 37 -4.5; 41 -4.5; 45 -5.1; 49 -5.6; 54 -5.7; 60 -5.7; 66 -6.2; 72 -6.3; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.4; 116 -7.7; 128 -8.0; 141 -8.4; 155 -8.7; 170 -9.0; 187 -9.5; 206 -9.8; 227 -9.9; 249 -10.0; 274 -8.8; 302 -7.2; 332 -8.0; 365 -8.5; 402 -9.0; 442 -9.6; 486 -9.8; 535 -7.9; 588 -5.7; 647 -7.0; 712 -7.6; 783 -7.6; 861 -5.4; 947 -6.6; 1042 -7.7; 1146 -3.1; 1261 -2.6; 1387 -2.1; 1526 -0.8; 1678 -1.0; 1846 -0.5; 2031 -1.0; 2234 -2.7; 2457 -4.7; 2703 -6.2; 2973 -6.8; 3270 -6.6; 3597 -5.6; 3957 -5.1; 4353 -5.3; 4788 -7.5; 5267 -5.4; 5793 -5.9; 6373 -5.8; 7010 -5.2; 7711 -6.5; 8482 -6.0; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman Edition XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman Edition XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.97 | 1.7 dB  |
| Peaking | 201 Hz  |  0.99 | -3.7 dB |
| Peaking | 461 Hz  |  3.71 | -3.3 dB |
| Peaking | 1016 Hz |  9.09 | -3.0 dB |
| Peaking | 1650 Hz |  1.81 | 6.1 dB  |
| Peaking | 578 Hz  | 12.53 | 1.8 dB  |
| Peaking | 740 Hz  |  6.67 | -1.9 dB |
| Peaking | 1187 Hz | 12.09 | 2.0 dB  |
| Peaking | 2084 Hz |  6.85 | 1.6 dB  |
| Peaking | 2919 Hz |  4.14 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20Edition%20XX/Massdrop%20x%20Hifiman%20Edition%20XX.png)