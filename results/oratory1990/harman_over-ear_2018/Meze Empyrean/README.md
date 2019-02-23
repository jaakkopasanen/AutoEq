# Meze Empyrean
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.1; 25 -5.2; 28 -5.3; 31 -5.4; 34 -5.6; 37 -5.6; 41 -5.7; 45 -5.7; 49 -5.8; 54 -5.9; 60 -6.0; 66 -6.3; 72 -6.6; 79 -6.7; 87 -7.1; 96 -7.4; 106 -7.8; 116 -8.1; 128 -8.4; 141 -8.8; 155 -9.0; 170 -9.0; 187 -8.8; 206 -8.4; 227 -7.6; 249 -7.6; 274 -8.1; 302 -8.0; 332 -7.7; 365 -7.4; 402 -7.6; 442 -7.5; 486 -6.0; 535 -5.4; 588 -6.2; 647 -6.6; 712 -6.3; 783 -6.0; 861 -6.4; 947 -5.6; 1042 -5.7; 1146 -5.3; 1261 -4.3; 1387 -3.4; 1526 -2.9; 1678 -2.1; 1846 -1.2; 2031 -0.5; 2234 -0.8; 2457 -1.4; 2703 -1.5; 2973 -2.0; 3270 -3.3; 3597 -4.9; 3957 -5.5; 4353 -5.1; 4788 -4.4; 5267 -3.6; 5793 -2.0; 6373 -1.3; 7010 -2.4; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -6.0; 12418 -6.7; 13660 -5.5; 15026 -7.7; 16529 -10.2; 18182 -12.1; 20000 -19.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Empyrean GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Empyrean ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 153 Hz   | 0.75 | -3.9 dB  |
| Peaking | 364 Hz   | 1.94 | -1.5 dB  |
| Peaking | 854 Hz   | 1.62 | -1.4 dB  |
| Peaking | 2103 Hz  | 1.64 | 4.7 dB   |
| Peaking | 6347 Hz  | 4.91 | 4.0 dB   |
| Peaking | 1136 Hz  | 6.13 | -1.0 dB  |
| Peaking | 1227 Hz  | 2.37 | 0.6 dB   |
| Peaking | 13830 Hz | 5.25 | 1.7 dB   |
| Peaking | 20156 Hz | 0.55 | -13.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%20Empyrean/Meze%20Empyrean.png)