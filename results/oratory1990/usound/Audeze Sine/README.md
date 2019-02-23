# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -0.9; 34 -0.9; 37 -0.9; 41 -1.0; 45 -1.3; 49 -1.5; 54 -1.8; 60 -2.2; 66 -2.6; 72 -2.9; 79 -3.1; 87 -3.5; 96 -4.1; 106 -4.5; 116 -4.9; 128 -5.2; 141 -5.4; 155 -5.7; 170 -5.7; 187 -5.5; 206 -5.4; 227 -5.8; 249 -6.1; 274 -6.3; 302 -6.4; 332 -6.4; 365 -6.4; 402 -6.4; 442 -6.7; 486 -6.9; 535 -6.8; 588 -6.7; 647 -6.5; 712 -6.4; 783 -6.4; 861 -6.4; 947 -6.7; 1042 -6.8; 1146 -7.2; 1261 -7.6; 1387 -8.1; 1526 -7.9; 1678 -7.8; 1846 -8.2; 2031 -8.6; 2234 -8.9; 2457 -8.5; 2703 -9.2; 2973 -9.6; 3270 -9.8; 3597 -9.5; 3957 -7.5; 4353 -4.8; 4788 -3.7; 5267 -3.6; 5793 -2.9; 6373 -2.1; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -8.9; 11289 -12.0; 12418 -11.4; 13660 -10.2; 15026 -10.3; 16529 -12.6; 18182 -14.5; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.61 | 5.2 dB  |
| Peaking | 57 Hz    | 0.92 | 2.4 dB  |
| Peaking | 2420 Hz  | 1.56 | -3.2 dB |
| Peaking | 11816 Hz | 4.14 | -5.2 dB |
| Peaking | 18651 Hz | 0.75 | -9.3 dB |
| Peaking | 490 Hz   | 2.46 | -0.7 dB |
| Peaking | 1356 Hz  | 3.2  | -1.1 dB |
| Peaking | 2434 Hz  | 5.09 | 1.0 dB  |
| Peaking | 3426 Hz  | 3.41 | -3.3 dB |
| Peaking | 5746 Hz  | 1.69 | 4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -9.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Audeze%20Sine/Audeze%20Sine.png)