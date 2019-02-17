# Bose SoundSport Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.6; 34 -3.1; 37 -3.5; 41 -4.0; 45 -4.4; 49 -4.8; 54 -5.1; 60 -5.3; 66 -5.5; 72 -5.6; 79 -5.7; 87 -5.7; 96 -5.9; 106 -6.1; 116 -6.3; 128 -6.3; 141 -6.3; 155 -6.3; 170 -6.2; 187 -6.0; 206 -5.9; 227 -5.6; 249 -5.4; 274 -5.1; 302 -4.9; 332 -4.8; 365 -4.7; 402 -4.5; 442 -4.3; 486 -4.1; 535 -4.0; 588 -3.2; 647 -3.1; 712 -2.6; 783 -2.2; 861 -2.2; 947 -3.1; 1042 -4.1; 1146 -4.5; 1261 -4.7; 1387 -5.0; 1526 -5.7; 1678 -6.4; 1846 -7.1; 2031 -7.4; 2234 -6.6; 2457 -5.4; 2703 -4.8; 2973 -4.7; 3270 -5.0; 3597 -5.3; 3957 -5.8; 4353 -6.5; 4788 -6.1; 5267 -5.4; 5793 -5.3; 6373 -4.0; 7010 -1.9; 7711 -3.5; 8482 -3.8; 9330 -3.8; 10263 -3.8; 11289 -5.1; 12418 -7.0; 13660 -7.5; 15026 -7.9; 16529 -4.9; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.61 | 3.5 dB  |
| Peaking | 123 Hz   | 0.63 | -2.7 dB |
| Peaking | 1942 Hz  | 2.61 | -3.7 dB |
| Peaking | 4427 Hz  | 3.11 | -2.7 dB |
| Peaking | 14280 Hz | 1.92 | -4.6 dB |
| Peaking | 786 Hz   | 1.82 | 3.6 dB  |
| Peaking | 878 Hz   | 0.92 | -1.7 dB |
| Peaking | 7020 Hz  | 8.94 | 2.5 dB  |
| Peaking | 10470 Hz | 2.73 | 1.1 dB  |
| Peaking | 12029 Hz | 5.05 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20Free/Bose%20SoundSport%20Free.png)