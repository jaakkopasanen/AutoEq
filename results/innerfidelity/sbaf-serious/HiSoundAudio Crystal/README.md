# HiSoundAudio Crystal
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.1; 28 -6.3; 31 -6.4; 34 -6.5; 37 -6.6; 41 -6.7; 45 -6.9; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.4; 87 -8.8; 96 -9.0; 106 -9.3; 116 -9.3; 128 -9.5; 141 -9.6; 155 -9.7; 170 -9.7; 187 -9.5; 206 -9.4; 227 -9.1; 249 -8.9; 274 -8.5; 302 -8.2; 332 -7.8; 365 -7.4; 402 -6.9; 442 -6.3; 486 -6.0; 535 -5.5; 588 -4.8; 647 -4.5; 712 -4.3; 783 -4.0; 861 -4.2; 947 -4.6; 1042 -4.9; 1146 -5.4; 1261 -6.3; 1387 -7.3; 1526 -8.5; 1678 -9.2; 1846 -9.3; 2031 -8.3; 2234 -6.5; 2457 -4.7; 2703 -0.5; 2973 -2.1; 3270 -5.3; 3597 -4.2; 3957 -2.9; 4353 -5.0; 4788 -5.9; 5267 -6.2; 5793 -8.2; 6373 -11.5; 7010 -9.3; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -7.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 185 Hz   | 0.51 | -3.8 dB |
| Peaking | 1528 Hz  | 0.35 | 5.8 dB  |
| Peaking | 1750 Hz  | 1.22 | -8.6 dB |
| Peaking | 2724 Hz  | 6.3  | 5.7 dB  |
| Peaking | 6418 Hz  | 4.29 | -6.6 dB |
| Peaking | 21 Hz    | 1    | 0.8 dB  |
| Peaking | 3907 Hz  | 2.77 | -1.5 dB |
| Peaking | 4010 Hz  | 7.24 | 3.5 dB  |
| Peaking | 16368 Hz | 2.72 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Crystal/HiSoundAudio%20Crystal.png)