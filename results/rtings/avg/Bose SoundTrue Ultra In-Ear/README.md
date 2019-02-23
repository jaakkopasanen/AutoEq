# Bose SoundTrue Ultra In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.8; 25 -3.9; 28 -3.8; 31 -3.8; 34 -3.7; 37 -3.7; 41 -3.6; 45 -3.6; 49 -3.5; 54 -3.5; 60 -3.6; 66 -3.7; 72 -3.8; 79 -3.9; 87 -4.0; 96 -4.3; 106 -4.4; 116 -4.4; 128 -4.5; 141 -4.5; 155 -4.8; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.5; 249 -4.2; 274 -3.8; 302 -3.5; 332 -3.1; 365 -2.7; 402 -2.4; 442 -2.1; 486 -1.8; 535 -1.4; 588 -1.1; 647 -0.7; 712 -0.5; 783 -0.7; 861 -1.6; 947 -2.7; 1042 -3.5; 1146 -3.9; 1261 -4.1; 1387 -4.2; 1526 -4.3; 1678 -4.6; 1846 -4.9; 2031 -5.0; 2234 -4.4; 2457 -3.6; 2703 -3.4; 2973 -3.6; 3270 -3.8; 3597 -3.9; 3957 -4.2; 4353 -4.8; 4788 -5.2; 5267 -6.2; 5793 -7.6; 6373 -7.6; 7010 -4.2; 7711 -3.3; 8482 -3.6; 9330 -3.6; 10263 -4.7; 11289 -3.7; 12418 -3.6; 13660 -3.6; 15026 -4.1; 16529 -3.6; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Ultra In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Ultra In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 179 Hz   | 1.12 | -1.6 dB |
| Peaking | 751 Hz   | 0.92 | 5.3 dB  |
| Peaking | 1113 Hz  | 0.86 | -3.5 dB |
| Peaking | 5878 Hz  | 3.95 | -4.5 dB |
| Peaking | 15297 Hz | 3.41 | -0.3 dB |
| Peaking | 2060 Hz  | 3.27 | -2.0 dB |
| Peaking | 2296 Hz  | 1.59 | 1.5 dB  |
| Peaking | 4464 Hz  | 2.75 | -0.6 dB |
| Peaking | 7497 Hz  | 7.97 | 1.5 dB  |
| Peaking | 10397 Hz | 9.9  | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundTrue%20Ultra%20In-Ear/Bose%20SoundTrue%20Ultra%20In-Ear.png)