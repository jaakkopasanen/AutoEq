# Mee Audio Pinnacle PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.1; 28 -2.5; 31 -2.8; 34 -3.1; 37 -3.3; 41 -3.6; 45 -3.9; 49 -4.1; 54 -4.4; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.5; 106 -6.8; 116 -7.0; 128 -7.2; 141 -7.2; 155 -7.2; 170 -8.5; 187 -8.6; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.3; 302 -6.9; 332 -6.4; 365 -6.3; 402 -5.9; 442 -5.5; 486 -4.9; 535 -4.3; 588 -3.7; 647 -3.2; 712 -2.6; 783 -2.0; 861 -1.5; 947 -1.3; 1042 -1.3; 1146 -1.5; 1261 -1.8; 1387 -1.6; 1526 -1.3; 1678 -0.5; 1846 -0.5; 2031 -0.8; 2234 -1.6; 2457 -3.0; 2703 -4.6; 2973 -5.3; 3270 -4.8; 3597 -4.0; 3957 -4.0; 4353 -5.1; 4788 -6.5; 5267 -7.0; 5793 -3.6; 6373 -1.1; 7010 -1.5; 7711 -5.3; 8482 -6.0; 9330 -2.1; 10263 -1.3; 11289 -3.9; 12418 -8.1; 13660 -10.7; 15026 -13.0; 16529 -11.3; 18182 -5.3; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 172 Hz   | 0.44 | -7.0 dB |
| Peaking | 3018 Hz  | 3.91 | -3.9 dB |
| Peaking | 4939 Hz  | 3.72 | -5.7 dB |
| Peaking | 14419 Hz | 1.58 | -8.8 dB |
| Peaking | 16455 Hz | 1.64 | -6.7 dB |
| Peaking | 912 Hz   | 3.35 | 1.3 dB  |
| Peaking | 1816 Hz  | 3.59 | 1.7 dB  |
| Peaking | 6759 Hz  | 3.21 | 6.0 dB  |
| Peaking | 8178 Hz  | 1.58 | -7.5 dB |
| Peaking | 9848 Hz  | 2.92 | 6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -13.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Mee%20Audio%20Pinnacle%20PX/Mee%20Audio%20Pinnacle%20PX.png)