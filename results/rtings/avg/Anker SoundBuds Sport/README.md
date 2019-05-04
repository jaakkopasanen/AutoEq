# Anker SoundBuds Sport
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -2.5; 45 -4.6; 49 -6.4; 54 -8.1; 60 -9.6; 66 -10.8; 72 -11.6; 79 -12.4; 87 -13.0; 96 -13.6; 106 -14.0; 116 -14.2; 128 -14.4; 141 -14.4; 155 -14.3; 170 -14.1; 187 -13.9; 206 -13.9; 227 -13.6; 249 -13.1; 274 -12.5; 302 -11.8; 332 -11.2; 365 -10.4; 402 -9.7; 442 -8.8; 486 -8.0; 535 -6.9; 588 -5.9; 647 -4.7; 712 -3.6; 783 -2.8; 861 -2.5; 947 -2.9; 1042 -3.6; 1146 -3.8; 1261 -3.8; 1387 -3.6; 1526 -3.4; 1678 -3.3; 1846 -3.4; 2031 -3.5; 2234 -3.4; 2457 -2.7; 2703 -2.2; 2973 -2.1; 3270 -2.2; 3597 -2.0; 3957 -1.6; 4353 -1.1; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.3; 8482 -8.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -11.7; 16529 -8.0; 18182 -6.5; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.77 | 12.3 dB |
| Peaking | 109 Hz   | 0.27 | -9.8 dB |
| Peaking | 816 Hz   | 0.88 | 5.5 dB  |
| Peaking | 3125 Hz  | 1.12 | 4.0 dB  |
| Peaking | 5464 Hz  | 2.86 | 5.4 dB  |
| Peaking | 495 Hz   | 3.14 | -0.3 dB |
| Peaking | 6577 Hz  | 6.23 | 2.6 dB  |
| Peaking | 8097 Hz  | 5.25 | -4.5 dB |
| Peaking | 12955 Hz | 2.78 | 1.7 dB  |
| Peaking | 14834 Hz | 2.34 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Sport/Anker%20SoundBuds%20Sport.png)