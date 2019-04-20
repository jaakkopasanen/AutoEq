# Hifiman Ananda
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.2; 25 -2.4; 28 -2.6; 31 -2.8; 34 -3.0; 37 -3.1; 41 -3.1; 45 -3.0; 49 -3.0; 54 -3.2; 60 -4.0; 66 -4.6; 72 -4.6; 79 -4.8; 87 -5.0; 96 -5.3; 106 -5.6; 116 -5.9; 128 -6.2; 141 -6.5; 155 -6.8; 170 -7.0; 187 -7.2; 206 -7.5; 227 -7.5; 249 -7.0; 274 -6.9; 302 -7.0; 332 -6.4; 365 -5.8; 402 -6.6; 442 -6.6; 486 -7.2; 535 -7.8; 588 -7.9; 647 -7.5; 712 -4.4; 783 -4.0; 861 -5.8; 947 -6.7; 1042 -5.8; 1146 -3.2; 1261 -2.2; 1387 -1.2; 1526 -1.0; 1678 -0.5; 1846 -1.3; 2031 -1.7; 2234 -2.5; 2457 -4.1; 2703 -5.9; 2973 -6.9; 3270 -7.0; 3597 -6.5; 3957 -6.0; 4353 -6.2; 4788 -5.8; 5267 -3.9; 5793 -4.1; 6373 -6.8; 7010 -6.4; 7711 -5.5; 8482 -5.2; 9330 -5.3; 10263 -5.8; 11289 -8.7; 12418 -6.6; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -12.1; 20000 -18.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.33 | 3.1 dB   |
| Peaking | 197 Hz   | 0.85 | -2.3 dB  |
| Peaking | 562 Hz   | 3.68 | -2.8 dB  |
| Peaking | 1618 Hz  | 2.27 | 5.3 dB   |
| Peaking | 19633 Hz | 1.29 | -13.8 dB |
| Peaking | 973 Hz   | 7.13 | -2.8 dB  |
| Peaking | 1708 Hz  | 0.51 | 0.8 dB   |
| Peaking | 3195 Hz  | 2.6  | -2.9 dB  |
| Peaking | 11441 Hz | 5.75 | -3.7 dB  |
| Peaking | 15979 Hz | 2.08 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Ananda/Hifiman%20Ananda.png)