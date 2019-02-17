# Audeze Sine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.6; 37 -0.6; 41 -0.7; 45 -1.0; 49 -1.2; 54 -1.5; 60 -1.9; 66 -2.4; 72 -2.7; 79 -2.8; 87 -3.2; 96 -3.9; 106 -4.3; 116 -4.6; 128 -5.0; 141 -5.1; 155 -5.4; 170 -5.4; 187 -5.3; 206 -5.1; 227 -5.5; 249 -5.8; 274 -6.0; 302 -6.1; 332 -6.1; 365 -6.1; 402 -6.1; 442 -6.4; 486 -6.6; 535 -6.5; 588 -6.5; 647 -6.2; 712 -6.1; 783 -6.1; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -7.0; 1261 -7.4; 1387 -7.8; 1526 -7.6; 1678 -7.5; 1846 -7.9; 2031 -8.3; 2234 -8.6; 2457 -8.2; 2703 -8.9; 2973 -9.3; 3270 -9.5; 3597 -9.3; 3957 -7.2; 4353 -4.6; 4788 -3.4; 5267 -3.3; 5793 -2.6; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.7; 11289 -11.7; 12418 -11.1; 13660 -9.9; 15026 -10.0; 16529 -12.3; 18182 -14.2; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.37 | 6.1 dB  |
| Peaking | 3434 Hz  | 1.05 | -5.9 dB |
| Peaking | 5213 Hz  | 1.14 | 7.3 dB  |
| Peaking | 11437 Hz | 3.09 | -4.5 dB |
| Peaking | 18893 Hz | 0.55 | -8.2 dB |
| Peaking | 840 Hz   | 2.36 | 0.6 dB  |
| Peaking | 1376 Hz  | 3.43 | -0.7 dB |
| Peaking | 5658 Hz  | 3.51 | -2.4 dB |
| Peaking | 6715 Hz  | 2.01 | 3.7 dB  |
| Peaking | 7504 Hz  | 4.06 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Audeze%20Sine/Audeze%20Sine.png)