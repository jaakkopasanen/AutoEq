# Bose SoundSport Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.7; 25 -3.1; 28 -3.7; 31 -4.2; 34 -4.7; 37 -5.1; 41 -5.6; 45 -6.1; 49 -6.5; 54 -6.9; 60 -7.1; 66 -7.3; 72 -7.4; 79 -7.5; 87 -7.7; 96 -7.9; 106 -8.0; 116 -8.1; 128 -8.1; 141 -8.1; 155 -8.1; 170 -7.9; 187 -7.8; 206 -7.7; 227 -7.4; 249 -7.3; 274 -7.1; 302 -6.8; 332 -6.5; 365 -6.3; 402 -6.2; 442 -6.1; 486 -6.1; 535 -6.2; 588 -5.6; 647 -5.7; 712 -6.0; 783 -6.3; 861 -6.7; 947 -7.0; 1042 -6.9; 1146 -6.4; 1261 -6.1; 1387 -5.2; 1526 -4.8; 1678 -5.2; 1846 -5.2; 2031 -5.0; 2234 -4.5; 2457 -4.0; 2703 -3.5; 2973 -2.9; 3270 -2.4; 3597 -1.7; 3957 -1.0; 4353 -0.5; 4788 -0.8; 5267 -0.7; 5793 -2.0; 6373 -3.2; 7010 -2.6; 7711 -4.8; 8482 -5.0; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -8.9; 13660 -16.9; 15026 -20.8; 16529 -13.7; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.21 | 3.8 dB   |
| Peaking | 119 Hz   | 0.69 | -2.0 dB  |
| Peaking | 255 Hz   | 0.06 | -1.2 dB  |
| Peaking | 4576 Hz  | 0.9  | 5.2 dB   |
| Peaking | 14907 Hz | 2.29 | -17.9 dB |
| Peaking | 1005 Hz  | 5.44 | -1.2 dB  |
| Peaking | 7965 Hz  | 5.19 | -1.1 dB  |
| Peaking | 11461 Hz | 3.18 | 3.0 dB   |
| Peaking | 13534 Hz | 4.74 | -3.3 dB  |
| Peaking | 18116 Hz | 3.96 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | -2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -14.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Bose%20SoundSport%20Free/Bose%20SoundSport%20Free.png)