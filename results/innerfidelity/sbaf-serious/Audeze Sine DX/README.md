# Audeze SINE DX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.6; 28 -3.8; 31 -4.0; 34 -4.2; 37 -4.4; 41 -4.5; 45 -4.4; 49 -4.5; 54 -4.6; 60 -4.9; 66 -5.1; 72 -5.3; 79 -5.5; 87 -5.8; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.9; 155 -7.1; 170 -7.2; 187 -7.2; 206 -7.2; 227 -7.2; 249 -7.4; 274 -7.5; 302 -7.5; 332 -7.6; 365 -7.6; 402 -7.7; 442 -7.7; 486 -8.0; 535 -8.1; 588 -7.7; 647 -7.7; 712 -8.2; 783 -8.5; 861 -9.2; 947 -9.8; 1042 -10.6; 1146 -11.3; 1261 -12.1; 1387 -12.3; 1526 -13.9; 1678 -13.4; 1846 -11.7; 2031 -9.4; 2234 -7.2; 2457 -5.7; 2703 -5.3; 2973 -4.4; 3270 -3.5; 3597 -2.1; 3957 -2.7; 4353 -4.2; 4788 -2.8; 5267 -0.5; 5793 -0.5; 6373 -3.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -10.8; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze SINE DX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze SINE DX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.07 | 3.2 dB   |
| Peaking | 56 Hz    | 1.8  | 1.5 dB   |
| Peaking | 1647 Hz  | 0.94 | -10.1 dB |
| Peaking | 2769 Hz  | 0.89 | 7.0 dB   |
| Peaking | 5577 Hz  | 3.58 | 5.4 dB   |
| Peaking | 309 Hz   | 0.67 | -0.8 dB  |
| Peaking | 713 Hz   | 1.94 | 0.7 dB   |
| Peaking | 2999 Hz  | 5.45 | -1.0 dB  |
| Peaking | 3626 Hz  | 7.69 | 1.7 dB   |
| Peaking | 19386 Hz | 1.24 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20SINE%20DX/Audeze%20SINE%20DX.png)