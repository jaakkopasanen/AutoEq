# Bose SoundTrue Ultra In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.5; 25 -8.6; 28 -8.5; 31 -8.5; 34 -8.5; 37 -8.4; 41 -8.4; 45 -8.3; 49 -8.3; 54 -8.1; 60 -7.9; 66 -7.8; 72 -7.7; 79 -7.6; 87 -7.5; 96 -7.2; 106 -6.9; 116 -6.5; 128 -6.0; 141 -5.6; 155 -5.6; 170 -5.6; 187 -5.2; 206 -4.8; 227 -4.3; 249 -4.0; 274 -3.6; 302 -3.3; 332 -2.9; 365 -2.5; 402 -2.2; 442 -2.0; 486 -1.7; 535 -1.3; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.7; 861 -1.6; 947 -2.7; 1042 -3.5; 1146 -3.9; 1261 -4.1; 1387 -4.2; 1526 -4.4; 1678 -4.7; 1846 -5.0; 2031 -5.2; 2234 -5.0; 2457 -4.3; 2703 -3.8; 2973 -3.4; 3270 -3.4; 3597 -3.5; 3957 -3.7; 4353 -4.3; 4788 -5.4; 5267 -6.5; 5793 -7.4; 6373 -6.4; 7010 -4.0; 7711 -3.4; 8482 -3.7; 9330 -3.7; 10263 -4.0; 11289 -3.8; 12418 -3.7; 13660 -3.7; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Ultra In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Ultra In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.22 | -4.9 dB |
| Peaking | 749 Hz  | 0.73 | 4.7 dB  |
| Peaking | 1255 Hz | 0.9  | -3.4 dB |
| Peaking | 5876 Hz | 3.25 | -4.2 dB |
| Peaking | 7390 Hz | 4.03 | 1.5 dB  |
| Peaking | 782 Hz  | 3.53 | 1.1 dB  |
| Peaking | 932 Hz  | 1.45 | -0.9 dB |
| Peaking | 1394 Hz | 2.3  | 0.9 dB  |
| Peaking | 2079 Hz | 3.12 | -1.1 dB |
| Peaking | 3129 Hz | 2.51 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundTrue%20Ultra%20In-Ear/Bose%20SoundTrue%20Ultra%20In-Ear.png)