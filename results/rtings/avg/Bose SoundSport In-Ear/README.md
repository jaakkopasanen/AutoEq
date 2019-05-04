# Bose SoundSport In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.4; 54 -2.6; 60 -3.8; 66 -4.9; 72 -5.8; 79 -6.6; 87 -7.3; 96 -7.8; 106 -8.0; 116 -8.0; 128 -7.9; 141 -7.8; 155 -7.6; 170 -7.5; 187 -7.3; 206 -7.2; 227 -7.0; 249 -7.1; 274 -7.2; 302 -7.3; 332 -7.2; 365 -7.4; 402 -7.7; 442 -7.6; 486 -7.6; 535 -7.5; 588 -7.3; 647 -6.7; 712 -6.0; 783 -5.3; 861 -5.0; 947 -5.0; 1042 -5.2; 1146 -5.7; 1261 -6.3; 1387 -7.1; 1526 -7.8; 1678 -8.4; 1846 -8.7; 2031 -8.5; 2234 -7.6; 2457 -5.9; 2703 -4.8; 2973 -3.9; 3270 -3.7; 3597 -4.0; 3957 -4.7; 4353 -5.8; 4788 -7.2; 5267 -7.2; 5793 -6.0; 6373 -6.6; 7010 -10.0; 7711 -8.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.85 | 7.9 dB  |
| Peaking | 387 Hz  | 0.08 | -1.8 dB |
| Peaking | 895 Hz  | 1.84 | 3.5 dB  |
| Peaking | 3294 Hz | 2.51 | 4.4 dB  |
| Peaking | 7249 Hz | 8.93 | -4.1 dB |
| Peaking | 52 Hz   | 3.08 | 1.6 dB  |
| Peaking | 103 Hz  | 1.62 | -1.2 dB |
| Peaking | 247 Hz  | 1.36 | 1.0 dB  |
| Peaking | 1939 Hz | 3.31 | -1.7 dB |
| Peaking | 2636 Hz | 5.05 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20In-Ear/Bose%20SoundSport%20In-Ear.png)