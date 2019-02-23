# HiSoundAudio Golden Crystal
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.0; 28 -10.9; 31 -10.8; 34 -10.7; 37 -10.6; 41 -10.6; 45 -10.5; 49 -10.5; 54 -10.4; 60 -10.4; 66 -10.3; 72 -10.3; 79 -10.4; 87 -10.4; 96 -10.4; 106 -10.2; 116 -10.0; 128 -9.9; 141 -9.7; 155 -9.5; 170 -9.1; 187 -8.8; 206 -8.5; 227 -7.9; 249 -7.5; 274 -7.1; 302 -6.6; 332 -6.1; 365 -5.6; 402 -5.1; 442 -4.5; 486 -4.2; 535 -3.8; 588 -3.1; 647 -2.9; 712 -2.8; 783 -2.4; 861 -2.6; 947 -2.9; 1042 -3.5; 1146 -4.0; 1261 -4.3; 1387 -4.9; 1526 -5.4; 1678 -6.3; 1846 -6.8; 2031 -6.8; 2234 -4.1; 2457 -0.5; 2703 -1.9; 2973 -2.5; 3270 -1.6; 3597 -0.7; 3957 -0.8; 4353 -2.3; 4788 -2.8; 5267 -2.7; 5793 -4.2; 6373 -8.6; 7010 -11.6; 7711 -9.6; 8482 -6.6; 9330 -6.1; 10263 -8.0; 11289 -6.5; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -6.2; 18182 -7.1; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiSoundAudio Golden Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Golden Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.34 | -5.5 dB |
| Peaking | 132 Hz   | 1.1  | -3.1 dB |
| Peaking | 3606 Hz  | 1.27 | 4.8 dB  |
| Peaking | 5790 Hz  | 3.02 | 4.5 dB  |
| Peaking | 6801 Hz  | 2.47 | -9.0 dB |
| Peaking | 770 Hz   | 1.26 | 3.2 dB  |
| Peaking | 1980 Hz  | 2.23 | -3.6 dB |
| Peaking | 2438 Hz  | 6.64 | 4.6 dB  |
| Peaking | 10531 Hz | 9.25 | -2.5 dB |
| Peaking | 17768 Hz | 3.21 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Golden%20Crystal/HiSoundAudio%20Golden%20Crystal.png)