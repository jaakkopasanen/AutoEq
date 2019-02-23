# Brainwavz S5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.5; 25 -11.6; 28 -11.7; 31 -11.8; 34 -11.9; 37 -11.9; 41 -12.0; 45 -12.1; 49 -12.2; 54 -12.2; 60 -12.4; 66 -12.5; 72 -12.6; 79 -12.7; 87 -12.9; 96 -13.0; 106 -12.9; 116 -12.8; 128 -12.7; 141 -12.5; 155 -12.3; 170 -11.9; 187 -11.5; 206 -11.1; 227 -10.5; 249 -10.0; 274 -9.4; 302 -8.8; 332 -8.1; 365 -7.4; 402 -6.8; 442 -6.1; 486 -5.5; 535 -4.9; 588 -3.9; 647 -3.3; 712 -2.8; 783 -2.2; 861 -2.0; 947 -2.1; 1042 -2.2; 1146 -2.2; 1261 -1.9; 1387 -2.4; 1526 -2.3; 1678 -2.3; 1846 -1.8; 2031 -1.3; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.6; 3270 -1.6; 3597 -3.9; 3957 -6.3; 4353 -9.3; 4788 -11.2; 5267 -13.6; 5793 -12.7; 6373 -8.8; 7010 -5.9; 7711 -6.4; 8482 -10.0; 9330 -10.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.3; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.31 | -4.5 dB  |
| Peaking | 151 Hz   | 0.55 | -4.6 dB  |
| Peaking | 1796 Hz  | 0.35 | 6.0 dB   |
| Peaking | 5278 Hz  | 2.29 | -10.6 dB |
| Peaking | 1563 Hz  | 3.03 | -1.7 dB  |
| Peaking | 2907 Hz  | 3.56 | 2.3 dB   |
| Peaking | 7213 Hz  | 5.56 | 2.8 dB   |
| Peaking | 9008 Hz  | 4.97 | -5.5 dB  |
| Peaking | 15023 Hz | 4.94 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S5/Brainwavz%20S5.png)