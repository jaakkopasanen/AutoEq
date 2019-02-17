# HiSoundAudio Crystal
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.2; 37 -8.3; 41 -8.5; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.6; 72 -9.9; 79 -10.1; 87 -10.5; 96 -10.8; 106 -11.0; 116 -11.1; 128 -11.3; 141 -11.4; 155 -11.5; 170 -11.4; 187 -11.3; 206 -11.2; 227 -10.9; 249 -10.7; 274 -10.3; 302 -9.9; 332 -9.6; 365 -9.1; 402 -8.6; 442 -8.1; 486 -7.8; 535 -7.3; 588 -6.6; 647 -6.3; 712 -6.1; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -7.2; 1261 -8.1; 1387 -9.1; 1526 -10.2; 1678 -11.0; 1846 -11.1; 2031 -10.0; 2234 -8.3; 2457 -6.5; 2703 -0.5; 2973 -3.7; 3270 -7.0; 3597 -6.0; 3957 -4.6; 4353 -6.7; 4788 -7.7; 5267 -8.0; 5793 -10.0; 6373 -13.2; 7010 -11.1; 7711 -7.3; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -8.0; 15026 -8.6; 16529 -9.6; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 102 Hz   |  0.55 | -3.9 dB |
| Peaking | 226 Hz   |  1.09 | -2.7 dB |
| Peaking | 1789 Hz  |  2.45 | -5.2 dB |
| Peaking | 2748 Hz  |  7.02 | 7.6 dB  |
| Peaking | 6450 Hz  |  4.68 | -7.3 dB |
| Peaking | 25 Hz    |  1.76 | -0.8 dB |
| Peaking | 781 Hz   |  2.85 | 1.5 dB  |
| Peaking | 3943 Hz  | 10.75 | 2.2 dB  |
| Peaking | 8489 Hz  |  4.44 | 1.1 dB  |
| Peaking | 16256 Hz |  1.58 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Crystal/HiSoundAudio%20Crystal.png)