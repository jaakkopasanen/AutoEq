# Bose SoundTrue Around-Ear II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.6; 25 -7.5; 28 -7.3; 31 -7.1; 34 -6.9; 37 -6.6; 41 -6.3; 45 -6.1; 49 -5.8; 54 -5.6; 60 -5.4; 66 -5.4; 72 -5.4; 79 -5.6; 87 -5.9; 96 -6.3; 106 -6.7; 116 -7.1; 128 -7.5; 141 -8.0; 155 -8.3; 170 -8.4; 187 -8.1; 206 -7.9; 227 -7.8; 249 -7.2; 274 -6.5; 302 -5.9; 332 -5.2; 365 -4.6; 402 -4.2; 442 -4.1; 486 -3.8; 535 -3.7; 588 -3.8; 647 -4.3; 712 -5.0; 783 -5.9; 861 -6.8; 947 -7.5; 1042 -7.7; 1146 -7.5; 1261 -7.4; 1387 -7.4; 1526 -7.7; 1678 -8.1; 1846 -8.4; 2031 -8.2; 2234 -7.1; 2457 -6.0; 2703 -7.7; 2973 -8.7; 3270 -9.4; 3597 -8.6; 3957 -7.6; 4353 -5.3; 4788 -2.3; 5267 -0.5; 5793 -4.4; 6373 -5.3; 7010 -5.9; 7711 -6.3; 8482 -7.6; 9330 -6.8; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 188 Hz  | 1.56 | -2.5 dB |
| Peaking | 565 Hz  | 0.87 | 5.3 dB  |
| Peaking | 906 Hz  | 0.65 | -3.5 dB |
| Peaking | 3383 Hz | 3.49 | -3.1 dB |
| Peaking | 5134 Hz | 4.62 | 6.7 dB  |
| Peaking | 20 Hz   | 1.08 | -1.3 dB |
| Peaking | 63 Hz   | 1.85 | 1.4 dB  |
| Peaking | 1918 Hz | 5.65 | -1.1 dB |
| Peaking | 2427 Hz | 9.7  | 1.7 dB  |
| Peaking | 8642 Hz | 7.74 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundTrue%20Around-Ear%20II/Bose%20SoundTrue%20Around-Ear%20II.png)