# Astell & Kern Rosie 2 o’clock
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.4; 25 -7.6; 28 -8.0; 31 -8.3; 34 -8.5; 37 -8.8; 41 -9.1; 45 -9.4; 49 -9.5; 54 -9.8; 60 -10.1; 66 -10.4; 72 -10.8; 79 -11.1; 87 -11.5; 96 -11.8; 106 -12.2; 116 -12.3; 128 -12.5; 141 -12.7; 155 -12.8; 170 -12.8; 187 -12.7; 206 -12.5; 227 -12.4; 249 -12.1; 274 -11.8; 302 -11.4; 332 -10.9; 365 -10.4; 402 -9.9; 442 -9.5; 486 -8.9; 535 -8.3; 588 -7.6; 647 -7.0; 712 -6.3; 783 -5.6; 861 -5.0; 947 -4.7; 1042 -4.7; 1146 -5.2; 1261 -6.0; 1387 -6.1; 1526 -5.6; 1678 -5.0; 1846 -4.4; 2031 -3.6; 2234 -2.3; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -3.2; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -9.2; 8482 -11.1; 9330 -9.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -10.6; 15026 -16.2; 16529 -17.4; 18182 -23.6; 20000 -28.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern Rosie 2 o’clock GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern Rosie 2 o’clock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 0.5  | -5.2 dB  |
| Peaking | 262 Hz   | 1.01 | -3.0 dB  |
| Peaking | 3403 Hz  | 0.91 | 6.9 dB   |
| Peaking | 6195 Hz  | 6.62 | 4.7 dB   |
| Peaking | 19405 Hz | 0.65 | -22.6 dB |
| Peaking | 903 Hz   | 3.76 | 2.0 dB   |
| Peaking | 6874 Hz  | 6.17 | 2.3 dB   |
| Peaking | 8327 Hz  | 3.35 | -5.9 dB  |
| Peaking | 12691 Hz | 1.51 | 6.9 dB   |
| Peaking | 14682 Hz | 1.97 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -14.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Astell%20&%20Kern%20Rosie%202%20o%E2%80%99clock/Astell%20&%20Kern%20Rosie%202%20o%E2%80%99clock.png)