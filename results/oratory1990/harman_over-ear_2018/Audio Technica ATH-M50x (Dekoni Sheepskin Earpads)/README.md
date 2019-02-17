# Audio Technica ATH-M50x (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.4; 25 -8.1; 28 -9.0; 31 -9.7; 34 -10.2; 37 -10.6; 41 -11.0; 45 -11.3; 49 -11.4; 54 -11.6; 60 -11.7; 66 -11.8; 72 -11.8; 79 -11.7; 87 -11.6; 96 -11.5; 106 -11.6; 116 -11.7; 128 -11.5; 141 -11.8; 155 -12.2; 170 -12.4; 187 -12.4; 206 -12.1; 227 -11.5; 249 -10.3; 274 -8.8; 302 -6.8; 332 -5.9; 365 -6.0; 402 -6.9; 442 -7.9; 486 -8.6; 535 -8.9; 588 -8.7; 647 -8.5; 712 -8.4; 783 -7.9; 861 -7.2; 947 -6.8; 1042 -6.2; 1146 -5.4; 1261 -4.8; 1387 -4.7; 1526 -4.0; 1678 -3.6; 1846 -3.6; 2031 -3.9; 2234 -4.7; 2457 -5.7; 2703 -5.8; 2973 -5.2; 3270 -3.2; 3597 -0.7; 3957 -3.3; 4353 -6.9; 4788 -2.4; 5267 -0.5; 5793 -5.5; 6373 -7.7; 7010 -8.9; 7711 -6.3; 8482 -6.5; 9330 -7.1; 10263 -6.7; 11289 -7.0; 12418 -11.2; 13660 -15.9; 15026 -16.4; 16529 -13.4; 18182 -11.4; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 73 Hz    | 0.45 | -5.3 dB  |
| Peaking | 189 Hz   | 2.19 | -3.7 dB  |
| Peaking | 1678 Hz  | 2.71 | 2.8 dB   |
| Peaking | 4211 Hz  | 1.21 | 3.7 dB   |
| Peaking | 15420 Hz | 1.05 | -10.1 dB |
| Peaking | 343 Hz   | 3.98 | 2.9 dB   |
| Peaking | 580 Hz   | 1.77 | -2.2 dB  |
| Peaking | 5246 Hz  | 9.85 | 4.7 dB   |
| Peaking | 6572 Hz  | 4.8  | -3.3 dB  |
| Peaking | 10761 Hz | 4.17 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -11.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads)/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads).png)