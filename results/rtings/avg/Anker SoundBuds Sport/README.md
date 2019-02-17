# Anker SoundBuds Sport
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.2; 45 -3.1; 49 -4.8; 54 -6.7; 60 -8.5; 66 -9.9; 72 -10.9; 79 -11.9; 87 -12.9; 96 -13.7; 106 -14.6; 116 -15.3; 128 -16.0; 141 -16.5; 155 -16.7; 170 -16.8; 187 -17.0; 206 -17.1; 227 -17.0; 249 -16.5; 274 -15.9; 302 -15.2; 332 -14.5; 365 -13.7; 402 -12.9; 442 -12.1; 486 -11.2; 535 -10.1; 588 -9.0; 647 -7.8; 712 -6.8; 783 -6.0; 861 -5.7; 947 -6.1; 1042 -6.7; 1146 -6.9; 1261 -6.9; 1387 -6.7; 1526 -6.5; 1678 -6.4; 1846 -6.4; 2031 -6.4; 2234 -5.8; 2457 -5.1; 2703 -5.0; 2973 -5.4; 3270 -5.7; 3597 -5.6; 3957 -5.2; 4353 -4.9; 4788 -3.8; 5267 -3.0; 5793 -2.7; 6373 -4.2; 7010 -6.5; 7711 -10.7; 8482 -12.6; 9330 -9.7; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -12.5; 15026 -15.5; 16529 -11.7; 18182 -9.2; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.98 | 8.7 dB   |
| Peaking | 169 Hz   | 0.51 | -11.5 dB |
| Peaking | 8462 Hz  | 3.14 | -10.6 dB |
| Peaking | 11998 Hz | 0.41 | 17.9 dB  |
| Peaking | 14543 Hz | 0.59 | -23.5 dB |
| Peaking | 17 Hz    | 2.8  | 2.4 dB   |
| Peaking | 805 Hz   | 3.19 | 2.8 dB   |
| Peaking | 4878 Hz  | 0.86 | -1.8 dB  |
| Peaking | 5674 Hz  | 2.57 | 3.6 dB   |
| Peaking | 17090 Hz | 4.21 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -9.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Sport/Anker%20SoundBuds%20Sport.png)