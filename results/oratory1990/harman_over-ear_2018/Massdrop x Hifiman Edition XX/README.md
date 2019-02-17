# Massdrop x Hifiman Edition XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.8; 28 -3.8; 31 -3.8; 34 -3.8; 37 -3.6; 41 -3.6; 45 -4.2; 49 -4.8; 54 -4.8; 60 -4.8; 66 -5.3; 72 -5.5; 79 -5.6; 87 -5.8; 96 -6.2; 106 -6.6; 116 -6.8; 128 -7.2; 141 -7.5; 155 -7.9; 170 -8.1; 187 -8.6; 206 -9.0; 227 -9.0; 249 -9.1; 274 -7.9; 302 -6.3; 332 -7.1; 365 -7.6; 402 -8.1; 442 -8.8; 486 -8.9; 535 -7.0; 588 -4.9; 647 -6.1; 712 -6.8; 783 -6.7; 861 -4.5; 947 -5.7; 1042 -6.8; 1146 -2.3; 1261 -1.7; 1387 -1.2; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -1.8; 2457 -3.9; 2703 -5.3; 2973 -6.0; 3270 -5.7; 3597 -4.7; 3957 -4.3; 4353 -4.4; 4788 -6.6; 5267 -4.5; 5793 -5.1; 6373 -4.9; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman Edition XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman Edition XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.19 | 3.1 dB  |
| Peaking | 187 Hz  | 0.48 | -3.4 dB |
| Peaking | 1032 Hz | 9.15 | -3.1 dB |
| Peaking | 1600 Hz | 1.22 | 6.7 dB  |
| Peaking | 6145 Hz | 2.36 | 1.5 dB  |
| Peaking | 308 Hz  | 6.58 | 2.3 dB  |
| Peaking | 518 Hz  | 2.59 | -2.7 dB |
| Peaking | 572 Hz  | 6.24 | 4.1 dB  |
| Peaking | 2964 Hz | 5.4  | -1.7 dB |
| Peaking | 3935 Hz | 5.88 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20Edition%20XX/Massdrop%20x%20Hifiman%20Edition%20XX.png)