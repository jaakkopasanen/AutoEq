# SoundMAGIC HP200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.6; 25 -5.5; 28 -5.4; 31 -5.2; 34 -4.9; 37 -4.6; 41 -4.0; 45 -3.4; 49 -2.9; 54 -1.9; 60 -0.7; 66 -1.7; 72 -4.3; 79 -6.0; 87 -5.8; 96 -6.9; 106 -8.1; 116 -8.4; 128 -8.7; 141 -8.6; 155 -7.9; 170 -7.6; 187 -8.1; 206 -7.7; 227 -7.0; 249 -6.5; 274 -5.8; 302 -5.1; 332 -4.3; 365 -3.4; 402 -2.7; 442 -1.9; 486 -1.5; 535 -1.1; 588 -0.5; 647 -0.6; 712 -0.9; 783 -0.8; 861 -1.4; 947 -2.1; 1042 -2.8; 1146 -3.2; 1261 -3.7; 1387 -4.7; 1526 -6.1; 1678 -7.5; 1846 -9.0; 2031 -10.4; 2234 -11.8; 2457 -11.9; 2703 -11.2; 2973 -9.7; 3270 -9.2; 3597 -9.2; 3957 -9.0; 4353 -8.9; 4788 -6.7; 5267 -4.3; 5793 -3.7; 6373 -0.6; 7010 -3.0; 7711 -8.1; 8482 -14.8; 9330 -17.6; 10263 -14.1; 11289 -6.9; 12418 -2.6; 13660 -2.6; 15026 -2.6; 16529 -2.6; 18182 -2.6; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC HP200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC HP200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 121 Hz  | 1.6  | -5.9 dB  |
| Peaking | 209 Hz  | 2.12 | -4.1 dB  |
| Peaking | 2335 Hz | 1.91 | -9.6 dB  |
| Peaking | 3891 Hz | 2.99 | -4.9 dB  |
| Peaking | 9353 Hz | 3.65 | -16.8 dB |
| Peaking | 15 Hz   | 0.32 | -3.1 dB  |
| Peaking | 59 Hz   | 3.75 | 4.3 dB   |
| Peaking | 654 Hz  | 1.82 | 2.8 dB   |
| Peaking | 6511 Hz | 5.31 | 5.2 dB   |
| Peaking | 8419 Hz | 7.4  | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP200/SoundMAGIC%20HP200.png)