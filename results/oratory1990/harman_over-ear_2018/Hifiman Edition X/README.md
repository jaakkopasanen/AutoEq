# Hifiman Edition X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.1; 28 -1.9; 31 -2.5; 34 -2.9; 37 -3.1; 41 -3.2; 45 -3.3; 49 -3.4; 54 -3.6; 60 -3.9; 66 -4.5; 72 -4.9; 79 -5.1; 87 -5.1; 96 -5.2; 106 -5.4; 116 -5.5; 128 -5.6; 141 -5.9; 155 -6.3; 170 -6.5; 187 -6.7; 206 -6.9; 227 -7.0; 249 -6.6; 274 -6.5; 302 -6.6; 332 -6.5; 365 -6.0; 402 -4.9; 442 -5.0; 486 -5.3; 535 -5.5; 588 -5.5; 647 -5.6; 712 -6.0; 783 -7.0; 861 -4.3; 947 -5.6; 1042 -6.8; 1146 -6.9; 1261 -3.3; 1387 -2.2; 1526 -2.7; 1678 -1.9; 1846 -1.5; 2031 -1.7; 2234 -2.5; 2457 -4.0; 2703 -5.0; 2973 -5.7; 3270 -5.4; 3597 -4.8; 3957 -4.2; 4353 -3.7; 4788 -3.3; 5267 -2.8; 5793 -5.2; 6373 -6.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.12 | 5.6 dB  |
| Peaking | 51 Hz    | 0.98 | 2.0 dB  |
| Peaking | 440 Hz   | 3.77 | 1.6 dB  |
| Peaking | 1796 Hz  | 1.74 | 5.3 dB  |
| Peaking | 4878 Hz  | 2.83 | 3.4 dB  |
| Peaking | 218 Hz   | 3.37 | -0.8 dB |
| Peaking | 884 Hz   | 8.81 | 2.1 dB  |
| Peaking | 1164 Hz  | 3.02 | -2.9 dB |
| Peaking | 1310 Hz  | 7.52 | 4.4 dB  |
| Peaking | 19985 Hz | 3.15 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X/Hifiman%20Edition%20X.png)