# Mpow Jaws
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.0; 25 -13.1; 28 -13.1; 31 -13.2; 34 -13.2; 37 -13.3; 41 -13.4; 45 -13.5; 49 -13.5; 54 -13.6; 60 -13.8; 66 -14.0; 72 -14.2; 79 -14.4; 87 -14.6; 96 -14.9; 106 -15.0; 116 -15.1; 128 -15.2; 141 -15.2; 155 -15.1; 170 -14.9; 187 -14.5; 206 -14.1; 227 -13.7; 249 -13.5; 274 -13.1; 302 -12.0; 332 -10.9; 365 -10.2; 402 -10.0; 442 -9.8; 486 -9.4; 535 -8.6; 588 -7.7; 647 -6.8; 712 -5.9; 783 -5.2; 861 -5.1; 947 -5.5; 1042 -5.3; 1146 -5.6; 1261 -5.7; 1387 -5.3; 1526 -4.7; 1678 -4.2; 1846 -3.8; 2031 -3.2; 2234 -2.0; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -1.5; 4353 -2.6; 4788 -3.1; 5267 -0.6; 5793 -1.8; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mpow Jaws GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mpow Jaws ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.23 | -6.3 dB |
| Peaking | 135 Hz  | 0.76 | -5.0 dB |
| Peaking | 263 Hz  | 1.14 | -3.3 dB |
| Peaking | 2919 Hz | 1.03 | 6.2 dB  |
| Peaking | 5616 Hz | 3.54 | 3.9 dB  |
| Peaking | 488 Hz  | 3.73 | -1.2 dB |
| Peaking | 807 Hz  | 2.39 | 1.8 dB  |
| Peaking | 1368 Hz | 1.81 | -0.4 dB |
| Peaking | 6699 Hz | 9.59 | 2.8 dB  |
| Peaking | 7922 Hz | 1.74 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Mpow%20Jaws/Mpow%20Jaws.png)