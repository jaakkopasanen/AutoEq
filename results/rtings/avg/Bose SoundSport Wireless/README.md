# Bose SoundSport Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.5; 28 -7.8; 31 -8.1; 34 -8.4; 37 -8.5; 41 -8.7; 45 -8.8; 49 -8.9; 54 -8.8; 60 -8.7; 66 -8.6; 72 -8.4; 79 -8.2; 87 -7.9; 96 -7.8; 106 -7.5; 116 -7.2; 128 -6.8; 141 -6.3; 155 -5.9; 170 -5.5; 187 -5.1; 206 -4.6; 227 -4.2; 249 -4.0; 274 -3.7; 302 -3.4; 332 -3.8; 365 -3.0; 402 -2.3; 442 -2.1; 486 -1.9; 535 -1.4; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.6; 861 -1.1; 947 -2.0; 1042 -2.6; 1146 -2.8; 1261 -2.7; 1387 -2.7; 1526 -2.9; 1678 -3.6; 1846 -4.4; 2031 -4.9; 2234 -4.5; 2457 -3.5; 2703 -3.0; 2973 -3.1; 3270 -4.0; 3597 -5.0; 3957 -5.9; 4353 -6.9; 4788 -7.2; 5267 -5.2; 5793 -2.4; 6373 -2.0; 7010 -4.9; 7711 -3.7; 8482 -3.5; 9330 -3.5; 10263 -3.5; 11289 -3.5; 12418 -3.5; 13660 -3.9; 15026 -4.2; 16529 -3.5; 18182 -3.5; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.66 | -3.5 dB |
| Peaking | 81 Hz    | 0.62 | -3.7 dB |
| Peaking | 666 Hz   | 1.13 | 3.1 dB  |
| Peaking | 2008 Hz  | 5.15 | -1.9 dB |
| Peaking | 4489 Hz  | 4.1  | -4.2 dB |
| Peaking | 1058 Hz  | 7.45 | -0.5 dB |
| Peaking | 2814 Hz  | 6.85 | 1.0 dB  |
| Peaking | 6081 Hz  | 5.53 | 4.7 dB  |
| Peaking | 6229 Hz  | 2.23 | -2.1 dB |
| Peaking | 14409 Hz | 6.89 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20Wireless/Bose%20SoundSport%20Wireless.png)