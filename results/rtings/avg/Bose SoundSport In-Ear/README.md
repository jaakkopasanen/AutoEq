# Bose SoundSport In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -2.2; 72 -3.4; 79 -4.4; 87 -5.4; 96 -6.2; 106 -6.9; 116 -7.4; 128 -7.8; 141 -8.1; 155 -8.3; 170 -8.5; 187 -8.6; 206 -8.6; 227 -8.6; 249 -8.6; 274 -8.7; 302 -8.8; 332 -8.8; 365 -9.0; 402 -9.2; 442 -9.2; 486 -9.2; 535 -9.1; 588 -8.8; 647 -8.2; 712 -7.5; 783 -6.8; 861 -6.4; 947 -6.3; 1042 -6.6; 1146 -7.1; 1261 -7.7; 1387 -8.5; 1526 -9.2; 1678 -9.7; 1846 -9.9; 2031 -9.6; 2234 -8.3; 2457 -6.6; 2703 -5.8; 2973 -5.4; 3270 -5.5; 3597 -5.9; 3957 -6.6; 4353 -7.7; 4788 -8.4; 5267 -8.4; 5793 -7.7; 6373 -9.4; 7010 -11.5; 7711 -9.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.6; 13660 -8.8; 15026 -7.8; 16529 -7.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.48 | 9.3 dB  |
| Peaking | 130 Hz   | 0.3  | -4.6 dB |
| Peaking | 1779 Hz  | 3.23 | -3.6 dB |
| Peaking | 6966 Hz  | 4.26 | -5.3 dB |
| Peaking | 14091 Hz | 2.94 | -2.4 dB |
| Peaking | 532 Hz   | 2.9  | -1.1 dB |
| Peaking | 878 Hz   | 3.6  | 1.4 dB  |
| Peaking | 3110 Hz  | 3.32 | 1.8 dB  |
| Peaking | 4812 Hz  | 4.53 | -1.8 dB |
| Peaking | 8951 Hz  | 4.25 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20In-Ear/Bose%20SoundSport%20In-Ear.png)