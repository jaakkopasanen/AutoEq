# Anker SoundBuds Sport
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.8; 54 -3.6; 60 -5.4; 66 -6.8; 72 -7.9; 79 -8.8; 87 -9.8; 96 -10.7; 106 -11.5; 116 -12.3; 128 -12.9; 141 -13.4; 155 -13.7; 170 -13.8; 187 -13.9; 206 -14.1; 227 -13.9; 249 -13.4; 274 -12.9; 302 -12.1; 332 -11.4; 365 -10.6; 402 -9.8; 442 -9.0; 486 -8.1; 535 -7.1; 588 -6.0; 647 -4.8; 712 -3.7; 783 -2.9; 861 -2.6; 947 -3.0; 1042 -3.7; 1146 -3.9; 1261 -3.8; 1387 -3.6; 1526 -3.4; 1678 -3.3; 1846 -3.3; 2031 -3.4; 2234 -2.8; 2457 -2.0; 2703 -1.9; 2973 -2.3; 3270 -2.7; 3597 -2.6; 3957 -2.1; 4353 -1.8; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.0; 7711 -7.7; 8482 -9.6; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.4; 15026 -12.5; 16529 -8.7; 18182 -6.5; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.56 | 11.0 dB  |
| Peaking | 272 Hz   | 0.23 | -16.5 dB |
| Peaking | 696 Hz   | 0.32 | 14.2 dB  |
| Peaking | 5302 Hz  | 1.55 | 6.4 dB   |
| Peaking | 18092 Hz | 0.12 | -2.7 dB  |
| Peaking | 2682 Hz  | 5.29 | 1.5 dB   |
| Peaking | 8300 Hz  | 5.52 | -4.6 dB  |
| Peaking | 12560 Hz | 1.13 | 3.4 dB   |
| Peaking | 14786 Hz | 2.34 | -6.3 dB  |
| Peaking | 17767 Hz | 2.24 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Sport/Anker%20SoundBuds%20Sport.png)