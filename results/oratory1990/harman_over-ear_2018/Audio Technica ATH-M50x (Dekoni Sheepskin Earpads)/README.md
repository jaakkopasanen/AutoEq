# Audio Technica ATH-M50x (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.4; 25 -8.0; 28 -8.9; 31 -9.5; 34 -10.0; 37 -10.4; 41 -10.7; 45 -10.9; 49 -11.1; 54 -11.2; 60 -11.3; 66 -11.4; 72 -11.4; 79 -11.3; 87 -11.2; 96 -11.1; 106 -11.1; 116 -11.2; 128 -11.0; 141 -11.3; 155 -11.7; 170 -12.0; 187 -12.0; 206 -11.7; 227 -11.0; 249 -9.8; 274 -8.2; 302 -6.2; 332 -5.2; 365 -5.4; 402 -6.3; 442 -7.3; 486 -8.0; 535 -8.3; 588 -8.0; 647 -7.8; 712 -7.8; 783 -7.3; 861 -6.6; 947 -6.1; 1042 -5.5; 1146 -4.8; 1261 -4.3; 1387 -4.4; 1526 -3.9; 1678 -3.5; 1846 -3.2; 2031 -3.2; 2234 -3.8; 2457 -4.7; 2703 -4.8; 2973 -4.3; 3270 -2.1; 3597 -0.5; 3957 -2.5; 4353 -5.5; 4788 -1.1; 5267 -0.5; 5793 -4.9; 6373 -8.1; 7010 -9.0; 7711 -6.3; 8482 -6.5; 9330 -6.7; 10263 -6.5; 11289 -6.7; 12418 -11.1; 13660 -16.3; 15026 -16.6; 16529 -13.2; 18182 -11.0; 20000 -15.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 67 Hz    | 0.55 | -5.0 dB  |
| Peaking | 185 Hz   | 2.1  | -4.1 dB  |
| Peaking | 1678 Hz  | 1.93 | 2.8 dB   |
| Peaking | 4035 Hz  | 1.28 | 4.6 dB   |
| Peaking | 15143 Hz | 1.26 | -10.8 dB |
| Peaking | 344 Hz   | 4.06 | 3.1 dB   |
| Peaking | 564 Hz   | 1.95 | -1.8 dB  |
| Peaking | 5278 Hz  | 8.5  | 4.4 dB   |
| Peaking | 6617 Hz  | 5.24 | -4.1 dB  |
| Peaking | 10810 Hz | 3.82 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -11.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads)/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads).png)