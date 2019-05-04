# Bose SoundSport Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.5; 28 -5.2; 31 -5.7; 34 -6.2; 37 -6.6; 41 -7.1; 45 -7.5; 49 -7.9; 54 -8.0; 60 -8.0; 66 -7.9; 72 -7.8; 79 -7.7; 87 -7.5; 96 -7.3; 106 -7.0; 116 -6.7; 128 -6.3; 141 -5.8; 155 -5.4; 170 -5.0; 187 -4.5; 206 -4.1; 227 -3.7; 249 -3.5; 274 -3.4; 302 -3.2; 332 -3.0; 365 -2.9; 402 -2.7; 442 -2.6; 486 -2.4; 535 -2.2; 588 -1.5; 647 -1.3; 712 -0.9; 783 -0.5; 861 -0.6; 947 -1.5; 1042 -2.4; 1146 -2.9; 1261 -3.0; 1387 -3.4; 1526 -4.0; 1678 -4.9; 1846 -5.7; 2031 -6.0; 2234 -5.6; 2457 -4.5; 2703 -3.6; 2973 -3.0; 3270 -2.9; 3597 -3.2; 3957 -3.6; 4353 -4.2; 4788 -4.8; 5267 -4.0; 5793 -3.3; 6373 -1.2; 7010 -0.7; 7711 -2.8; 8482 -3.1; 9330 -3.1; 10263 -3.1; 11289 -4.5; 12418 -5.5; 13660 -4.9; 15026 -5.6; 16529 -3.4; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 66 Hz    | 0.61 | -5.1 dB |
| Peaking | 753 Hz   | 1.42 | 2.7 dB  |
| Peaking | 1961 Hz  | 2.3  | -3.2 dB |
| Peaking | 6736 Hz  | 7.67 | 3.4 dB  |
| Peaking | 13817 Hz | 1.42 | -2.4 dB |
| Peaking | 19 Hz    | 1.99 | 1.1 dB  |
| Peaking | 1106 Hz  | 8.57 | -0.5 dB |
| Peaking | 3083 Hz  | 4.35 | 0.9 dB  |
| Peaking | 4750 Hz  | 4.33 | -1.7 dB |
| Peaking | 9869 Hz  | 4.73 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20Free/Bose%20SoundSport%20Free.png)