# Hifiman Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.1; 28 -2.9; 31 -3.6; 34 -4.0; 37 -4.2; 41 -4.3; 45 -4.4; 49 -4.5; 54 -4.7; 60 -5.0; 66 -5.6; 72 -6.0; 79 -6.2; 87 -6.2; 96 -6.3; 106 -6.5; 116 -6.6; 128 -6.7; 141 -7.0; 155 -7.4; 170 -7.6; 187 -7.8; 206 -8.0; 227 -8.1; 249 -7.7; 274 -7.6; 302 -7.7; 332 -7.6; 365 -7.1; 402 -6.0; 442 -6.0; 486 -6.5; 535 -6.6; 588 -6.6; 647 -6.7; 712 -7.2; 783 -7.8; 861 -5.7; 947 -6.7; 1042 -7.9; 1146 -8.0; 1261 -4.5; 1387 -3.2; 1526 -3.9; 1678 -2.9; 1846 -2.6; 2031 -2.8; 2234 -3.6; 2457 -5.1; 2703 -6.2; 2973 -6.8; 3270 -6.5; 3597 -5.9; 3957 -5.3; 4353 -4.8; 4788 -4.3; 5267 -4.0; 5793 -6.3; 6373 -7.5; 7010 -4.8; 7711 -5.6; 8482 -5.8; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.74 | 7.8 dB  |
| Peaking | 221 Hz   | 0.73 | -2.1 dB |
| Peaking | 1082 Hz  | 5.52 | -3.2 dB |
| Peaking | 1721 Hz  | 2.07 | 3.6 dB  |
| Peaking | 4990 Hz  | 6.99 | 2.0 dB  |
| Peaking | 419 Hz   | 8.34 | 1.1 dB  |
| Peaking | 753 Hz   | 7.98 | -1.8 dB |
| Peaking | 2187 Hz  | 3.2  | 1.0 dB  |
| Peaking | 2889 Hz  | 3.55 | -1.7 dB |
| Peaking | 17808 Hz | 0.5  | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X/Hifiman%20Edition%20X.png)