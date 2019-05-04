# Bose SoundTrue Around-Ear II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.9; 25 -6.8; 28 -6.7; 31 -6.5; 34 -6.3; 37 -6.0; 41 -5.7; 45 -5.4; 49 -5.1; 54 -4.8; 60 -4.7; 66 -4.7; 72 -4.7; 79 -4.9; 87 -5.1; 96 -5.5; 106 -5.9; 116 -6.4; 128 -6.9; 141 -7.3; 155 -7.6; 170 -7.7; 187 -7.4; 206 -7.3; 227 -7.2; 249 -6.6; 274 -5.9; 302 -5.3; 332 -4.7; 365 -4.0; 402 -3.7; 442 -3.5; 486 -3.4; 535 -3.3; 588 -3.4; 647 -3.9; 712 -4.6; 783 -5.6; 861 -6.4; 947 -7.1; 1042 -7.3; 1146 -7.1; 1261 -7.0; 1387 -7.1; 1526 -7.4; 1678 -7.9; 1846 -8.2; 2031 -8.1; 2234 -7.4; 2457 -6.6; 2703 -7.7; 2973 -8.3; 3270 -8.6; 3597 -7.9; 3957 -6.7; 4353 -4.5; 4788 -2.1; 5267 -0.5; 5793 -3.6; 6373 -4.0; 7010 -5.4; 7711 -6.7; 8482 -6.7; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 190 Hz  | 1.74 | -2.3 dB |
| Peaking | 525 Hz  | 0.96 | 4.6 dB  |
| Peaking | 1109 Hz | 0.46 | -2.6 dB |
| Peaking | 3365 Hz | 3.21 | -2.4 dB |
| Peaking | 5124 Hz | 3.65 | 6.2 dB  |
| Peaking | 21 Hz   | 0.9  | -1.1 dB |
| Peaking | 63 Hz   | 1.7  | 1.7 dB  |
| Peaking | 1900 Hz | 7.48 | -0.9 dB |
| Peaking | 3445 Hz | 0.35 | 0.2 dB  |
| Peaking | 8140 Hz | 6.61 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundTrue%20Around-Ear%20II/Bose%20SoundTrue%20Around-Ear%20II.png)