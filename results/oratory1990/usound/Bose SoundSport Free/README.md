# Bose SoundSport Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.5; 34 -3.0; 37 -3.4; 41 -3.9; 45 -4.4; 49 -4.8; 54 -5.1; 60 -5.4; 66 -5.6; 72 -5.7; 79 -5.8; 87 -6.0; 96 -6.1; 106 -6.3; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.3; 170 -6.2; 187 -6.1; 206 -5.9; 227 -5.7; 249 -5.5; 274 -5.4; 302 -5.2; 332 -5.0; 365 -4.9; 402 -4.8; 442 -4.7; 486 -4.8; 535 -5.0; 588 -4.3; 647 -4.5; 712 -4.8; 783 -5.1; 861 -5.4; 947 -5.6; 1042 -5.6; 1146 -5.2; 1261 -5.0; 1387 -4.5; 1526 -4.4; 1678 -4.8; 1846 -4.8; 2031 -5.0; 2234 -5.1; 2457 -5.2; 2703 -5.0; 2973 -4.6; 3270 -4.0; 3597 -3.1; 3957 -2.0; 4353 -1.1; 4788 -1.1; 5267 -1.0; 5793 -2.5; 6373 -4.1; 7010 -3.0; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -5.8; 13660 -7.4; 15026 -4.9; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.08 | 4.2 dB  |
| Peaking | 119 Hz   | 0.61 | -2.0 dB |
| Peaking | 3146 Hz  | 0.57 | -1.2 dB |
| Peaking | 4656 Hz  | 1.74 | 4.8 dB  |
| Peaking | 13565 Hz | 4.16 | -3.2 dB |
| Peaking | 977 Hz   | 4.09 | -0.9 dB |
| Peaking | 1496 Hz  | 5.21 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Bose%20SoundSport%20Free/Bose%20SoundSport%20Free.png)