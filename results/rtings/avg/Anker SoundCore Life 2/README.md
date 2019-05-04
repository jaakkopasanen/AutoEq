# Anker SoundCore Life 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.0; 25 -13.9; 28 -13.6; 31 -13.3; 34 -13.0; 37 -12.9; 41 -12.9; 45 -13.2; 49 -13.7; 54 -14.1; 60 -14.3; 66 -14.3; 72 -14.2; 79 -13.8; 87 -13.3; 96 -12.5; 106 -11.5; 116 -10.4; 128 -9.3; 141 -7.9; 155 -6.6; 170 -5.3; 187 -4.0; 206 -3.0; 227 -2.2; 249 -1.5; 274 -1.0; 302 -0.5; 332 -0.5; 365 -1.2; 402 -2.5; 442 -3.8; 486 -4.6; 535 -4.4; 588 -3.9; 647 -3.6; 712 -3.7; 783 -4.2; 861 -4.8; 947 -5.1; 1042 -3.9; 1146 -3.1; 1261 -4.3; 1387 -5.4; 1526 -5.6; 1678 -5.7; 1846 -6.3; 2031 -6.8; 2234 -5.8; 2457 -4.5; 2703 -4.4; 2973 -3.9; 3270 -6.9; 3597 -8.0; 3957 -8.1; 4353 -7.4; 4788 -5.5; 5267 -5.5; 5793 -4.6; 6373 -4.0; 7010 -7.4; 7711 -9.6; 8482 -9.4; 9330 -7.5; 10263 -5.3; 11289 -5.9; 12418 -10.5; 13660 -11.0; 15026 -5.6; 16529 -5.2; 18182 -5.2; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundCore Life 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundCore Life 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.71 | -7.5 dB |
| Peaking | 74 Hz    | 0.68 | -8.5 dB |
| Peaking | 269 Hz   | 1    | 6.1 dB  |
| Peaking | 11610 Hz | 0.62 | -3.0 dB |
| Peaking | 20064 Hz | 3.22 | -3.3 dB |
| Peaking | 3901 Hz  | 3.6  | -3.7 dB |
| Peaking | 6345 Hz  | 5.04 | 3.1 dB  |
| Peaking | 8041 Hz  | 1.81 | -8.6 dB |
| Peaking | 10534 Hz | 0.67 | 8.0 dB  |
| Peaking | 13115 Hz | 2.58 | -9.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 5.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundCore%20Life%202/Anker%20SoundCore%20Life%202.png)