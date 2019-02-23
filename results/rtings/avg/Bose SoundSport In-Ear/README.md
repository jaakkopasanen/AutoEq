# Bose SoundSport In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.9; 72 -2.0; 79 -3.1; 87 -4.0; 96 -4.8; 106 -5.5; 116 -6.0; 128 -6.4; 141 -6.7; 155 -7.0; 170 -7.1; 187 -7.3; 206 -7.3; 227 -7.3; 249 -7.3; 274 -7.4; 302 -7.5; 332 -7.5; 365 -7.7; 402 -7.9; 442 -7.8; 486 -7.8; 535 -7.7; 588 -7.4; 647 -6.9; 712 -6.1; 783 -5.4; 861 -5.0; 947 -5.0; 1042 -5.3; 1146 -5.8; 1261 -6.4; 1387 -7.1; 1526 -7.9; 1678 -8.4; 1846 -8.6; 2031 -8.3; 2234 -7.0; 2457 -5.2; 2703 -4.5; 2973 -4.1; 3270 -4.1; 3597 -4.5; 3957 -5.2; 4353 -6.4; 4788 -7.1; 5267 -7.1; 5793 -6.3; 6373 -8.1; 7010 -10.2; 7711 -8.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.49 | 7.5 dB  |
| Peaking | 490 Hz  | 0.11 | -2.3 dB |
| Peaking | 898 Hz  | 1.68 | 3.8 dB  |
| Peaking | 3128 Hz | 2.16 | 4.3 dB  |
| Peaking | 7087 Hz | 7.07 | -3.9 dB |
| Peaking | 64 Hz   | 2.2  | 2.5 dB  |
| Peaking | 70 Hz   | 0.71 | -1.4 dB |
| Peaking | 278 Hz  | 1.63 | 0.7 dB  |
| Peaking | 1930 Hz | 3.6  | -1.5 dB |
| Peaking | 2458 Hz | 5.88 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20In-Ear/Bose%20SoundSport%20In-Ear.png)