# Audio Technica ATH-M50x (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.8; 25 -7.5; 28 -8.4; 31 -9.1; 34 -9.6; 37 -10.0; 41 -10.4; 45 -10.7; 49 -10.9; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.2; 79 -11.1; 87 -11.0; 96 -10.9; 106 -11.0; 116 -11.1; 128 -10.9; 141 -11.2; 155 -11.6; 170 -11.9; 187 -11.8; 206 -11.5; 227 -10.9; 249 -9.8; 274 -8.2; 302 -6.2; 332 -5.3; 365 -5.4; 402 -6.3; 442 -7.3; 486 -8.0; 535 -8.3; 588 -8.1; 647 -8.0; 712 -7.8; 783 -7.3; 861 -6.7; 947 -6.2; 1042 -5.6; 1146 -4.8; 1261 -4.2; 1387 -4.1; 1526 -3.4; 1678 -3.1; 1846 -3.0; 2031 -3.3; 2234 -4.1; 2457 -5.1; 2703 -5.2; 2973 -4.7; 3270 -2.6; 3597 -0.5; 3957 -2.7; 4353 -6.3; 4788 -1.8; 5267 -0.5; 5793 -4.9; 6373 -7.1; 7010 -8.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.6; 13660 -15.4; 15026 -15.8; 16529 -12.8; 18182 -10.9; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 68 Hz    | 0.58 | -4.7 dB |
| Peaking | 185 Hz   | 2.04 | -4.1 dB |
| Peaking | 1650 Hz  | 2.18 | 3.2 dB  |
| Peaking | 4168 Hz  | 1.15 | 4.1 dB  |
| Peaking | 15270 Hz | 1.18 | -9.8 dB |
| Peaking | 344 Hz   | 4.07 | 3.0 dB  |
| Peaking | 572 Hz   | 1.93 | -1.9 dB |
| Peaking | 5271 Hz  | 9.65 | 4.2 dB  |
| Peaking | 6619 Hz  | 4.99 | -3.1 dB |
| Peaking | 10816 Hz | 3.86 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -10.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads)/Audio%20Technica%20ATH-M50x%20(Dekoni%20Sheepskin%20Earpads).png)