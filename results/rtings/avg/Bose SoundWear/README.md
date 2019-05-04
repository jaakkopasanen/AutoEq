# Bose SoundWear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -1.0; 155 -2.5; 170 -3.7; 187 -3.7; 206 -2.7; 227 -0.5; 249 -1.5; 274 -3.0; 302 -4.7; 332 -5.4; 365 -4.8; 402 -8.0; 442 -8.1; 486 -8.5; 535 -10.2; 588 -8.6; 647 -6.1; 712 -7.4; 783 -8.7; 861 -8.5; 947 -6.6; 1042 -5.0; 1146 -5.9; 1261 -7.3; 1387 -3.6; 1526 -1.4; 1678 -2.0; 1846 -6.1; 2031 -8.9; 2234 -10.5; 2457 -9.6; 2703 -9.4; 2973 -10.4; 3270 -12.5; 3597 -13.6; 3957 -12.4; 4353 -13.7; 4788 -14.0; 5267 -13.3; 5793 -7.6; 6373 -5.6; 7010 -4.4; 7711 -6.2; 8482 -8.3; 9330 -8.1; 10263 -6.6; 11289 -9.8; 12418 -14.6; 13660 -16.7; 15026 -16.8; 16529 -11.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundWear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundWear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.31 | 5.8 dB   |
| Peaking | 127 Hz   | 0.78 | 3.6 dB   |
| Peaking | 1589 Hz  | 6.24 | 7.1 dB   |
| Peaking | 3822 Hz  | 1.46 | -7.4 dB  |
| Peaking | 14318 Hz | 1.92 | -12.0 dB |
| Peaking | 183 Hz   | 3.66 | -2.6 dB  |
| Peaking | 234 Hz   | 3.19 | 4.1 dB   |
| Peaking | 513 Hz   | 2.37 | -3.6 dB  |
| Peaking | 5165 Hz  | 4.71 | -5.6 dB  |
| Peaking | 6388 Hz  | 2.46 | 5.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB   |
| Peaking | 62 Hz    | 1.41 | 4.7 dB   |
| Peaking | 125 Hz   | 1.41 | 4.2 dB   |
| Peaking | 250 Hz   | 1.41 | 3.9 dB   |
| Peaking | 500 Hz   | 1.41 | -3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundWear/Bose%20SoundWear.png)