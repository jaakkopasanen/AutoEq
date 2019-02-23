# Bose SoundSport Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.5; 25 -2.8; 28 -3.2; 31 -3.4; 34 -3.7; 37 -3.9; 41 -4.0; 45 -4.0; 49 -4.1; 54 -4.2; 60 -4.3; 66 -4.5; 72 -4.6; 79 -4.5; 87 -4.6; 96 -4.8; 106 -5.0; 116 -5.1; 128 -5.2; 141 -5.1; 155 -5.1; 170 -5.0; 187 -4.9; 206 -4.7; 227 -4.4; 249 -4.2; 274 -3.9; 302 -3.5; 332 -4.0; 365 -3.1; 402 -2.5; 442 -2.3; 486 -1.9; 535 -1.5; 588 -1.1; 647 -0.7; 712 -0.5; 783 -0.6; 861 -1.1; 947 -1.9; 1042 -2.6; 1146 -2.7; 1261 -2.7; 1387 -2.6; 1526 -2.9; 1678 -3.6; 1846 -4.3; 2031 -4.7; 2234 -3.7; 2457 -2.7; 2703 -2.6; 2973 -3.2; 3270 -4.3; 3597 -5.4; 3957 -6.3; 4353 -7.5; 4788 -7.0; 5267 -5.1; 5793 -2.6; 6373 -3.2; 7010 -4.9; 7711 -3.4; 8482 -3.4; 9330 -3.4; 10263 -3.4; 11289 -3.4; 12418 -3.4; 13660 -4.6; 15026 -4.6; 16529 -3.4; 18182 -3.4; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 2.03 | 1.7 dB  |
| Peaking | 138 Hz   | 0.57 | -1.8 dB |
| Peaking | 675 Hz   | 1.18 | 3.1 dB  |
| Peaking | 1946 Hz  | 6.51 | -1.6 dB |
| Peaking | 4392 Hz  | 3.59 | -4.6 dB |
| Peaking | 1057 Hz  | 6.86 | -0.5 dB |
| Peaking | 2723 Hz  | 4.74 | 1.3 dB  |
| Peaking | 3511 Hz  | 6.21 | -0.9 dB |
| Peaking | 14264 Hz | 1.09 | 0.5 dB  |
| Peaking | 14324 Hz | 3.98 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20Wireless/Bose%20SoundSport%20Wireless.png)