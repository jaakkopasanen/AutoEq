# Bose SoundTrue Around-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.0; 23 -17.1; 25 -17.1; 28 -17.0; 31 -16.9; 34 -16.8; 37 -16.8; 41 -16.7; 45 -16.5; 49 -16.3; 54 -15.9; 60 -15.4; 66 -15.1; 72 -14.7; 79 -14.4; 87 -13.9; 96 -13.5; 106 -13.1; 116 -12.7; 128 -12.3; 141 -11.9; 155 -11.7; 170 -11.5; 187 -11.5; 206 -11.1; 227 -10.4; 249 -9.7; 274 -8.8; 302 -7.7; 332 -6.6; 365 -5.6; 402 -4.4; 442 -3.4; 486 -2.6; 535 -2.0; 588 -1.8; 647 -1.8; 712 -2.0; 783 -2.7; 861 -3.5; 947 -4.2; 1042 -4.4; 1146 -4.2; 1261 -3.4; 1387 -1.9; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.7; 2234 -1.6; 2457 -3.9; 2703 -7.4; 2973 -10.2; 3270 -11.5; 3597 -11.6; 3957 -10.8; 4353 -9.8; 4788 -9.5; 5267 -10.4; 5793 -11.5; 6373 -10.8; 7010 -7.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Around-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Around-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 17 Hz   | 0.1  | -10.2 dB |
| Peaking | 554 Hz  | 1.34 | 5.7 dB   |
| Peaking | 1971 Hz | 1.26 | 8.1 dB   |
| Peaking | 3290 Hz | 1.7  | -8.1 dB  |
| Peaking | 5872 Hz | 4.01 | -4.7 dB  |
| Peaking | 112 Hz  | 1.53 | 0.7 dB   |
| Peaking | 212 Hz  | 2.57 | -1.2 dB  |
| Peaking | 1089 Hz | 3    | -2.5 dB  |
| Peaking | 1117 Hz | 1.58 | 1.6 dB   |
| Peaking | 7720 Hz | 7.41 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 5.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 4000 Hz  | 1.41 | -7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bose%20SoundTrue%20Around-Ear/Bose%20SoundTrue%20Around-Ear.png)