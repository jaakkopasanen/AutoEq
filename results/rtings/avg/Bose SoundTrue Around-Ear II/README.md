# Bose SoundTrue Around-Ear II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.3; 25 -6.2; 28 -6.1; 31 -5.9; 34 -5.6; 37 -5.4; 41 -5.1; 45 -4.8; 49 -4.6; 54 -4.3; 60 -4.2; 66 -4.2; 72 -4.2; 79 -4.4; 87 -4.7; 96 -5.0; 106 -5.5; 116 -5.9; 128 -6.3; 141 -6.8; 155 -7.0; 170 -7.1; 187 -6.9; 206 -6.7; 227 -6.6; 249 -5.9; 274 -5.2; 302 -4.7; 332 -4.0; 365 -3.4; 402 -3.0; 442 -2.8; 486 -2.6; 535 -2.5; 588 -2.6; 647 -3.0; 712 -3.8; 783 -4.7; 861 -5.6; 947 -6.3; 1042 -6.5; 1146 -6.2; 1261 -6.1; 1387 -6.2; 1526 -6.5; 1678 -6.9; 1846 -7.1; 2031 -6.9; 2234 -5.8; 2457 -4.8; 2703 -6.5; 2973 -7.4; 3270 -8.1; 3597 -7.4; 3957 -6.4; 4353 -4.1; 4788 -1.1; 5267 -0.5; 5793 -3.2; 6373 -4.1; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 1.48 | 2.6 dB  |
| Peaking | 508 Hz  | 1.34 | 4.5 dB  |
| Peaking | 2453 Hz | 4.18 | 3.5 dB  |
| Peaking | 3507 Hz | 0.88 | -3.6 dB |
| Peaking | 5077 Hz | 2.29 | 8.5 dB  |
| Peaking | 97 Hz   | 1.88 | 1.1 dB  |
| Peaking | 329 Hz  | 1.43 | 3.2 dB  |
| Peaking | 364 Hz  | 0.45 | -3.0 dB |
| Peaking | 822 Hz  | 1.01 | 3.0 dB  |
| Peaking | 934 Hz  | 2.69 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 4.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundTrue%20Around-Ear%20II/Bose%20SoundTrue%20Around-Ear%20II.png)